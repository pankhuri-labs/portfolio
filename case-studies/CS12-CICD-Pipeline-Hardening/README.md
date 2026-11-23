# CS12: CI/CD Pipeline Hardening

Domain: SaaS, technology and software vendors; open-source maintainers · Org type: product

## 1. Problem statement

Build pipelines are now the most privileged and least governed systems in a software company. A typical GitHub Actions workflow pulls third-party actions by a mutable tag such as `@v4`, runs with a token that can write to the repository, has access to long-lived cloud keys and package-registry tokens stored as repository secrets, executes on shared or self-hosted runners with open egress, and may be triggered by anyone who can open a pull request or post a comment. A single compromised action, a malicious dependency install script, or a pull-request title that is interpolated into a shell command is enough to read every secret available to the job and publish them, push code, or ship a trojanised release to customers. CS03 covers SBOM, provenance and CRA obligations for what you ship; this case study covers the pipeline itself: how workflows are written, what they trust, and what credentials they can reach.

## 2. Why now

| Incident or driver | What happened | Lesson |
|---|---|---|
| **Ultralytics (PyPI, Dec 2024)** | Attackers abused a `pull_request_target` workflow with a script injection through a branch name, plus GitHub Actions cache poisoning, so that the project's own release pipeline published versions 8.3.41 and 8.3.42 containing a cryptominer | A privileged trigger plus untrusted input can make your legitimate pipeline publish malware |
| **reviewdog and tj-actions/changed-files (Mar 2025)** | `reviewdog/action-setup` was compromised (CVE-2025-30154); a token obtained through that chain was used to repoint all tags of `tj-actions/changed-files` (CVE-2025-30066, used by more than 23,000 repositories) to a commit that dumped runner memory, printing secrets into build logs; Unit 42 traced the initial target to Coinbase | Tags are mutable; one compromised action cascades into others; public logs are an exfiltration channel |
| **Nx "s1ngularity" (26 Aug 2025)** | A `pull_request_target` workflow echoed an unsanitised PR title; the injected command took a write-capable `GITHUB_TOKEN`, triggered the publish workflow and stole the npm token; malicious Nx versions were live for about four hours and used local AI coding CLIs to hunt for secrets | Default write tokens and `workflow_dispatch` on publish workflows turn a lint job into a release compromise |
| **Shai-Hulud npm worm (Sep 2025) and Shai-Hulud 2.0 (Nov 2025)** | Stolen maintainer tokens were used to publish trojanised packages that harvested secrets and republished other packages the victim maintained; the November wave ran in `preinstall`, affected several hundred packages and exposed secrets from tens of thousands of repositories, with a destructive fallback | Install scripts run in CI with CI's credentials; long-lived publish tokens are the worm's fuel |

Platforms have changed defaults in response. GitHub added organisation policies to block specific actions and enforce SHA pinning (August 2025); from 8 December 2025 `pull_request_target` always runs the workflow file from the default branch; from mid-2026 `actions/checkout` refuses to check out fork pull-request code in `pull_request_target` and `workflow_run` workflows unless explicitly overridden. npm is moving to short-lived granular tokens, FIDO-based 2FA and trusted publishing (GitHub, 22 September 2025). On the regulatory side, the EU Cyber Resilience Act requires manufacturers to report actively exploited vulnerabilities from 11 September 2026 and to handle vulnerabilities in their build components, and US secure software development attestations reference NIST SP 800-218 (SSDF), which includes protecting the build environment.

## 3. Pain points addressed

| Product organisations | Services organisations |
|---|---|
| PP-P-04 CI/CD is a soft target: third-party actions, long-lived secrets, unpinned dependencies | PP-S-10 developers delivering client code without a consistent secure SDLC (pipelines built for clients inherit the same risks) |
| PP-P-05 secrets in CI logs and runner environments | PP-S-07 clients request supply-chain evidence |
| PP-P-08 CRA and secure software attestation obligations | |
| PP-P-15 many deploys per day, so controls must be automated in the pipeline | |

## 4. Root causes

