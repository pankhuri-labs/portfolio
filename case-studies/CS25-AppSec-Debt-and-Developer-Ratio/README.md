# CS25: Application Security Debt and the Developer Ratio

Domain: SaaS, BFSI, IT services delivering code · Org type: product, with a services variant for IT services firms

## 1. Problem statement

Most software organisations have one application security engineer for every hundred or more developers. That team cannot review every design, triage every scanner finding or answer every question, so one of two things happens: security becomes a queue that delays releases, or it is bypassed and changes ship unreviewed. Meanwhile SAST, SCA, container and IaC scanners generate tens of thousands of findings with no owner and no sense of which matter, the backlog grows each sprint, and developers learn to ignore security tickets. AI coding assistants raise output further, adding code faster than any review process designed for human pace. The debt compounds: the same classes of vulnerability (injection, broken access control, secrets in code) are re-introduced because nothing in the development path makes the secure option the easy one.

## 2. Why now

| Incident or driver | What happened | Lesson |
|---|---|---|
| **CISA Secure by Design pledge (May 2024)** | Software manufacturers pledged measurable progress on seven goals within a year, including MFA, removing default passwords, reducing entire classes of vulnerability, publishing CVEs with CWE data and having a vulnerability disclosure policy | Buyers and governments now ask for evidence that whole bug classes are being removed, not that findings are being closed |
| **Google, memory safety in Android (Sept 2024)** | Google reported that the memory-safety share of Android vulnerabilities fell from 76% in 2019 to 24% in 2024, mainly by writing new code in memory-safe languages rather than rewriting old code | Secure defaults for new code reduce debt faster than remediation of old code |
| **AI-generated code (Veracode, July 2025)** | Testing of code produced by many large language models found security flaws in around 45% of the tasks tested, with little improvement in newer or larger models | AI raises output; without guardrails it raises the defect rate too |
| **EU Cyber Resilience Act (vulnerability reporting from 11 Sept 2026)** | Manufacturers of products with digital elements must report actively exploited vulnerabilities within 24 hours and meet essential cybersecurity requirements by December 2027 | Security debt in shipped products becomes a regulatory liability |

US federal buyers require a secure software development attestation aligned with NIST SP 800-218 (SSDF), and enterprise customers ask for SAMM or BSIMM-style maturity evidence in questionnaires. The supply of AppSec engineers will not grow to match developer headcount, so the model has to change.

## 3. Pain points addressed

| Product organisations | Services organisations |
|---|---|
| PP-P-06 AppSec to developer ratio of roughly 1:100 or worse; reviews become a bottleneck or are skipped | PP-S-10 developers deliver client code without consistent secure SDLC; client blames vendor for findings |
| PP-P-15 many deploys per day make gate-based reviews impossible | PP-S-05 skills shortage; junior staff triage findings without context |
| PP-P-01 scanner noise: thousands of findings, most not exploitable | PP-S-06 AI-assisted delivery with different data rules per client |
| PP-P-07 AI features and AI-generated code without threat models | |

## 4. Root causes

1. **Security as a gate, not a platform.** The AppSec team reviews outputs instead of building components and defaults that prevent bugs.
2. **Every finding treated equally.** Without reachability, exposure and asset context, teams cannot tell the few findings that matter from the many that do not ([CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md)).
3. **Reviews are not risk-tiered.** A copy change and a new payment flow get the same process, or the same lack of one.
4. **No ownership.** Findings land in a central tool, not in the owning team's backlog with an SLA.
5. **Bug classes are fixed one instance at a time.** Each SQL injection is patched; the query API that allowed it is left in place.
6. **No measurement of capability.** Teams cannot show whether practices improve, so investment follows the latest incident.

## 5. Solution

### 5.1 Paved roads and secure defaults

| Bug class | Paved-road control |
|---|---|
| Injection | Parameterised query layer or ORM only; lint rule blocking string-built SQL |
| Cross-site scripting | Framework auto-escaping; Trusted Types and strict CSP in the web template |
| Broken access control | Central authorisation guard and tenant-scoped data access in the service template (CS23) |
| Secrets in code | Secret manager client in templates; pre-commit and server-side secret scanning with push protection |
| Insecure dependencies | Curated base images and dependency allow-lists; automated update pull requests |
| Cloud misconfiguration | Approved IaC modules with secure defaults (CS22) |
| Memory safety | New components in memory-safe languages where practical |

Measure adoption: the share of services built from the template is the leading indicator of future debt.

### 5.2 Risk-based design review triage

- A short intake form (ten questions) on every epic or design document: new internet exposure, authentication or authorisation change, handling of payment, health or personal data, new third party or integration, cryptography, AI/LLM component, multi-tenant data path, privileged operation, regulatory scope.
- Score routes the work: **Tier 0** (no triggers) self-service checklist; **Tier 1** (one or two triggers) security champion review using a threat-model template; **Tier 2** (high-risk triggers such as payments, authentication or AI agents with tool access) AppSec engineer review.
- Target: AppSec engineers spend their review time on the Tier 2 work, typically a small fraction of all changes.

### 5.3 Security champions

- One champion per team (roughly 1 per 8-10 developers), with about 10-20% of their time allocated, a defined role (Tier 1 reviews, first-line triage, paved-road feedback), training and a career benefit recognised in performance reviews.
- Monthly champion forum run by AppSec; champions get early access to new templates and tooling.

