# CS50: Why Security Tools Fail to Land: Adoption Challenges for Organisations and Scaling Challenges for Security Vendors

Domain: All sectors; SaaS, BFSI, Healthcare, Manufacturing, Public sector, IT services, MSSPs and security product vendors · Org type: both

> **Point of view.** The same security tool can be a success in one organisation and shelfware in the next. This case study looks at that gap from both ends of the contract: the **organisation adopting a security tool** (the buyer, whether a product company, a bank, a hospital or an IT services firm) and the **security product vendor** trying to scale the tool across hundreds or thousands of customer organisations. For each side it lists the problem statements, the root cause behind each one, and recommended next steps, then picks out **five key actions** for each side separately. It ends with where the two sides meet, because most adoption failures are caused jointly.
>
> Vendor-neutral. Products are named only where a public event is the example. Survey figures are dated in the text; some well-known figures are several years old and are marked as such, because the pattern they describe has not changed. Companion file: [adoption-scorecards.md](adoption-scorecards.md) with an adoption-readiness scorecard for buyers and a scale-readiness scorecard for vendors.
>
> Related case studies: tool selection by organisation size (CS46), a first-hand enterprise rollout ([CS35](../CS35-GitHub-Advanced-Security-Enterprise-Rollout/README.md)), AppSec debt and developer ratio ([CS25](../CS25-AppSec-Debt-and-Developer-Ratio/README.md)) and IGA application onboarding at scale (CS42).

## In plain business terms (for readers outside IT)

**The short version.** Buying a security tool is like buying a gym membership: the value comes from turning up every week, not from signing the contract. Organisations often buy tools that nobody has time to set up, that raise more alarms than the team can read, or that overlap with tools they already own. Vendors, for their part, sell a tool that works brilliantly in a demo and in their first fifty customers, then struggle when the next five hundred customers each have different systems, rules and skills.

| Side | The problem, in business terms | It is like... | The question to ask |
|---|---|---|---|
| Organisation | We pay for tools that are switched on but not used | A burglar alarm installed but never armed | "Which of our security tools has a named owner and a weekly routine?" |
| Organisation | Tools raise so many alerts that real ones are missed | A smoke detector that goes off every time someone makes toast | "What share of alerts led to a real fix last quarter?" |
| Organisation | We own several tools that do the same job | Three different alarm companies watching the same door | "Which tools could we drop without losing coverage?" |
| Vendor | What worked for early customers breaks for larger or regulated ones | A restaurant that cannot cope when it opens ten branches | "Can a new customer get value in 30 days without our engineers on site?" |
| Vendor | Customers buy but do not renew because they never got value | Selling gym memberships nobody uses, then losing them at renewal | "How many customers use the product weekly, and how many just pay?" |

**Three decisions for a board or owner**

1. **Fund the running, not just the buying.** Every security tool budget line carries the people time to run it, typically agreed before purchase.
2. **Measure outcomes, not ownership.** Ask how much risk the tool removed, not how many tools the organisation has.
3. **Retire before you add.** A new tool is approved only with a named tool to retire or a gap it provably fills.

## 1. Problem statement

**Adoption side.** Organisations buy security tools faster than they can absorb them. Tools are bought by feature list and analyst quadrant, deployed partially, tuned rarely and owned by nobody once the project team moves on. Each tool raises its own findings in its own console, developers and IT teams treat security tickets as noise, and the security team cannot show the board which spend reduced which risk. The result is tool sprawl, shelfware, alert fatigue and duplicate cost alongside real coverage gaps.

**Scaling side.** Security product vendors find that the product that won their first customers does not scale across organisations. Every new customer has a different identity provider, code host, cloud mix, ticketing tool, data-residency rule and maturity level. Onboarding depends on vendor engineers, detection content tuned for one estate is noisy in the next, multi-tenant architecture strains under large or regulated customers, and pricing units that suited start-ups surprise enterprises at true-up. Customers buy but do not reach value, and churn shows up at the first renewal.

The question this case study answers: **why do security tools fail to land in organisations, why do security products struggle to scale across organisations, and what should each side do first?**

## 2. Why now

