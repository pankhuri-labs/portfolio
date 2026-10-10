# CS35: Scaling GitHub Advanced Security Across a Large Enterprise

**Domain: Large enterprises with in-house engineering, including regulated financial-domain applications; IT services firms running AppSec platforms for clients** · Org type: both

> **In short**
> - **The problem:** adding GitHub Advanced Security to a mature AppSec programme without coverage gaps, duplicate alerts or developer fatigue.
> - **The approach:** treat the security platform as an internal product: evaluation criteria, a time-boxed pilot, a Go / No-Go decision, rollout in batches, champions and KPIs.
> - **The result:** an enterprise-wide rollout whose method became the template for later security tool rollouts.
> - **For your team:** this is what my **security tool evaluation** and **rollout playbook** offers deliver.

> **First-hand experience.** This case study is drawn from my own work as the Product Manager who led the evaluation, productisation, rollout and scaling of GitHub Advanced Security (GHAS) in a large global enterprise. The organisation, internal tools, repositories, teams, people, volumes, thresholds and performance results are deliberately left out. Public product facts are kept and cited.

## 1. Problem statement

The organisation already had a mature application security programme: an incumbent commercial SAST tool and an internally developed secret-scanning solution. The question was not "should we turn on a scanner?" but how GHAS could strengthen and modernise that ecosystem without reducing coverage, disrupting developer workflows, creating duplicate findings or adding operational burden. The estate was mixed: modern cloud-native services and complex legacy applications; repositories on both GitHub Enterprise and GitHub Cloud; languages that CodeQL supports, partly supports and does not support; standard and heavily customised CI/CD pipelines; and financial-domain applications that need control coverage, traceability, access governance, audit evidence and exception management. Administration of the existing secret scanner was spread across many people with no clear owner. Many product families, platform, security, governance and operations teams all had a stake. A tool switch done as a big-bang deployment would have created coverage gaps, alert noise and migration fatigue; done manually repository by repository, it would never have finished.

## 2. Why now

| Driver | What happened | Lesson |
|---|---|---|
| **GHAS unbundled (April 2025)** | GitHub split GHAS into two products, GitHub Secret Protection and GitHub Code Security, sold per active committer and opened to GitHub Team plans | Enterprises can now adopt secret protection and code scanning separately, so the "overlap with what we already have" question is asked per capability |
| **Copilot Autofix for code scanning (GA August 2024)** | AI-generated fix suggestions for CodeQL alerts became generally available to GHAS customers | Remediation speed becomes a selling point, but suggestions still need developer review, tests and change control |
| **Scale enablement features** | Default setup for code scanning (no workflow file) and organisation-level security configurations let admins enable scanning across many repositories at once | Zero-touch onboarding is technically possible; the hard part is deciding which repositories are eligible and what happens to the rest |
| **Secrets leaking at scale** | GitGuardian counted about 23.8 million new hard-coded secrets on public GitHub in 2024 (State of Secrets Sprawl 2025) | Push protection and secret scanning in the developer path are now baseline expectations (see CS14) |
| **Secure development attestation** | NIST SP 800-218 (SSDF), CISA Secure by Design and financial-sector supervisors ask for evidence that code is scanned and findings are fixed within agreed timelines | Coverage, SLA and closure evidence must be designed in, not assembled for an audit |

