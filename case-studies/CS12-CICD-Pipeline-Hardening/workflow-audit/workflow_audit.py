#!/usr/bin/env python3
"""workflow_audit.py: flag risky patterns in GitHub Actions workflow files.

Dependency-free (standard library only). It reads .github/workflows/*.yml|*.yaml
line by line rather than parsing YAML fully, so treat results as a triage list,
not a proof of safety.

Checks
  PIN-001  third-party action or reusable workflow not pinned to a 40-char commit SHA
  TRG-001  pull_request_target or workflow_run trigger (runs with secrets on untrusted input)
  TRG-002  issue_comment / pull_request_review_comment trigger (attacker-controlled text)
  CHK-001  checkout of the PR head ref/sha (pwn-request pattern when combined with TRG-001)
  INJ-001  untrusted github.event fields interpolated with ${{ }} inside run:
  PRM-001  no top-level permissions: block (falls back to repository default token scope)
  PRM-002  permissions: write-all
  SEC-001  secrets: inherit passed to a reusable workflow
  RUN-001  self-hosted runner in a workflow with an untrusted trigger
  CRD-001  actions/checkout without persist-credentials: false

Usage
  python3 workflow_audit.py <repo-root-or-workflows-dir> [--json]
Exit code is 1 if any HIGH finding is present, else 0 (usable as a CI gate).
"""
import json
import os
import re
import sys

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
USES_RE = re.compile(r"^\s*-?\s*uses:\s*['\"]?([^'\"\s#]+)")
UNTRUSTED_EXPR = re.compile(
    r"\$\{\{\s*github\.(event\.(pull_request\.(title|body|head\.ref|head\.label)"
    r"|issue\.(title|body)|comment\.body|review\.body|review_comment\.body"
    r"|head_commit\.message|commits|pages|workflow_run\.head_branch)|head_ref)"
)
HEAD_REF_RE = re.compile(
    r"ref:\s*\$\{\{\s*(github\.event\.pull_request\.head\.(sha|ref)|github\.head_ref"
    r"|github\.event\.workflow_run\.head_(sha|branch))"
)

SEVERITY = {
    "PIN-001": "HIGH", "TRG-001": "MEDIUM", "TRG-002": "MEDIUM", "CHK-001": "HIGH",
    "INJ-001": "HIGH", "PRM-001": "MEDIUM", "PRM-002": "HIGH", "SEC-001": "MEDIUM",
    "RUN-001": "HIGH", "CRD-001": "LOW",
}
ADVICE = {
    "PIN-001": "Pin to a full commit SHA with a version comment; let Dependabot/Renovate update it.",
    "TRG-001": "Prefer pull_request; if pull_request_target is needed, never check out or run PR code in it.",
    "TRG-002": "Treat comment text as untrusted; gate on author_association and pass via env vars.",
    "CHK-001": "Do not check out PR head code in a privileged workflow; split into unprivileged build + privileged report.",
    "INJ-001": "Pass the value through an env: variable and quote it (\"$TITLE\") instead of ${{ }} in run:.",
    "PRM-001": "Add top-level 'permissions: contents: read' and grant more per job.",
    "PRM-002": "Replace write-all with the minimum scopes per job.",
    "SEC-001": "Pass only the named secrets the called workflow needs.",
    "RUN-001": "Use GitHub-hosted or ephemeral, isolated runners for untrusted triggers.",
    "CRD-001": "Set persist-credentials: false so the token is not left in .git/config.",
}


def find_workflows(path):
    if os.path.isfile(path):
        return [path]
    wf_dir = os.path.join(path, ".github", "workflows")
    if not os.path.isdir(wf_dir):
        wf_dir = path
    files = []
    for name in sorted(os.listdir(wf_dir)):
        if name.endswith((".yml", ".yaml")):
            files.append(os.path.join(wf_dir, name))
    return files