| Driver | What happened | Effect on adoption and scaling |
|---|---|---|
| **Tool sprawl is measured and costly** | IBM Institute for Business Value and Palo Alto Networks (survey of 1,000 executives, Jul-Sep 2024, published 28 Jan 2025): organisations run an average of **83 security solutions from 29 vendors**; 52% call complexity the biggest obstacle to security operations; executives estimate fragmentation costs about 5% of annual revenue | Buyers are now judged on what they retire, not only on what they add; vendors must prove they replace something |
| **Consolidation became the default buying intent** | Gartner (418 respondents, Mar-Apr 2022): **75%** of organisations pursuing vendor consolidation, up from 29% in 2020; only 29% expected lower licence spend, 65% expected better risk posture | Point products must integrate or be absorbed; platforms must prove depth in every module they sell |
| **Shelfware is an old, unsolved pattern** | Osterman Research for Trustwave (Jan 2015): about **28%** of security software spend underused or unused; top reasons were IT too busy (35%) and too few resources (33%), with insufficient vendor support at 18% | The constraint is people and time, not features; the figure is old, but the causes appear unchanged in later surveys |
| **Market consolidation by acquisition** | Google completed its acquisition of Wiz on 11 Mar 2026; earlier, Tenable bought Vulcan Cyber (2025), Black Duck separated from Synopsys (2024) and ZAP moved under Checkmarx (2024) (see CS46) | Buyers face roadmap and licence changes mid-adoption; vendors face customers asking for exit terms |
| **Regulation asks for evidence of operation** | EU CRA vulnerability reporting from 11 Sep 2026; PCI DSS v4.0.1 future-dated requirements mandatory since 31 Mar 2025; DORA applied from 17 Jan 2025; NIS2 transposition across the EU; CERT-In six-hour reporting in India | An installed tool is no longer enough; auditors ask for coverage, SLA and remediation evidence the tool must produce |
| **AI raises volume on both sides** | AI coding assistants raise code volume; vendors add AI triage, autofix and agentic features to every product | More findings to absorb for buyers; for vendors, AI features must earn trust before they reduce work |

## 3. Pain points addressed

| Product organisations | Services organisations |
|---|---|
| PP-P-47 (new) security tools bought faster than they are absorbed: partial deployment, no owner after go-live, alert noise developers ignore, overlapping tools and no outcome measure, so spend rises while coverage stays unproven | PP-S-43 (new) services firms and MSSPs adopt and operate security tools across many client estates: per-client onboarding by hand, licences and data separation per tenant, client-specific tuning that does not carry over, and tool choices dictated by each client contract |
| PP-P-48 (new) security product vendors cannot scale the product across customer organisations: bespoke onboarding, integration long tail, detection content tuned for early customers, multi-tenant limits for large and regulated customers, pricing units that surprise at true-up, and churn from customers who never reached value | PP-S-38 MSSPs and IT services firms must offer AppSec and VM to clients of every size with multi-tenant licensing |
| PP-P-01 scanner noise; developers stop trusting findings | PP-S-01 hundreds of client environments with different scanners and SLAs |
| PP-P-35 consolidating overlapping AppSec tools across a mixed estate | PP-S-30 tool rollouts and migrations for clients run as one-off projects |
| PP-P-43 tools bought for the wrong organisation size | PP-S-05 skills shortage; junior analysts triage without context |

---

## Part A: Organisations adopting security tools

### A.1 Problem statements, root causes and recommended next steps

