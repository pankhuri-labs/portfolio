# From finding to fix: triage, routing and remediation

**Role:** AGM and Technology Product Manager, Application Security and Vulnerability Management (Dec 2024 to Sep 2026) · **Organisation:** John Deere

A scanner is only useful if the right finding reaches the right owner, in time, with a reason to act. I owned the rules and workflow that decided what analysts and developers saw first, and the SLA they were held to.

## Risk-weighted routing

- Specified the remediation workflow in the IT service management platform: extra weighted risk parameters (such as exposure, source severity and exploitability) set a business-relevant severity, route each finding to its owner group and escalate the most severe findings.
- Prioritised on CVSS, EPSS, CISA KEV and asset criticality, so teams worked on what attackers actually use.

## SLAs and exceptions

- Owned and enforced the severity-based SLA policy for application security and vulnerability findings.
- Made the exception process much faster, so teams asked for time instead of going quiet.
- Traced missed SLAs to findings that were discovered late, and directed the risk-rating review that fixed them.

## Cutting noise so developers trust the findings

- Enabled the extended security query suite, added a custom code-scanning query that flags unpinned CI/CD action references, and added custom secret-scanning patterns.
- Auto-closed alerts from test code and already-remediated findings.
- Worked with developers to harden the CI/CD path: branch protection rules, and access and permissions limited to specific directory groups.

## Open-source risk

- Product owner for the SCA tool: reachability analysis to focus on exploitable components, and auto-remediation pull requests to make the fix the easy path.

## AI-assisted remediation

- Shaped the success criteria and guardrails for an AI remediation programme led by my engineering manager: LLM agents raise fix pull requests with confidence scores, and a human always reviews them.
- Helped define the accuracy metric and confidence thresholds, and reviewed the prompts. Most AI-raised fix pull requests were accepted.

## Vulnerability management

- Product owner for the enterprise vulnerability management platform, with near-complete asset coverage across a large estate.
- Led the endpoint platform's vulnerability management from a pilot to the wider estate, comparing findings with the incumbent on real data and reconciling the CMDB to close coverage gaps.

## Feedback loops

- Support-queue issues fed straight into the backlog. Security champions, the AppSec and VM knowledge base on the developer portal, and remediation guides kept developers moving.
- I supplied requirements and data from all five platforms to a single prioritised findings view, owned by a peer product manager.

## What I'd tell another security leader

Measure fixed within SLA, not findings raised. If the number is not moving, look at routing, ownership and noise before you buy another scanner.

[← Back to portfolio](../README.md)