def audit_file(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    findings = []

    def add(rule, lineno, detail):
        findings.append({"file": path, "line": lineno, "rule": rule,
                         "severity": SEVERITY[rule], "detail": detail,
                         "advice": ADVICE[rule]})

    text = "\n".join(lines)
    has_top_perms = any(re.match(r"^permissions:", l) for l in lines)
    untrusted_trigger = False
    in_run_block = False
    run_indent = 0
    checkout_blocks = []  # (lineno, indent)

    for i, raw in enumerate(lines, start=1):
        line = raw.split(" #")[0] if " #" in raw else raw
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())
        if stripped.startswith("#") or not stripped:
            continue

        # Triggers (both map and list/inline forms)
        for trig in ("pull_request_target", "workflow_run"):
            if re.search(r"(^|[\s\[,])" + trig + r"\s*(:|,|\]|$)", stripped):
                untrusted_trigger = True
                add("TRG-001", i, trig + " trigger")
        for trig in ("issue_comment", "pull_request_review_comment"):
            if re.search(r"(^|[\s\[,])" + trig + r"\s*(:|,|\]|$)", stripped):
                untrusted_trigger = True
                add("TRG-002", i, trig + " trigger")

        if re.match(r"^permissions:\s*write-all", stripped) or re.match(r"^permissions:\s*write-all", line):
            add("PRM-002", i, "permissions: write-all")

        m = USES_RE.match(line)
        if m:
            ref = m.group(1)
            if not (ref.startswith("./") or ref.startswith("docker://")):
                target, _, version = ref.partition("@")
                if not SHA_RE.match(version or ""):
                    add("PIN-001", i, "%s pinned to '%s'" % (target, version or "(none)"))
                if target == "actions/checkout":
                    checkout_blocks.append((i, indent))
            elif ref.startswith("docker://") and "@sha256:" not in ref:
                add("PIN-001", i, "%s not pinned to an image digest" % ref)

        if re.match(r"^secrets:\s*inherit", stripped):
            add("SEC-001", i, "secrets: inherit")

        if HEAD_REF_RE.search(line):
            add("CHK-001", i, "checks out pull request head code")

        if re.match(r"^runs-on:.*self-hosted", stripped):
            runs_self_hosted_line = i
            if untrusted_trigger:
                add("RUN-001", runs_self_hosted_line, "self-hosted runner with untrusted trigger")

        # run: blocks (single line or block scalar)
        rm = re.match(r"^-?\s*run:\s*(.*)$", stripped)
        if rm:
            in_run_block = rm.group(1).strip() in ("|", ">", "|-", ">-", "|+", ">+")
            run_indent = indent
            if UNTRUSTED_EXPR.search(rm.group(1)):
                add("INJ-001", i, UNTRUSTED_EXPR.search(rm.group(1)).group(0) + " }} in run:")
            continue
        if in_run_block:
            if indent > run_indent:
                if UNTRUSTED_EXPR.search(line):
                    add("INJ-001", i, UNTRUSTED_EXPR.search(line).group(0) + " }} in run:")
            else:
                in_run_block = False

    if not has_top_perms:
        add("PRM-001", 1, "no top-level permissions block")

    # persist-credentials check: look in the lines following each checkout step
    for lineno, ind in checkout_blocks:
        window = lines[lineno: lineno + 8]
        block = []
        for l in window:
            if l.strip().startswith("- ") and (len(l) - len(l.lstrip())) <= ind:
                break
            block.append(l)
        if not any(re.search(r"persist-credentials:\s*false", l) for l in block):
            add("CRD-001", lineno, "actions/checkout keeps the token in .git/config")

    # Reorder: escalate TRG-001 note if combined with head checkout
    if untrusted_trigger and any(f["rule"] == "CHK-001" for f in findings):
        for f in findings:
            if f["rule"] == "CHK-001":
                f["detail"] += " in a privileged trigger (pwn request)"
    return findings


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    as_json = "--json" in argv
    target = [a for a in argv[1:] if a != "--json"][0]
    files = find_workflows(target)
    findings = []
    for f in files:
        findings.extend(audit_file(f))
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    findings.sort(key=lambda f: (order[f["severity"]], f["file"], f["line"]))
    if as_json:
        print(json.dumps(findings, indent=2))
    else:
        print("Scanned %d workflow file(s); %d finding(s)\n" % (len(files), len(findings)))
        for f in findings:
            print("%-6s %s %s:%d  %s" % (f["severity"], f["rule"],
                                         os.path.relpath(f["file"], target), f["line"], f["detail"]))
            print("       fix: %s" % f["advice"])
        counts = {s: sum(1 for f in findings if f["severity"] == s) for s in order}
        print("\nSummary: HIGH %(HIGH)d, MEDIUM %(MEDIUM)d, LOW %(LOW)d" % counts)
    return 1 if any(f["severity"] == "HIGH" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