| # | Problem statement | Root cause | Recommended next steps |
|---|---|---|---|
| A1 | **Tools are bought by feature list, not by operating model.** The contract is signed before anyone asks who will run the tool every week. | Procurement and security evaluate capability (analyst reports, demos, RFP checklists); operating cost in people time is not part of the business case. | Add an operating-model section to every business case: owner, weekly routine, FTE needed, integrations, first 90-day outcomes. No purchase without a named run owner. |
| A2 | **Partial deployment that looks complete.** Agents on 60% of endpoints, scanners on half the repos, cloud accounts added only at launch. | No reconciled asset inventory to measure coverage against; rollout ends when the project budget ends, not when coverage is proven. | Define coverage against an inventory (CMDB, cloud accounts, code host, identity directory). Track coverage % weekly until it reaches the agreed target; keep the project open until then. |
| A3 | **Alert and finding noise.** Default rules produce thousands of findings; teams tune nothing and start ignoring the tool. | Out-of-the-box policies are tuned for the vendor's demo, not the buyer's estate; no time budgeted for tuning; severity not tied to exploitability or business context. | Run a tuning sprint before broad rollout: baseline false-positive rate on own code and assets, disable low-value rules, prioritise by exploitation evidence (KEV, EPSS) and asset criticality ([CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md)). |
| A4 | **Developers and IT teams do not act on findings.** Security tickets sit in a separate console or a backlog nobody grooms. | Findings are delivered where security works, not where engineers work; ownership of the fix is unclear; no SLA or incentive. | Deliver findings into pull requests, IDEs and the team's existing ticket queue; route by code or asset owner; agree remediation SLAs with engineering leadership; start blocking only after trust is earned. |
| A5 | **Integration gaps make each tool an island.** Separate consoles, no SSO or SCIM, no feed to SIEM, ticketing or CMDB. | Integration is treated as phase 2; connectors exist but nobody owns building and maintaining them. | Make SSO, SCIM, ticketing, SIEM and asset-inventory integration acceptance criteria in the proof of concept, not after go-live. |
| A6 | **Tool sprawl and overlap.** Two SAST tools on the same repos; three products with endpoint agents; nobody knows what can be retired. | Tools are added per incident, audit finding or acquisition; there is no capability map and no retirement process. | Build a capability map (control, tool, coverage, owner, cost, renewal date). For each overlap, choose a primary tool, prove coverage, then retire the other at renewal ([CS35](../CS35-GitHub-Advanced-Security-Enterprise-Rollout/README.md)). |
| A7 | **Skills and capacity gap.** The one engineer who understood the tool leaves; analysts lack time to learn advanced features. | Training is a one-off at go-live; tool knowledge is not documented; security teams are understaffed relative to the estate. | Fund a run budget (people time) alongside licence cost; document runbooks; train two people per tool; use the vendor's customer success and managed options where internal capacity is thin. |
| A8 | **No outcome measure.** Success is reported as "deployed" or "number of findings", so the board cannot tell whether spend reduced risk. | KPIs are chosen from what the tool reports, not from the risk the tool was bought to reduce. | Define two or three outcome KPIs per tool before purchase (for example exploited-vulnerability mean time to remediate, secrets exposure time, coverage of tier-1 assets) and review them quarterly. |
| A9 | **Change resistance and workflow friction.** Agents slow laptops, pipeline gates break builds, new MFA prompts frustrate staff. | Rollout is done to users rather than with them; no pilot with representative teams; performance and friction not measured. | Pilot with a willing team per business unit; measure friction (build time added, agent CPU, help-desk tickets); publish the fix for each complaint; use champions. |
| A10 | **Licence and renewal surprises.** Contributor, asset or workload counts overrun; vendor is acquired and terms change mid-contract. | Licence units modelled on today's headcount; no change-of-control, data-export or price-cap terms. | Model licence units for three years; add renewal caps, data-export and termination-on-change-of-control clauses; review usage counts monthly. |

### A.2 Deep dive: the root causes behind the root causes

Across the ten problem statements, four underlying causes recur:

1. **Capability is bought; capacity is not.** The licence is a capital-style decision with a clear owner; the people time to run the tool is an unbudgeted assumption. Shelfware surveys have cited "too busy" and "too few resources" as the top reasons for over a decade.
2. **No shared inventory to measure against.** Coverage, overlap and outcome are all impossible to prove without a reconciled view of assets, code, identities and suppliers. Each tool brings its own partial inventory, which makes the sprawl worse (CS49, wave 0).
3. **Security sits outside the engineering workflow.** Where findings go to a security console, they are ignored; where they arrive in the pull request or the team's queue with a clear owner, they get fixed.
4. **The adoption project ends too early.** Go-live is treated as the finish line. Value comes in the months after: tuning, integration, ownership, and retirement of what the tool replaced.