1. **Mutable references.** Actions, reusable workflows and container images are referenced by tag or branch, so the code that runs can change without any change in your repository.
2. **Privileged triggers on untrusted input.** `pull_request_target`, `workflow_run` and `issue_comment` run with secrets and a write token while processing data an outsider controls (PR titles, branch names, comment bodies, fork code).
3. **Over-scoped, long-lived credentials.** Repository default token permissions are read/write; cloud keys and registry tokens are static secrets visible to every job.
4. **Install-time code execution.** `npm install`, `pip install` and build plugins run arbitrary scripts inside the job that holds the secrets.
5. **Runners are trusted and unmonitored.** Persistent self-hosted runners are reused across jobs and repositories, with open egress and no record of what each job contacted.
6. **Nobody owns workflow code.** Workflow YAML is not reviewed by security, not covered by CODEOWNERS, and not scanned.

## 5. Solution

### 5.1 Governance of workflow code

- Add `.github/workflows/` and `.github/actions/` to CODEOWNERS with a platform or security reviewer; protect them with rulesets.
- Organisation policy: allow only GitHub-authored, verified-creator and an internal allow-list of actions; turn on **SHA pinning enforcement**; block known-compromised actions.
- Run a workflow linter on every pull request. The [workflow audit script](workflow-audit/workflow_audit.py) in this folder is a dependency-free starting point (see 5.6); zizmor and actionlint are fuller options.

### 5.2 Triggers and untrusted input

| Pattern | Rule |
|---|---|
| `pull_request_target`, `workflow_run` | Avoid. If required (for labelling or commenting on fork PRs), never check out or execute PR code and never expose secrets other than a minimal token |
| Fork PR builds | Use `pull_request` (no secrets, read-only token); require approval for first-time and outside contributors |
| Expressions in `run:` | Never interpolate `${{ github.event.* }}` text fields into shell; pass through `env:` and quote |
| `workflow_dispatch` on publish workflows | Restrict with environments that require reviewers and a protected branch or tag |
| Caches | Do not restore caches written by untrusted workflows into release jobs; scope cache keys per branch |

### 5.3 Credentials: least privilege and short life

- `permissions: contents: read` at workflow top level; grant `id-token: write`, `packages: write` or `contents: write` only to the job that needs it. Set the organisation default token to read-only.
- **OIDC federation** to AWS, Azure and Google Cloud with trust policies bound to repository, branch or environment (`sub` claim), replacing static cloud keys.
- **Trusted publishing** to npm and PyPI (OIDC) instead of long-lived publish tokens; FIDO2 for maintainer accounts.
- Deployment secrets live in **environments** with required reviewers and branch restrictions, not repository-wide secrets.
- `persist-credentials: false` on checkout; mask and never echo secrets; enable secret scanning and push protection on logs and code (CS14).

### 5.4 Dependencies and runners

- `npm ci --ignore-scripts` (allow-list the few packages that need scripts), lockfiles enforced, a package proxy with a minimum release age (for example 3-7 days) for new versions.
- GitHub-hosted or **ephemeral, single-use** self-hosted runners (one job per VM or pod); never self-hosted runners on public repositories.
- Egress allow-listing and process monitoring on runners (for example Harden-Runner) so a step that contacts an unknown host or reads runner memory is blocked or alerted.

### 5.5 Build integrity (SLSA Build track)

| Level | What it means | How |
|---|---|---|
| Build L1 | Provenance exists | Generate provenance for every release artifact |
| Build L2 | Signed provenance from a hosted build platform | GitHub artifact attestations or Sigstore signing in CI |
| Build L3 | Hardened, isolated builds; signing keys not reachable by build steps | Reusable, isolated release workflow; ephemeral runners; verify attestations at deploy |

Release and deployment admission should verify provenance (`gh attestation verify`, policy controllers in Kubernetes). SBOM and CRA reporting are in CS03.

### 5.6 Supporting artifact: workflow audit script

[`workflow-audit/workflow_audit.py`](workflow-audit/workflow_audit.py) scans `.github/workflows` for unpinned actions and reusable workflows, privileged triggers, PR-head checkouts, untrusted expressions in `run:`, missing or `write-all` permissions, `secrets: inherit`, self-hosted runners on untrusted triggers and checkouts that persist credentials. It exits non-zero on HIGH findings so it can gate CI. Run `python3 workflow-audit/workflow_audit.py workflow-audit/sample` to see it flag the deliberately insecure `pr-checks.yml` and pass the hardened `release.yml`.

### 5.7 Product organisation variant

Priority order: release and deploy pipelines (they hold publish and production credentials), then public repositories, then internal ones. Authors of actions should publish immutable, signed releases and document the permissions each needs.