### 5.4 Triage at scale with ASPM

- Aggregate SAST, SCA, secrets, container, IaC and DAST findings into an application security posture management (ASPM) layer that deduplicates and maps each finding to a service, owner and runtime context.
- Prioritise by reachability, internet exposure, data sensitivity and exploit signals (KEV, EPSS); suppress unreachable dependency findings with a VEX-style justification.
- Route to the owning team's backlog with SLAs by priority, not severity alone; report debt per team.

### 5.5 AI-assisted remediation, with guardrails

- Use AI autofix for well-understood finding types (dependency upgrades, injection with parameterisation, missing output encoding) as pull requests that go through normal review and tests.
- Risks to manage: incorrect or partial fixes that silence the scanner without removing the flaw; new vulnerabilities in generated code; hallucinated package names that attackers register (slopsquatting); leakage of proprietary code to external models.
- Controls: rescan after every AI fix; require tests demonstrating the fix; approved models and data-handling settings only; dependency allow-lists; track the defect rate of AI-generated changes separately.

### 5.6 Measure maturity

- Run an OWASP SAMM assessment (15 practices across governance, design, implementation, verification and operations) as a baseline and every six months; set target levels per practice.
- Use BSIMM activity descriptions to compare with peers and choose next investments.
- Track the CISA pledge goals publicly if you are a software manufacturer, especially reduction of whole vulnerability classes.

### 5.7 Product organisation variant

- AppSec reorganises as a platform team: roughly half its capacity goes to paved roads and tooling, the rest to Tier 2 reviews and incident support.
- Security requirements for each product line are expressed as automated checks in CI, so fast release cadence is preserved.

### 5.8 Services organisation variant (IT services delivering code)

- Agree a secure SDLC baseline per client (SAMM target levels, scanner set, SLAs) in the statement of work, so responsibility for findings is clear.
- Maintain reusable secure starter kits per technology stack across delivery units.
- Train and certify a champion per delivery team; run AI coding assistants only under each client's data-handling rules.
- Hand over scan results, threat models and residual-risk lists at each release.

## 6. 90-day plan

| Days | Deliverable |
|---|---|
| 0-30 | SAMM baseline; findings aggregated with owners for the top 20 services; design intake form live; champion role defined and first cohort named |
| 30-60 | Reachability and exposure prioritisation in place; SLAs by priority; service template with authorisation, secrets and query layer; Tier 1 reviews run by champions |
| 60-90 | AI autofix pilot on two finding types with rescan and test controls; paved-road adoption measured; debt and SAMM targets reported to leadership |

## 7. KPIs

| KPI | Target |
|---|---|
| Services built from the secure template | ≥ 60% in 12 months |
| Teams with a trained security champion | ≥ 90% |
| Tier 2 designs reviewed by AppSec before build | 100% |
| Reachable high-priority findings past SLA | Falling to ≤ 5% |
| Recurrence of the top three vulnerability classes | Down 50% year on year |
| AI-generated fixes merged that later fail rescan or tests | ≤ 5% |
| SAMM score in target practices | +0.5 per practice per year |

## 8. Tooling options

- **Open source / free:** OWASP SAMM toolbox, OWASP ASVS, Semgrep community rules, CodeQL (free for open source), OWASP Dependency-Check and Dependency-Track, Gitleaks and TruffleHog, DefectDojo (aggregation), OWASP Threat Dragon, BSIMM reports.
- **Commercial categories:** ASPM platforms, SAST/SCA suites with reachability, AI-assisted remediation tools, developer security training platforms, internal developer portals with scorecards.

## 9. Risks and how to handle them

| Risk | Mitigation |
|---|---|
| Champions lack time and drift away | Allocated time in sprint planning; recognition in performance reviews; rotate every 18-24 months |
| Paved roads are seen as restrictive | Build with developers; make the template the fastest way to ship; allow documented deviations |
| ASPM becomes another dashboard nobody reads | Route findings into team backlogs; review debt in engineering leadership meetings |
| AI fixes introduce new flaws | Rescan, tests and human review for every AI pull request; measure and stop if quality drops |
| Triage tiers are gamed to avoid review | Spot-check Tier 0 and Tier 1 decisions; incidents trigger reclassification |

## 10. Learnings

1. The ratio cannot be fixed by hiring; the AppSec team has to multiply itself through platforms and champions.
2. Removing a vulnerability class with a secure default is worth more than fixing many instances.
3. Risk-tiered design review puts scarce experts on the few changes that matter.
4. AI remediation is useful for routine fixes, but only with rescans, tests and review.
5. Measure capability (SAMM, adoption, recurrence), not only finding counts.

## References

- CISA, Secure by Design pledge: https://www.cisa.gov/securebydesign/pledge
- OWASP SAMM: https://owaspsamm.org/
- BSIMM (Building Security In Maturity Model): https://www.bsimm.com/
- NIST SP 800-218, Secure Software Development Framework: https://csrc.nist.gov/pubs/sp/800/218/final
- Google Security Blog, "Eliminating Memory Safety Vulnerabilities at the Source" (Sept 2024): https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html
- Veracode, "AI-Generated Code Poses Major Security Risks in Nearly Half of All Development Tasks" (July 2025): https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
- EU Cyber Resilience Act, Regulation (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