### A.3 Domain notes for adopters

| Domain | What is different |
|---|---|
| **BFSI** | Regulators (DORA, RBI, SEBI CSCRF, PCI DSS) expect evidence that controls operate, so partial deployment is an audit finding; change windows are tight, so pilots need production-like test environments |
| **Healthcare** | Clinical systems and medical devices cannot take agents or reboots; adoption depends on passive and network-based tools and clinical engineering buy-in (CS13) |
| **Manufacturing and OT** | IT tools often cannot run on OT assets; separate OT visibility tools must still feed one risk view (CS20) |
| **Public sector** | Procurement cycles are long and framework-bound, so a tool is often chosen years before the team that runs it is hired; data-residency and sovereign-cloud rules narrow choice |
| **SaaS and technology** | Engineering autonomy is high; tools that add friction to developers are bypassed, so developer experience decides adoption ([CS25](../CS25-AppSec-Debt-and-Developer-Ratio/README.md)) |
| **IT services and MSSPs** | Must adopt tools that work across many client estates with tenant separation and client-specific contracts; see A.4 |

### A.4 Product organisation and services organisation variants

- **Product organisations** adopt tools for their own estate and their own product. The main risk is developer rejection: tools that slow builds or flood pull requests are bypassed. Lead with the developer workflow, tune before gating, and measure fix rates per team.
- **Services organisations** (IT services, MSSPs, SIs) adopt tools twice: for their own estate, and as a delivery platform across client estates. The main risks are per-client onboarding by hand, licences that do not fit multi-tenant use, tuning that does not carry from one client to the next, and contracts where the client chooses the tool. Standardise a reference stack, build onboarding as code, keep a reusable tuning library per sector, and write tool ownership, data handling and exit into the client contract.

### A.5 Key 5 actions for organisations adopting security tools

| # | Action | What it looks like in practice | Measure of success |
|---|---|---|---|
| 1 | **Buy the operating model, not the feature list** | Every security tool business case names the run owner, weekly routine, FTE, integrations and 90-day outcomes; proof of concept runs on own code and assets with false-positive rate measured | 100% of new tool purchases have a named owner and a run budget |
| 2 | **Prove coverage against one inventory** | One reconciled inventory of assets, repos, cloud accounts and identities; each tool reports coverage % against it weekly; the rollout closes only at target coverage | Tier-1 asset coverage above 95% per tool within 90 days of go-live |
| 3 | **Put findings where the work happens** | Findings delivered to pull requests, IDEs and existing ticket queues, routed to the owner, prioritised by exploitation and business context, with agreed SLAs | Fix rate per team; mean time to remediate exploited vulnerabilities within SLA |
| 4 | **Retire before you add** | A capability map of control, tool, owner, cost and renewal date; a new tool requires a named retirement or a proven gap; overlaps resolved at renewal | Number of tools and vendors falling year on year, with coverage stable or rising |
| 5 | **Measure outcomes and keep the adoption project open until they move** | Two or three outcome KPIs per tool agreed before purchase and reviewed quarterly; adoption is "done" when the KPIs move, not at go-live | Quarterly outcome report per tool; tools with no outcome movement in two quarters go to a keep, fix or retire review |

---

## Part B: Security product vendors scaling tools across organisations

### B.1 Problem statements, root causes and recommended next steps