### 5.8 Services organisation variant

IT services firms that build and run pipelines for clients should ship a hardened pipeline template per platform (GitHub Actions, GitLab CI, Azure DevOps), use client-owned OIDC trust and secrets rather than delivery-team keys, run the same linter on client repositories, and hand over pipeline ownership and credentials at contract end.

## 6. 90-day plan

| Days | Deliverable |
|---|---|
| 0-30 | Inventory of workflows, third-party actions and secrets; organisation default token set to read-only; CODEOWNERS on workflow paths; workflow audit in CI (report-only); all `pull_request_target` uses reviewed |
| 30-60 | All third-party actions SHA-pinned with Dependabot/Renovate; SHA-pinning policy enforced; OIDC replaces static cloud keys for release and deploy; trusted publishing for npm/PyPI; `--ignore-scripts` and package cooldown in release jobs |
| 60-90 | Ephemeral runners and egress monitoring for release pipelines; artifact attestations at SLSA Build L2 (L3 for flagship products); audit becomes blocking; tabletop: "a pinned action we use is compromised" |

## 7. KPIs

| KPI | Target |
|---|---|
| Third-party action references pinned to a commit SHA | 100% |
| Workflows with explicit least-privilege `permissions:` | ≥ 95% |
| Long-lived cloud keys stored as CI secrets | 0 for release and deploy pipelines |
| Packages published via trusted publishing (OIDC) | 100% |
| `pull_request_target` workflows that check out PR code | 0 |
| Release artifacts with verified signed provenance | 100% |
| Time to rotate all CI secrets after an action compromise | ≤ 4 hours |

## 8. Tooling options

- **Open source / free:** zizmor and actionlint (workflow linting), OpenSSF Scorecard (pinning and token-permission checks), Dependabot and Renovate (SHA updates), Gitleaks and TruffleHog (secrets in logs and code), Sigstore/cosign and GitHub artifact attestations (provenance), SLSA GitHub generator, StepSecurity Harden-Runner community tier (egress), OPA/Kyverno for deploy-time verification.
- **Commercial categories:** CI/CD security posture management, software supply-chain security platforms, package firewalls with malicious-package intelligence, runner egress and runtime protection, ASPM with pipeline inventory.

## 9. Risks and how to handle them

| Risk | Mitigation |
|---|---|
| SHA pinning freezes vulnerable versions | Automated update PRs with changelog review; Scorecard and advisory alerts on pinned actions |
| Pinning to a SHA from a malicious fork network | Verify the SHA belongs to the upstream repository's history; prefer pinning to signed release commits |
| `--ignore-scripts` breaks native builds | Allow-list packages that need scripts; build them in an isolated job without secrets |
| Linter noise leads to ignored findings | Start with HIGH rules only; make rules blocking per repository once clean |

## 10. Learnings

1. Treat workflow YAML as production code with owners, review and scanning.
2. Mutable tags are the main reason tj-actions reached so many repositories; SHA pinning plus enforcement is cheap.
3. Privileged triggers on untrusted input (Ultralytics, Nx) are the most common route from a pull request to a release compromise.
4. Short-lived OIDC credentials and trusted publishing remove the tokens that worms like Shai-Hulud depend on.
5. Provenance verification at deploy time turns pipeline hardening into something you can prove to customers and regulators.

## References

- CISA, "Supply Chain Compromise of Third-Party tj-actions/changed-files (CVE-2025-30066) and reviewdog/action-setup (CVE-2025-30154)" (March 2025): https://www.cisa.gov/news-events/alerts
- Nx, "s1ngularity postmortem" (2025): https://nx.dev/blog/s1ngularity-postmortem
- GitHub, "Our plan for a more secure npm supply chain" (22 September 2025): https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/
- GitHub changelog, "Actions pull_request_target and environment branch protections changes" (7 November 2025): https://github.blog/changelog/2025-11-07-actions-pull_request_target-and-environment-branch-protections-changes/
- GitHub changelog, "GitHub Actions policy now supports blocking and SHA pinning actions" (15 August 2025): https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/
- OWASP Top 10 CI/CD Security Risks: https://owasp.org/www-project-top-10-ci-cd-security-risks/
- NIST SP 800-204D, Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines (2024): https://csrc.nist.gov/pubs/sp/800/204/d/final
- SLSA specification: https://slsa.dev/
