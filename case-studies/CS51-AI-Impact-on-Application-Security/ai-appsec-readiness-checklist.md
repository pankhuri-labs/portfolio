# AI and AppSec Readiness Checklists

Companion to [CS51](README.md). Two short checklists: one for **product organisations** using AI in software development, one for **services organisations** delivering or testing client software with AI and building AI security services. Score each line 0 (not in place), 1 (partly in place) or 2 (in place and evidenced). Review quarterly; the field changes monthly.

## Checklist 1: guardrails for AI-assisted development (product organisations)

| # | Area | Control | Evidence to look for | Score (0-2) |
|---|---|---|---|---|
| 1 | Policy | AI-assisted development policy approved, mapped to NIST SSDF and CISA Secure by Design | Policy document; mapping table | |
| 2 | Inventory | All AI coding assistants, agents, IDE extensions and MCP servers in use are listed with owner and settings | Inventory export | |
| 3 | Inventory | AI components in products (agent frameworks, model servers, vector databases) are in the asset inventory and AI-BOM | AI-BOM; VM scan coverage | |
| 4 | Gates | AI-assisted changes pass the same SAST, SCA, secrets scanning and tests as any change | Pipeline configuration | |
| 5 | Gates | Rules tuned for classes AI handles worst (cross-site scripting, log injection, authorisation) | Rule set changes and precision data | |
| 6 | Provenance | AI-assisted changes are labelled (tool telemetry or commit trailer) | Sample of commits | |
| 7 | Dependencies | Package installs go through a registry proxy with allow-list or age and reputation checks | Proxy logs; blocked installs | |
| 8 | Dependencies | First-seen dependencies flagged in pull requests | Pull request bot output | |
| 9 | Agents | Each coding agent has its own scoped, short-lived identity | Identity provider records | |
| 10 | Agents | Human approval required for pushes to protected branches, pipeline changes and production access | Branch protection and agent settings | |
| 11 | Agents | Agent execution sandboxed; auto-execute modes off on sensitive repositories | Configuration review | |
| 12 | Agents | Agent actions logged to the SIEM with alerting on unusual behaviour | SIEM queries | |
| 13 | Injection | Agents that read untrusted content cannot act with write or network access without approval | Design review records | |
| 14 | Review | Pull request size limits; humans review security-relevant paths | Repository rules | |
| 15 | Prioritisation | Exploitation-based SLAs (KEV, EPSS, threat intelligence) including AI components | SLA policy; remediation metrics | |
| 16 | AI defence tools | AI triage and autofix benchmarked on own code; precision, recall and rescan-pass rate tracked | Pilot report | |
| 17 | PSIRT | Proof of concept required for inbound reports; capacity planned for batch disclosures and CRA clocks | Disclosure policy; staffing plan | |
| 18 | Metrics | Escaped-defect rate of AI-assisted changes reported separately | Dashboard | |

**Reading the score (max 36):** 0-12 AI is adopted without guardrails; 13-24 guardrails exist but agents and dependencies are weak spots; 25-36 AI-assisted development is governed and evidenced.

## Checklist 2: AI in delivery and AI security service readiness (services organisations)

| # | Area | Control | Evidence to look for | Score (0-2) |
|---|---|---|---|---|
| 1 | Contracts | AI-in-delivery schedule in new and renewed client contracts (tools, data terms, disclosure, accountability, evidence) | Contract template; share of contracts | |
| 2 | Policy in tools | Per-client AI policy enforced in tooling (managed licences, workspace settings, policy-as-code) | Tool admin consoles | |
| 3 | Accounts | No personal AI accounts used on client code or data | Device and network controls | |
| 4 | Separation | Separate workspaces or virtual desktops and per-client credentials for engineers on several clients | Access design | |
| 5 | Extensions and MCP | Approved catalogue of IDE extensions and MCP servers; others blocked | Catalogue; endpoint policy | |
| 6 | Register | Per-client AI use register (tools, settings, scope) maintained | Register sample | |
| 7 | Quality | Provider-side security gates on every delivery, independent of client gates | Delivery checklist; pipeline | |
| 8 | Quality | AI-assisted share and security defect rate reported to clients | Client reports | |
| 9 | Incident | Client notification process for AI tool or agent compromise | Runbook | |
| 10 | Services | AI and agent security testing methodology mapped to OWASP LLM and Agentic Top 10 and NIST AI RMF | Methodology document | |
| 11 | Services | Human validation of AI findings is a named step in testing and managed services | Service description | |
| 12 | Services | At least one outcome-priced managed AppSec or VM offer | Service catalogue | |
| 13 | Skills | Practitioners trained in AI red teaming and agent security per delivery unit | Training records | |
| 14 | Talent | Junior roles redesigned around validating and supervising AI output | Role descriptions; career paths | |
| 15 | Evidence | Per-client evidence pack aligned to the client's framework (DORA, RBI, SEBI, CRA) | Sample evidence pack | |

**Reading the score (max 30):** 0-10 AI use in delivery is ungoverned and services are not ready; 11-20 controls exist for some clients and services are in pilot; 21-30 AI is governed per client and AI security services are productised.