| # | Problem statement | Root cause | Recommended next steps |
|---|---|---|---|
| B1 | **Onboarding does not scale.** Each new customer needs vendor engineers for weeks; time to first value grows as customers get larger. | The product was built hand in hand with early adopters; setup steps live in engineers' heads, not in the product. | Measure time to first value per customer; turn the top onboarding steps into guided, self-service setup and onboarding-as-code (Terraform, APIs); publish reference deployments by segment. |
| B2 | **The integration long tail.** Every customer has a different identity provider, code host, cloud, SIEM, ticketing and CMDB; each missing connector stalls a deal or a rollout. | Integrations are built per deal by sales engineering; no integration platform, SDK or partner programme; connectors break when third-party APIs change. | Publish open APIs, webhooks and a connector SDK; prioritise connectors by revenue blocked; certify partner-built connectors; monitor connector health as a product metric. |
| B3 | **Detection content and defaults do not travel.** Rules tuned for early customers produce false positives in new estates; customers lose trust in the first month. | Defaults reflect the design-partner estate; tuning knowledge is held by customer success, not encoded in the product; no feedback loop from customer suppressions to rule quality. | Ship segment-specific default policies; collect (with consent) false-positive and suppression signals to improve rules; make tuning recommendations in-product; track precision per rule. |
| B4 | **Multi-tenancy and performance limits.** Large customers hit API rate limits, scan queues and data volumes the architecture was not built for; regulated customers need tenant isolation, data residency and customer-managed keys. | Architecture optimised for speed to market; isolation and residency added per deal; capacity planning based on average, not largest, customers. | Design for the largest 10% of customers: per-tenant quotas, regional data planes, customer-managed keys, documented isolation model; load test at 10x the largest customer (CS17). |
| B5 | **Deployment model mismatch.** SaaS-only products lose regulated, public-sector and OT customers; on-premises and air-gapped versions lag the SaaS release. | One deployment model chosen early; others built as forks with separate release trains. | Decide the deployment models per target segment deliberately; build one codebase with deployment profiles; publish feature parity and lag openly. |
| B6 | **Pricing and packaging friction.** Licence units (contributors, credits, assets, workloads) that suited start-ups surprise enterprises at true-up; modules bundled into a platform are hard to compare. | Pricing designed for land, not expand; usage not visible to the customer between renewals. | Give customers a live usage view and forecast; offer price caps and committed-use bands; keep a simple path from a single module to the platform; publish what each unit counts. |
| B7 | **Customers buy but do not reach value, then churn.** Licences are sold, deployment stalls, and renewal is lost. | Sales compensation rewards bookings, not adoption; customer success is reactive and understaffed; no product telemetry on adoption depth. | Define a value milestone per product (for example first critical finding fixed through the workflow) and instrument it; tie part of sales and customer success incentives to adoption; intervene on accounts with stalled deployment in the first 90 days. |
| B8 | **Trust and assurance load grows with each customer.** Security questionnaires, SOC 2 and ISO 27001 evidence, pen-test reports, SBOMs and data-processing reviews per deal; the security vendor is itself a supply-chain target. | Assurance handled deal by deal; vendor's own security programme not productised as evidence. | Publish a trust centre with current attestations, SBOM, vulnerability disclosure policy and incident history; meet EU CRA reporting for the vendor's own products; answer questionnaires from a maintained evidence library (CS33). |
| B9 | **Platform breadth versus depth.** Consolidation pressure pushes vendors to add modules; shallow modules lose to specialists in proofs of concept and damage trust in the core. | Roadmap driven by competitive checklists rather than depth of use; acquisitions integrated at the console level only. | Add modules only where a shared data model gives a real advantage; publish depth benchmarks; integrate acquisitions at the data and workflow level before cross-selling. |
| B10 | **Partner and channel scale.** MSSPs, SIs and resellers sell and run the tool, but lack multi-tenant consoles, partner APIs and training, so delivery quality varies. | Partner programme designed for resale, not for delivery; product has no MSSP mode. | Ship an MSSP mode (multi-tenant console, delegated administration, per-client billing and reporting); certify partners on delivery outcomes; give partners the same onboarding automation as direct customers. |

### B.2 Deep dive: the root causes behind the root causes

1. **Design-partner overfitting.** Early customers shaped the product, defaults and onboarding. What scaled to fifty customers was really a service delivered by the founding engineers.
2. **Bookings measured, adoption not.** When revenue is recognised at signature and renewal is a year away, stalled deployments are invisible until churn.
3. **Integration treated as services, not product.** Each connector built for a deal becomes a maintenance liability; customers experience the gaps as product quality.
4. **Architecture sized for the average customer.** Large and regulated customers are where growth is, and where isolation, residency, scale and deployment flexibility are non-negotiable.

### B.3 Domain notes for vendors selling into each sector