CodeQL supports a defined list of languages (for example Java and Kotlin, C#, C and C++, Go, JavaScript and TypeScript, Python, Ruby and Swift). Anything outside that list, such as PHP or many legacy and platform-specific languages, gets no CodeQL analysis, so "GHAS enabled" is not the same as "SAST covered".

## 3. Pain points addressed

| Product organisations | Services organisations |
|---|---|
| PP-P-35 consolidating or replacing SAST and secret scanning across a large, mixed estate: overlapping tools, duplicate findings, unsupported languages, custom pipelines, manual migration | PP-S-30 AppSec platform rollouts and tool migrations for clients run as one-off manual projects with different scanners, languages and admin models per client |
| PP-P-01 scanner noise: developers stop trusting findings | PP-S-10 developers deliver client code without a consistent secure SDLC |
| PP-P-06 small AppSec team relative to developers; onboarding cannot depend on hand-holding | PP-S-07 regulated clients ask for evidence of control coverage and remediation |
| PP-P-19 regulator-driven remediation timelines in financial services | |

## 4. Root causes

1. **Tool rollouts treated as deployments, not products.** Enablement is measured; adoption, alert quality, remediation and operations are not designed.
2. **Enablement confused with coverage.** A repository with scanning switched on may fail to build, use an unsupported language or never be analysed.
3. **One enablement pattern for a diverse estate.** Legacy builds, custom pipelines, hosting differences and regulated applications need different paths.
4. **Retiring the old tool too early, or never.** Without validated transition criteria, either coverage drops or both tools run forever and developers see every finding twice.
5. **Manual, per-repository change.** Onboarding and decommissioning that depend on each team editing its repository stall and drift.
6. **Fragmented administration.** Admin rights for the existing secret scanner were spread across the organisation with no single accountable owner.
7. **Alert volume used as the success measure.** Volume rewards noise; developers lose trust and dismiss alerts.

## 5. Solution: how the rollout was run

### 5.1 My role and the principles I set

As Product Manager I owned the initiative end to end: discovery and internal assessment, pilot, productisation, rollout, transition to operations and continuous improvement. I defined the product vision, roadmap, acceptance criteria, adoption targets, success measures and scaling strategy; led the evaluation of GHAS against the incumbent SAST tool and the in-house secret scanner; directed pilot engagement; drove zero-touch onboarding and legacy-tool decommissioning automation; led alert tuning; and set up remediation, SLA, closure-monitoring, governance and support mechanisms with teams across the product family and the wider enterprise.

The principles I set for every decision:

- Security coverage is never reduced during the transition.
- An existing tool is retired only after coverage, compliance, operational readiness and transition criteria are validated for that scope.
- Automation is the default; manual onboarding is the exception.
- Standard onboarding needs no developer action.
- Alert quality and actionability matter more than alert volume.
- Unsupported technologies keep complementary controls.
- Compliance, auditability, access governance, documentation and operational ownership are designed into the product.
- Enterprise standards are balanced with application-specific needs.

### 5.2 Internal assessment before broad adoption

Early effort went into understanding the current ecosystem before anything was switched on at scale:

- Existing SAST and secret-scanning capabilities, workflows, dependencies, support models and what decommissioning would involve.
- Application architectures, legacy technologies, repository patterns and languages, mapped to CodeQL support.
- Implementation and performance considerations on GitHub Enterprise and GitHub Cloud.
- Custom build and deployment pipelines: compatibility, run time, resources, failure modes and operational impact.
- Financial-domain compliance, governance, audit, access, evidence and exception requirements.
- Who administered the secret scanner and how access was granted.
- Representative pilot cohorts, evaluation criteria, success measures and exception paths.

### 5.3 Pilot-led validation with explicit acceptance criteria

Pilot teams were treated as product partners and chosen to cover varied stacks, legacy and modern architectures, repository profiles, both hosting environments, pipeline patterns, security maturity levels and compliance contexts. Their feedback on relevance, duplicates, navigation, remediation guidance, scan behaviour, pipeline impact, documentation and support shaped configurations, automation, communications and support before scaling.

| Criterion | What was assessed |
|---|---|
| Detection quality | Relevance, accuracy, precision and actionability; false-positive trends and recurring noise; known-case detection, comparative coverage and potential false-negative patterns; consistency across languages, architectures, repositories and hosting; how early in the SDLC findings appear; where default queries need enterprise customisation |
| Ease of remediation | Navigation from alert to code and impact; quality of in-context guidance; efficiency of triage, ownership, fixing and validation; usefulness of autofix as an accelerator under developer review, tests and change control |
| Scale and coverage | Whether onboarding can be automated with no developer action; scale across repositories, departments and product families; coverage across supported languages, both hosting environments, legacy apps and custom pipelines; ability to flag exceptions and keep complementary controls |

Precision (are the alerts right?) and recall (what is being missed?) were assessed separately, because false positives and false negatives need different analysis.

### 5.4 Segmentation and exception management

One pattern did not fit the whole portfolio, so applications and repositories were segmented to decide standard eligibility, extra assessment, complementary controls and exception paths:

| Segment | Path |
|---|---|
| Modern apps in CodeQL-supported languages, standard pipelines | Standard zero-touch onboarding |
| Legacy apps with complex architectures or build dependencies | Additional assessment; standard enablement only where technically appropriate |
| Unsupported or partly supported languages | Existing or complementary SAST retained; documented as a coverage gap, not as covered |
| Customised CI/CD and deployment pipelines | Pipeline impact analysis before enablement |
| Financial-domain or otherwise regulated apps | Compliance requirements checked; evidence and access rules applied |
| GitHub Enterprise versus GitHub Cloud | Environment-specific configuration and monitoring |

Exceptions required a technical assessment, coverage and risk analysis, a documented rationale, a named owner, approvals, alternative controls and periodic reassessment.

### 5.5 Coverage, performance and pipeline impact

- **Language coverage.** CodeQL support was mapped against the enterprise technology landscape, and unsupported languages were listed explicitly so that GHAS enablement was never read as complete SAST coverage. Required capabilities were not retired early.
- **Performance across hosting environments.** Scan behaviour was evaluated against repository size, complexity, language, build needs, workflow design, scan duration, resource use, configuration consistency, monitoring and troubleshooting. The goal was scalable patterns, accepting that performance varies by context; no unsupported comparison between environments was assumed.
- **Custom pipelines.** Impact analysis covered workflow changes, CodeQL build requirements, run time, compute, failure behaviour, dependencies, interaction with existing controls, rollback, troubleshooting ownership and shared pipeline components, so platform teams had confidence before enablement.

### 5.6 Compliance and governance designed in

- Control coverage and continuity through the transition.
- Traceability from detection to ownership, remediation, exception, risk acceptance or closure.
- Risk-based prioritisation and SLA monitoring.
- Audit evidence and retention.
- Role-based access, least privilege and separation of duties where required.
- Documented exception and approval processes, and control documentation suitable for audit.

### 5.7 Alert tuning and customisation

Customisation was evidence-driven: default query suites, configuration choices, custom queries or query packs where justified, recurring false-positive patterns, potential coverage gaps and maintenance cost were analysed together. The aim was higher relevance and developer trust without drifting far from the supported platform or creating a query library nobody can maintain.

### 5.8 Zero-touch onboarding and batch-based rollout

Standard onboarding was automated: eligibility identification, standardised configuration, repeatability and less drift, with no developer action for typical repositories. Developers spent their time where their judgement is needed: understanding findings, assessing context, fixing, reviewing autofix suggestions and giving feedback.

Rollout ran in controlled batches, each one a learning loop: **Enable → Observe → Learn → Refine → Scale**.

1. Validate eligibility, language support, technical readiness, compliance needs and pipeline dependencies.
2. Apply automated onboarding and standard enablement patterns.
3. Monitor scan behaviour, performance, alert quality, support demand and remediation experience.
4. Collect feedback from newly onboarded teams.
5. Find recurring issues, exceptions and documentation gaps.
6. Refine automation, configuration, communications, support and the next batch plan.

### 5.9 Automated decommissioning of the legacy tool

Where a transition was approved, retiring the old tool's integrations was automated wherever feasible, and only after coverage, readiness, compliance and transition criteria were met for that scope. This removed repetitive repository-level changes, duplicate alerts and tool overlap, kept transitions consistent and auditable, kept complementary controls in place and spared developers a second round of migration work.

### 5.10 Admin roles, documentation and change enablement

- **Access management.** Security, platform, identity and access management, governance and operations stakeholders worked together to give the secret-scanning capability clear administrative ownership, role-based and least-privilege access, separation of duties where needed, consistent practices and defined support and escalation paths.
- **Documentation as part of the product.** Vision, scope, architecture, evaluation outcomes and decision principles; language and coverage mapping; eligibility, onboarding, configuration and exception guidance; developer guidance on alerts, triage, remediation and autofix; ownership, SLA, escalation, closure and risk treatment; pipeline guidance and known limitations; admin roles; compliance considerations; transition, decommissioning, support and troubleshooting; metrics and review ownership.
- **Change enablement.** Leadership updates, readiness sessions, pilot forums, developer communications, onboarding notifications, FAQs, office hours, migration guidance, operational handovers, support channels and feedback loops, tailored to AppSec and VM, GitHub platform admins, engineering teams, architecture and cloud, CI/CD and developer experience, IAM, governance, risk, compliance and audit, operations and leadership.

### 5.11 From pilot to operations

**Pilot validation → Productisation → Batch-based adoption → Enterprise coverage → Security outcomes → Continuous improvement**

In operations, early alert closures were analysed as a signal: they can mean fast remediation or effective autofix, but also noise, inconsistent dismissals, training needs or tuning opportunities. The operating loop was **Detect → Triage → Act → Close → Analyse → Tune → Improve**, looking at closure reasons and time to close, code fixes versus dismissals, patterns by query, language, repository or department, repeated "false positive", "test code" or "acceptable risk" classifications, and reopened findings.

### 5.12 Product organisation variant

For a company that builds its own software, this is the main pattern: treat the AppSec platform as an internal product with a PM, acceptance criteria, a roadmap and adoption metrics. Pair it with paved roads and champions from CS25, exploit-driven prioritisation from [CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md) for dependency findings, and pipeline hardening from CS12, since enabling code scanning changes workflows and permissions.

### 5.13 Services organisation variant

IT services firms that run AppSec platforms or tool migrations for many clients can package the same model: a reusable eligibility and segmentation rulebook, a language-coverage matrix, onboarding and decommissioning automation, pilot acceptance criteria, and a client-specific exception register and evidence pack. Each client keeps its own configuration, admin model and SLAs. Where the firm's developers work inside client GitHub organisations, the client's alerts, SLAs and closure rules apply to the firm's code too (PP-S-10).

## 6. Phased plan

Phases and exit gates as run; durations depend on the estate and are not given here.

| Phase | Deliverable | Exit gate |
|---|---|---|
| 1 Assess | Current-state map of tools, workflows, languages, hosting, pipelines, compliance needs and admin model; pilot cohorts and acceptance criteria | Criteria and segments agreed with security, platform and governance |
| 2 Pilot | Representative teams onboarded; detection, remediation and scale criteria measured; feedback captured | Acceptance criteria met or gaps owned |
| 3 Productise | Standard configurations, onboarding automation, documentation, support model, exception process, compliance evidence | Zero-touch onboarding works for the standard segment |
| 4 Scale in batches | Enable, observe, learn, refine, scale per batch | Each batch reviewed before the next |
| 5 Transition | Decommissioning automation for approved scopes; complementary controls kept for unsupported scope | Coverage, readiness and compliance validated per scope |
| 6 Operate and improve | SLA and ageing monitoring, early-closure analysis, tuning, documentation ownership | Regular operational reviews in place |

## 7. KPIs

The measurement framework I used. Internal values are confidential; the targets below are illustrative starting points, not the organisation's numbers.

| Dimension | Measures | Illustrative target |
|---|---|---|
| Detection quality | Precision and relevance, false-positive trend, known-case detection, false-negative and coverage analysis, timeliness | Recurring noise patterns falling batch on batch |
| Developer experience | Ease of navigation, usefulness of guidance and autofix, pilot and batch feedback, onboarding effort, support demand | No developer action for standard onboarding |
| Enterprise adoption | Eligible repository coverage, successful analysis coverage, department and product-family coverage, automated onboarding rate, exception population | Every eligible repository analysed successfully, not just enabled |
| Remediation outcomes | SLA compliance, time to ownership, time to remediation, ageing, closure quality, reopened findings | High-severity findings past SLA trending down |
| Continuous improvement | Early-closure trends, query and configuration improvements, recurring-noise reduction | Learning from each batch applied to the next |
| Transition efficiency | Validated decommissioning, reduction in manual migration effort, duplicate tooling and duplicate alerts | Zero scopes retired before coverage is validated |

Four coverage numbers are kept separate: technically enabled, successfully analysed, capability applicable (language supported) and effectively covered.

## 8. Tooling options

- **GitHub native:** GitHub Code Security (CodeQL code scanning, default and advanced setup, Copilot Autofix), GitHub Secret Protection (secret scanning, push protection, custom patterns), Dependabot, security configurations at organisation and enterprise level, security overview, REST and GraphQL APIs for automation and reporting.
- **Open source / free:** CodeQL CLI and query packs (free for open source), Semgrep community rules for languages CodeQL does not cover, Gitleaks and TruffleHog, OpenSSF Scorecard, DefectDojo for aggregating findings.
- **Commercial categories:** incumbent SAST suites kept for unsupported languages, ASPM platforms for one view across scanners, secret-detection platforms covering non-GitHub sources, GRC tooling for exception and evidence management.

## 9. Risks and trade-offs

| Trade-off or risk | How it was handled |
|---|---|
| Rollout speed versus depth of validation | Pilot acceptance criteria and batch gates; speed came from automation, not from skipping checks |
| Standardisation versus flexibility for legacy and specialised apps | Segmentation with standard and exception paths |
| Tool consolidation versus continuity of coverage | Retire only after validated coverage; complementary controls for unsupported languages |
| Automated enablement versus application-specific control | Eligibility rules; pipeline impact analysis before enabling custom pipelines |
| Detection sensitivity versus alert noise and fatigue | Evidence-driven tuning; early-closure analysis |
| Central governance versus distributed admin ownership | Clear admin model with least privilege and separation of duties |
| Faster decommissioning versus compliance and readiness | Transition criteria per scope, signed off before retirement |
| Developer convenience versus regulated control requirements | Compliance needs designed into configuration, evidence and access |
| Autofix accepted without review | Autofix treated as a suggestion under normal review, tests and change control |

## 10. Learnings

1. Enterprise AppSec transformation is a product, architecture, governance, developer-experience and change challenge, not only a tool deployment.
2. Technical evaluation alone does not reveal developer friction, alert usability, documentation gaps or support needs; representative pilot users do.
3. Alert volume is not success. Trust, precision, actionability, timely detection, remediation and closure quality are.
4. False positives and false negatives need different analysis; assess precision separately from recall and coverage.
5. Broad repository enablement is not effective security coverage.
6. Automation speeds adoption, but eligibility rules, exception management, impact analysis, documentation, governance and complementary controls make it safe.
7. Developer experience covers the whole transition; automating both onboarding and decommissioning reduces fatigue.
8. Batch-based rollout is a learning system that improves automation, configuration, support and documentation over time.
9. Design transition and operations early: ownership, access, support, escalation, documentation and life-cycle management.
10. Retire a security tool after its replacement's coverage and readiness are validated, not when the replacement is merely switched on.

## References

- GitHub Blog, "Introducing GitHub Secret Protection and GitHub Code Security" (March 2025): https://github.blog/changelog/2025-03-04-introducing-github-secret-protection-and-github-code-security/
- GitHub Docs, About code scanning with CodeQL and supported languages: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql
- GitHub Docs, Configuring default setup for code scanning at scale: https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning-at-scale
- GitHub Docs, About enabling security features at scale (security configurations): https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale
- GitHub Docs, Responsible use of Copilot Autofix for code scanning: https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning
- GitHub Docs, About push protection: https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection
- GitGuardian, The State of Secrets Sprawl 2025: https://blog.gitguardian.com/the-state-of-secrets-sprawl-2025/
- NIST SP 800-218, Secure Software Development Framework: https://csrc.nist.gov/pubs/sp/800/218/final
- CISA, Secure by Design: https://www.cisa.gov/securebydesign