| Domain | What scaling requires |
|---|---|
| **BFSI** | Data residency, customer-managed keys, regulator-ready evidence (DORA register of ICT third parties, RBI and SEBI outsourcing rules), exit plans and concentration-risk answers (CS09) |
| **Healthcare** | Agentless and passive options for clinical systems; HIPAA business associate terms; medical-device integrations |
| **Manufacturing and OT** | On-premises or air-gapped deployment; OT protocol support; no active scanning by default |
| **Public sector** | Sovereign-cloud and FedRAMP or national equivalents; framework procurement listings; long sales cycles that need partner delivery |
| **SaaS and technology** | Developer experience, API-first design, self-serve onboarding and usage-based pricing |
| **MSSPs and IT services** | Multi-tenant console, delegated administration, per-client billing and data separation |

### B.4 Product organisation and services organisation variants

- **Security product companies** (the vendor itself) should run Part B as a product and go-to-market programme owned jointly by product, engineering and customer success, with adoption telemetry as the shared metric.
- **Services organisations that productise tools** (MSSPs building managed detection or managed VM on top of vendor tools, SIs packaging a "security platform" for clients) face Part B problems at smaller scale: onboarding each client, tuning across estates, multi-tenant data separation and pricing per client. The same five actions apply, with the vendor's MSSP mode and APIs as prerequisites in vendor selection.

### B.5 Key 5 actions for security product vendors scaling across organisations

| # | Action | What it looks like in practice | Measure of success |
|---|---|---|---|
| 1 | **Productise onboarding and time to first value** | Guided setup, onboarding-as-code and segment reference deployments replace engineer-led onboarding; time to first value tracked per customer | Median time to first value under 30 days; share of customers onboarded without vendor engineers |
| 2 | **Treat integrations as a platform** | Open APIs, webhooks, connector SDK, certified partner connectors and connector health monitoring; roadmap prioritised by revenue blocked | Top 20 customer integration targets covered; connector failure rate; deals stalled for missing integrations |
| 3 | **Make defaults and detection content learn across customers** | Segment-specific policies, consented false-positive and suppression feedback, in-product tuning advice, precision tracked per rule | False-positive rate in first 30 days per new customer; share of findings actioned |
| 4 | **Architect for the largest and most regulated 10%** | Per-tenant quotas, regional data planes, customer-managed keys, documented isolation, deployment profiles from one codebase, an MSSP mode | Performance at 10x largest customer in load tests; regulated deals not lost on architecture |
| 5 | **Measure and reward adoption, not bookings** | A value milestone per product instrumented in telemetry; sales and customer success incentives partly tied to adoption; transparent usage and price forecasting for customers | Weekly active usage per licence; gross and net revenue retention; churn attributed to "never reached value" falling |

---

## 4. Where the two sides meet

Most adoption failures are jointly caused. The buyer under-resources the rollout; the vendor overpromises time to value. A short **mutual success plan**, agreed at signature, aligns both sides:

| Element | Buyer commits | Vendor commits |
|---|---|---|
| Owner | Named run owner and executive sponsor | Named customer success manager and technical contact |
| Scope | Inventory to measure coverage against; target coverage % | Supported integrations for the buyer's stack, confirmed in writing |
| Outcomes | Two or three outcome KPIs and a baseline | Time-to-first-value milestone and tuning support until it is met |
| Workflow | Engineering leadership agrees routing and SLAs | Findings delivered into the buyer's pull requests and ticketing tools |
| Review | Quarterly outcome review; keep, fix or retire decision | Usage and outcome report; roadmap commitments that affect the buyer |
| Exit | Data-export and retirement plan | Data export in an open format; change-of-control terms |

## 5. 90-day plans

| Days | Organisation adopting a tool | Vendor scaling a tool |
|---|---|---|
| 0-30 | Capability map of current tools (owner, cost, coverage, renewal); pick the top three overlaps; write the operating model and outcome KPIs for the next purchase | Instrument time to first value and weekly active use; identify the ten onboarding steps that need engineers; list integrations blocking revenue |
| 31-60 | Reconcile one inventory; measure coverage per tool; run a tuning sprint on the noisiest tool; route its findings into the engineers' workflow | Ship guided setup for the top three onboarding steps; publish API and webhook documentation; launch false-positive feedback from customers |
| 61-90 | Retire or consolidate one overlapping tool at renewal; first quarterly outcome review; publish keep, fix or retire decisions | Load test at 10x the largest customer; define the MSSP mode and data-residency roadmap; tie a share of customer success incentives to adoption milestones |

## 6. KPIs

| Organisation adopting tools | Vendor scaling tools |
|---|---|
| Tools and vendors in use, year on year | Median time to first value |
| Coverage % of tier-1 assets per tool | Share of customers onboarded self-service |
| Share of findings actioned, and false-positive rate | False-positive rate in the first 30 days |
| Mean time to remediate exploited vulnerabilities | Weekly active usage per licence |
| Licence utilisation (used versus paid units) | Gross and net revenue retention; churn from "never reached value" |
| Tools with a named owner and runbook | Integration coverage and connector health |
| Outcome KPIs moving per tool, per quarter | Support tickets per customer, trending down as customers grow |

## 7. Risks and how to handle them

| Risk | Mitigation |
|---|---|
| Consolidation leaves a coverage gap | Retire only after coverage on the replacement is proven per asset, repo and app |
| A platform module is shallow in one area | Test the weakest module in the proof of concept; keep a specialist only for that gap |
| Outcome KPIs are gamed (findings closed as "won't fix") | Audit closures; time-limited exceptions; pair counts with exposure measures |
| Vendor acquisition changes terms mid-adoption | Change-of-control, data-export and price-cap clauses; roadmap commitments in writing |
| Vendor adoption telemetry raises customer privacy concerns | Collect only usage metadata, with consent, documented in the data-processing agreement |
| Vendor incentives on adoption slow new sales | Phase in a small share of incentive first; measure net revenue retention alongside bookings |
| Self-service onboarding misconfigures a regulated customer | Guided checks and secure defaults; customer success review for regulated segments |

## 8. Learnings

1. **A tool is adopted when it has an owner, a routine and an outcome**, not when it is installed.
2. **People time is the real constraint.** Budget the run cost with the licence, or expect shelfware.
3. **Coverage needs an inventory.** Without one, neither buyer nor vendor can prove what the tool protects.
4. **Findings that arrive in the engineer's workflow get fixed.** Findings in a security console mostly do not.
5. **Vendors scale by turning services into product:** onboarding, integrations and tuning knowledge must move from people into the product.
6. **Adoption is the vendor's revenue.** Customers who never reach value churn, so adoption deserves the same measurement as bookings.
7. **Most failures are joint.** A mutual success plan at signature costs an hour and prevents most of them.

## References

- IBM Institute for Business Value and Palo Alto Networks, "IBM and Palo Alto Networks find platformization is key to reduce cybersecurity complexity" (28 Jan 2025): https://newsroom.ibm.com/2025-01-28-ibm-and-palo-alto-networks-find-platformization-is-key-to-reduce-cybersecurity-complexity
- Gartner survey on security vendor consolidation (Sep 2022), reported by Cyber Magazine: https://cybermagazine.com/articles/75-of-rganisations-are-pursuing-security-vendor-consolidat
- Osterman Research for Trustwave, security shelfware survey (Jan 2015), reported by CSO Online: https://www.csoonline.com/article/2876101/28-percent-of-security-spending-wasted-on-shelfware.html
- Google Cloud, "Google Completes Acquisition of Wiz" (11 Mar 2026): https://www.googlecloudpresscorner.com/2026-03-11-Google-Completes-Acquisition-of-Wiz
- Regulation (EU) 2024/2847, Cyber Resilience Act: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- Regulation (EU) 2022/2554, Digital Operational Resilience Act: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- PCI Security Standards Council, PCI DSS v4.0.1: https://www.pcisecuritystandards.org/document_library/
- CISA, Known Exploited Vulnerabilities Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- FIRST, Exploit Prediction Scoring System (EPSS): https://www.first.org/epss/
- CISA, Secure by Design: https://www.cisa.gov/securebydesign
