# CS47: Running a Penetration Testing Programme as a Security Manager

Domain: All sectors; BFSI, SaaS, Healthcare, Public sector, IT services and MSSPs · Org type: both

> **Point of view.** Written for the person who *owns* penetration testing in an organisation: a security manager, AppSec or VM lead, or a services-firm engagement manager. It covers how to decide what to test, scope it, authorise it, buy it, govern it while it runs, keep the SOC informed, turn findings into risk decisions, drive remediation and retest, and report KPIs. It deliberately contains **no exploitation steps, payloads or tool commands**: the testers own technique; the manager owns scope, safety, evidence and outcomes. Companion file: [governance templates](governance-templates.md).

## 1. Problem statement

Most organisations commission penetration tests every year, yet the same classes of finding come back year after year. Scope is set by budget and calendar rather than risk, so the payments flow gets the same five days as the marketing site. Asset lists come from a spreadsheet nobody reconciled, so internet-facing systems are missed and third-party assets are tested without permission. Authorisation is signed by whoever is available rather than the person who owns the asset. The SOC either is not told, raises a real incident and burns a day, or is told everything and learns nothing about detection. Reports arrive as long PDFs, findings are rated by the tester's CVSS score with no business context, they never enter the engineering backlog, and retests are skipped or done without evidence. Services firms face the mirror image: inaccurate scoping on fixed fees, inconsistent quality across testers, client environments not ready on day one, and retests that grow into unpaid new tests.

The question this case study answers: **how does a security manager run penetration testing as a programme, so that every test is risk-scoped, legally authorised, operationally safe, visible to the SOC, and ends with findings that are fixed, retested and reported as reduced risk?**

## 2. Why now

| Driver | What happened | Lesson |
|---|---|---|
| **Regulation asks for tests and evidence** | PCI DSS v4.0.1 requirement 11.4 (annual and after significant change, internal and external, segmentation testing, a documented methodology, remediation and retest) mandatory since 31 March 2025; DORA threat-led penetration testing (TLPT) RTS adopted in 2025; SEBI CSCRF (Aug 2024) requires VAPT by empanelled auditors; NIST SP 800-53 control CA-8 | A test without a documented methodology, retest evidence and closure trail now fails audit, not just good practice |
| **Release cadence outran the annual test** | Product teams ship weekly; cloud estates change daily | Point-in-time tests need to be complemented by change-triggered tests, continuous testing (PTaaS, bug bounty) and VM ([CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md)) |
| **Exposure is outside the asset list** | Edge appliances and forgotten internet-facing hosts keep featuring in mass-exploitation campaigns (CS02); exploitation of vulnerabilities was about 20% of initial access in the Verizon DBIR 2025 | Scoping must start from discovered attack surface, not the CMDB alone |
| **AI-assisted and "automated pentest" offerings** | Many vendors now sell automated or agentic testing at a fraction of manual prices (CS46) | Managers need a clear view of what automation covers well (breadth, regression) and what still needs human testers (authorisation, business logic, chained impact) |
| **Third parties and cloud** | Shared-responsibility models, SaaS and MSPs mean the asset under test is often not wholly yours; third parties feature in about 30% of breaches (DBIR 2025) | Authorisation and scope must name every party whose systems could be touched |

## 3. Pain points addressed

| Product organisations | Services organisations |
|---|---|
| PP-P-44 penetration tests scoped by budget and calendar rather than risk; findings sit in PDFs, are rated without business context, and are not retested, so the same findings recur | PP-S-39 testing providers scope fixed-fee tests on vague inputs, staff testers of uneven quality, wait on unready client environments and absorb retest scope creep |
| PP-P-10 customer questionnaires and pen-test evidence requests slow sales | PP-S-07 regulated clients demand test evidence (DORA, SEBI CSCRF, RBI) |
| PP-P-11 cloud misconfiguration across many accounts | PP-S-11 clients cannot say what is internet-facing |
| PP-P-12 API sprawl and broken object-level authorisation | PP-S-10 client blames the vendor for findings in delivered code |
| PP-P-06 AppSec to developer ratio of 1:100 or worse | PP-S-05 skills shortage; junior staff triage without context |

## 4. Root causes

1. **No test objective.** The test answers "are we compliant?" instead of a business question such as "can one customer read another customer's data?".
2. **Inventory is assumed.** Scope comes from what the team remembers, not from reconciled asset discovery.
3. **Authority is unclear.** Nobody checks that the signatory owns every in-scope asset, or that hosting, SaaS and cloud terms allow testing.
4. **Testing is bought on day rates, not outcomes.** Vendor selection compares price per day, not methodology, tester quality, report quality or retest terms.
5. **Governance stops at kick-off.** Nobody tracks coverage, safety or critical findings while the test runs.
6. **Ratings ignore context.** Tester severity is treated as business risk; nobody adjusts for exposure, data sensitivity or compensating controls.
7. **Findings are not owned.** No ticket, no owner, no SLA, no retest, so closure is a status change rather than evidence.

## 5. Solution: the programme lifecycle

```
 Programme level ─────────────────────────────────────────────────────────────────────────────
  Asset inventory & risk tiers ─► Annual test plan ─► Vendor panel ─► KPIs & board reporting
 Engagement level ────────────────────────────────────────────────────────────────────────────
  1 Discover ─► 2 Scope ─► 3 Authorise & RoE ─► 4 Ready ─► 5 Govern the test ─► 6 Report & rate
                                                               │                         │
                                             SOC monitoring & deconfliction    7 Remediate ─► 8 Retest & close
```

The manager runs two loops: a **programme loop** (yearly plan, vendor panel, KPIs) and an **engagement loop** for each test. The public methodologies map onto the engagement loop as follows; the manager should ask vendors which one they follow and require it to be named in the report.

| Engagement step (this case study) | PTES | NIST SP 800-115 | OSSTMM 3 | CREST / PCI DSS guidance |
|---|---|---|---|---|
| 1 Discover, 2 Scope | Pre-engagement interactions; intelligence gathering; threat modelling | Planning | Scope, channels and vectors | CREST buyer's guide: define requirements and scope; PCI pen test guidance: scoping the CDE |
| 3 Authorise and RoE | Pre-engagement (rules of engagement) | Planning (rules of engagement, Appendix B) | Rules of engagement | Contractual and legal authorisation |
| 4 Ready, 5 Govern the test | Vulnerability analysis, exploitation, post-exploitation (tester-owned) | Discovery and attack (tester-owned) | Test phases (tester-owned) | Conduct of testing, communication |
| 6 Report and rate | Reporting | Reporting | Security Test Audit Report (STAR) | Report quality and severity |
| 7 Remediate, 8 Retest | Not covered | Post-testing activities (Section 8) | Not covered | PCI DSS 11.4.4: findings corrected and retested |

### 5.1 Programme level: what gets tested and how often

**Asset inventory and risk tiers.** Build the test universe from reconciled sources: CMDB, cloud account inventories, DNS and certificate transparency records, external attack surface management (EASM), the code host, mobile app store listings and the SaaS register. Assign every asset or application an owner and a tier.

| Tier | Example | Minimum test cadence | Test type |
|---|---|---|---|
| 1 Critical | Payments, customer data stores, identity provider, internet-facing customer apps, cardholder data environment | Annually **and** on significant change | Grey-box application and API test; infrastructure test; segmentation test where PCI applies; threat-led or red team for the most mature |
| 2 High | Internal business apps with sensitive data, partner APIs, admin portals | Annually or every 18 months | Grey-box application test; internal infrastructure test |
| 3 Moderate | Internal tools, low-sensitivity sites | Every two years or on major change | Scanning plus light manual verification; bug bounty coverage |
| 4 Low | Static content, decommissioning | VM scanning only | No manual test |

**Define "significant change"** in policy so teams know when a test is triggered: new internet-facing service, authentication or authorisation change, new data class, new tenancy model, platform migration, major third-party integration, or merger and acquisition.

**Choose the right activity for the question.** Penetration tests prove exploitability within a scope; vulnerability scanning gives breadth; red team exercises test detection and response against an objective; purple team exercises improve detections collaboratively; bug bounty or a vulnerability disclosure programme gives continuous external coverage. A mature programme uses all five and does not ask any one of them to do another's job.

**Annual test plan.** Publish a 12-month calendar by tier, aligned with release trains, change freezes, audit dates and budget. Hold 15-20% of budget in reserve for change-triggered and incident-driven tests.

### 5.2 Vendor selection and panel management

| Criterion | What good looks like | How to check |
|---|---|---|
| Accreditation | CREST, CHECK (UK government), CERT-In empanelment (India), PCI QSA/ASV where relevant, TIBER/CBEST/DORA TLPT providers for threat-led tests | Certificates and scheme registers |
| Methodology | Named public methodology (PTES, NIST SP 800-115, OWASP WSTG for web, OWASP MASTG for mobile, OSSTMM) adapted to your context | Ask for their methodology document and a sanitised sample report |
| Tester quality | Named testers, relevant certifications, background checks, consistent lead tester across years for continuity, rotation at least every few years for fresh eyes | CVs before the SoW; right to approve substitutions |
| Report quality | Executive summary in business language, reproducible findings, evidence, risk rating with rationale, remediation advice, coverage statement (what was and was not tested) | Sample report; score it against the template in [governance-templates.md](governance-templates.md) |
| Data handling | Evidence encrypted, minimised, retained for an agreed period and destroyed with a certificate; compliant with DPDP Act 2023 or GDPR | Contract clause; data processing agreement |
| Communication | Daily status, critical findings reported within an agreed time (for example four hours), named emergency contact | SoW clause |
| Retest | Included within an agreed window (for example 90 days), scope limited to original findings | SoW clause |
| Liability and insurance | Professional indemnity and cyber insurance at an agreed level | Certificates |

Run a **panel of two or three vendors**: one primary per test type, a second for rotation and peak load. Score each engagement afterwards (findings validity, coverage, report quality, communication, retest) and use the scores at renewal.

### 5.3 Engagement step 1: discover

Before scoping, the manager gathers the context that makes the scope right:

- **Reconcile the asset list** for the application or environment against discovery sources; shadow assets found here are often the most valuable findings of the year.
- **Architecture and data flows**: trust boundaries, authentication model, tenancy model, third parties, logging.
- **Threat model**: the five to ten abuse cases that would hurt the business, written in business language (for example "an agent at the outsourced help desk exports customer records"). Use MITRE ATT&CK to describe relevant adversary behaviour for infrastructure and red team work, and the OWASP Top 10 and OWASP API Security Top 10 (2023) as coverage checklists for applications.
- **History**: previous reports, open findings, bug bounty reports, incidents and VM backlog. Retesting old findings is cheap and revealing.
- **Constraints**: fragile systems, change freezes, trading windows, data residency, clinical or OT safety.

### 5.4 Engagement step 2: scope

- **Objective in one sentence**, agreed with the business owner.
- **In scope**: explicit URLs, API base paths, IP ranges, cloud accounts, app builds, environments, roles and the version under test.
- **Out of scope**: explicit list, including third-party systems you do not own, denial-of-service, social engineering and physical access unless separately agreed.
- **Knowledge level**: grey-box (credentials and documentation) is the default for applications because it gives the most coverage per day; black-box when the question is specifically about an outsider; white-box (source code and architecture) for the highest-risk components.
- **Environment**: production gives realism but needs tighter rules; a production-like staging environment is acceptable if it matches authentication, WAF, data volumes and integrations. Record the differences in the report.
- **Effort**: estimate from attack surface (roles, functions, API endpoints, integrations, hosts), not page count. Add explicit days for reporting, quality assurance and retest. Time-boxed with coverage targets beats "find everything".
- **Coverage targets**: for example every role tested for horizontal and vertical access, every state-changing API tested for authorisation, every trust boundary crossed at least once. These let the manager check coverage without managing technique.

### 5.5 Engagement step 3: authorise and set rules of engagement

Authorisation is the legal line between a penetration test and an offence under laws such as India's IT Act 2000, the UK Computer Misuse Act 1990 and the US Computer Fraud and Abuse Act.

1. **Signed authorisation letter** from a person with authority over every in-scope asset, naming the testing firm, testers, dates, scope and source IP addresses.
2. **Third-party permissions**: cloud providers publish policies for customer testing (AWS, Microsoft Azure and Google Cloud generally allow testing of your own resources without prior approval but prohibit denial-of-service and testing of the provider's own infrastructure); hosting providers, SaaS vendors and MSPs need written permission or exclusion.
3. **Rules of engagement** (template in [governance-templates.md](governance-templates.md)): testing windows and time zone, permitted and prohibited activities, data handling, stop conditions, communication plan and escalation, SOC deconfliction model, cleanup and evidence destruction.
4. **Stop conditions** agreed in advance: service degradation, evidence of a prior or live compromise, real personal or payment data exposed beyond minimal proof, an out-of-scope system reached, or a critical issue with live external exposure.

### 5.6 Engagement step 4: readiness

A third of lost test days are lost to unready environments. Run a readiness check five working days before the start: accounts for each role (at least two per role so cross-account access can be tested), test data, VPN or jump host access, allow-listing of tester IPs where agreed, backups confirmed, monitoring contacts confirmed, and a kick-off call that walks through scope, RoE and the communication plan. Postpone rather than start unready.

### 5.7 Engagement step 5: govern the test while it runs

The manager does not direct technique but owns safety, scope and progress.

| Control | What the manager does |
|---|---|
| Daily stand-up or status note | Progress against coverage targets, blockers, findings so far, planned activity for the next window |
| Critical finding protocol | Tester reports criticals within the agreed time; manager convenes owner and security lead; decides whether to contain now (for example restrict access, rotate a credential) or continue testing; records the decision |
| Scope control | Any request to widen scope goes through change control with a signed amendment |
| Safety watch | Operations and application owners report anomalies; the stop conditions are invoked without debate if met |
| Prior-compromise protocol | If testers find signs of a real attacker, testing pauses and the incident response plan takes over; evidence is preserved |
| Coverage check at the midpoint | Compare tested functions and roles against targets; re-plan the remaining days |

### 5.8 Monitoring and deconfliction with the SOC

"Monitor" in a test has three meanings, and a good manager plans all three.

1. **Operational monitoring**: application, infrastructure and business monitoring to catch any impact early.
2. **Detection monitoring**: the SOC or MDR observes the test and records what it saw, which turns every test into a detection exercise at no extra cost.
3. **Post-test monitoring**: watching for the same weaknesses being used for real after the report, until fixes are verified.

Choose a deconfliction model per test and write it into the RoE:

| Model | Who knows | Use when | Deconfliction |
|---|---|---|---|
| **Announced** | SOC informed of dates, tester IPs and scope | Most application and compliance tests | SOC tags tester activity; still records which actions triggered alerts |
| **Partially announced** | SOC lead and a small "white cell" know; analysts do not | Measuring detection and triage | White cell confirms "is this the test?" within minutes through an out-of-band channel; a code word protects against an attacker claiming to be the tester |
| **Unannounced (red team)** | Only the white cell | Threat-led tests (TIBER-EU, CBEST, DORA TLPT) | White cell prevents a full incident response or external escalation; never used for routine tests |

After each test, run a short **detection review**: which tester activities were logged, alerted, triaged and escalated. Map gaps to MITRE ATT&CK techniques so the SOC can build detections; this is the start of purple teaming.

### 5.9 Engagement step 6: report and rate

**Require a consistent report structure** (template in [governance-templates.md](governance-templates.md)): executive summary with the objective answered, attack-path narrative in business terms, coverage statement, findings with evidence and reproduction steps for the engineering team, and remediation guidance.

**Separate technical severity from business risk.** The tester provides technical severity, typically with CVSS v4.0 and a rationale. The manager converts it into business risk by adjusting for:

| Factor | Moves risk up | Moves risk down |
|---|---|---|
| Exposure | Internet-facing, unauthenticated | Internal only, behind strong authentication |
| Data and function | Personal, payment or health data; money movement; admin functions | Public or test data |
| Exploitation evidence | Listed in CISA KEV, high EPSS, public exploit ([CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md)) | No known exploitation |
| Compensating controls | None | Verified WAF rule, network segmentation, monitoring alert that fires |
| Chaining | Part of an attack path to a crown jewel | Isolated |

Record the final rating, the rationale and who agreed it. **Never downgrade a finding silently**; a disputed finding gets a documented decision.

**Debrief** in two sessions: a technical walkthrough for engineers, and a 30-minute executive readout that answers the test objective, shows the top attack path and asks for decisions.

### 5.10 Engagement step 7: remediate

- **Every finding becomes a ticket** in the engineering backlog with an owner, a due date and a link to the evidence. The PDF is not the system of record.
- **Remediation SLAs by business risk**, for example: critical 15 days, high 30 days, medium 90 days, low next planned release. Align with the VM programme so one SLA model applies across scanning and testing.
- **Fix the class, not just the instance.** If authorisation flaws appear on three endpoints, ask for a central authorisation control and a regression test, not three patches (CS23).
- **Risk acceptance** only by the business owner, time-bound (for example six or twelve months), with compensating controls and a review date. Acceptances are reported at the risk committee.
- **Feed lessons back** into secure coding standards, threat-model templates, SAST and DAST rules and developer training.

### 5.11 Engagement step 8: retest and close

- Retest within the agreed window (for example 90 days) by the original tester or firm, limited to the original findings.
- **Closure needs evidence**: the retest result for each finding (fixed, partially fixed, not fixed, risk accepted), with the date and tester. PCI DSS 11.4.4 expects this trail.
- **Regression**: add a check for each fixed finding to automated testing where possible, so the issue cannot quietly return.
- Close the engagement: confirm cleanup of test accounts and artefacts, evidence destruction certificate, vendor scorecard, lessons learned.

### 5.12 Product and services variants

| Topic | Product organisation (buyer) | Services organisation (provider) |
|---|---|---|
| Scoping | Risk tiers and significant-change triggers drive scope; budget follows | Structured scoping questionnaire; price by attack surface; written assumptions; change-request process |
| Quality | Vendor scorecards; tester continuity; sample report standard | Methodology playbooks, peer review of every report, technical QA by a senior tester, finding library with consistent wording |
| Readiness | Internal readiness checklist owned by the app owner | Pre-engagement checklist sent with the SoW; start date only confirmed when readiness is met |
| Legal | Authorisation from the asset owner; third-party permissions | Never test without signed authorisation; verify the signatory's authority; professional indemnity |
| Retest | Built into the SoW | Priced explicitly; scope limited to original findings |
| Continuous testing | Combine annual tests with PTaaS, bug bounty and DAST in CI | Offer a subscription model with change-triggered testing |
| Data | Data processing agreement with each vendor | Evidence minimisation, encryption, destruction certificates (DPDP Act 2023, GDPR) |

## 6. 90-day plan

| Days | Action | Output |
|---|---|---|
| 1-30 | Reconcile asset inventory with EASM, cloud and code host; assign owners and tiers; define "significant change"; collect last two years of reports and open findings | Test universe with tiers; open-finding baseline |
| 31-60 | Publish the annual test plan; standardise SoW, authorisation letter, RoE and report templates; agree SOC deconfliction model; select or re-score the vendor panel | Test calendar; templates; panel |
| 61-90 | Run the first engagement on a Tier 1 asset with the full lifecycle; load all open findings into the backlog with SLAs; first KPI report to the risk committee | One end-to-end engagement; KPI baseline |

## 7. KPIs

| KPI | Definition | Target (example) | Why it matters |
|---|---|---|---|
| Tier 1 test coverage | Tier 1 assets tested in the last 12 months or since last significant change ÷ all Tier 1 assets | 100% | Proves the plan is executed where risk is highest |
| Change-triggered test rate | Significant changes tested before or within 30 days of go-live ÷ significant changes | ≥ 90% | Shows testing keeps pace with change |
| Unknown-asset discovery | In-scope assets found by discovery that were not on the inventory | Trending to zero | Measures inventory quality |
| Mean time to remediate by risk | Days from report to verified fix, by risk rating | Within SLA | Core outcome measure |
| SLA compliance | Findings fixed within SLA ÷ findings due | ≥ 90% critical/high | Accountability |
| Retest verification rate | Findings closed with retest evidence ÷ findings closed | 100% | Closure is evidence, not a status change |
| Repeat finding rate | Findings of the same class on the same asset as a previous test | Falling year on year | Shows root causes are being fixed |
| Risk acceptance age | Acceptances past review date | Zero | Stops acceptance becoming permanent |
| Detection rate | Tester activities that generated a SOC alert ÷ activities that should have | Rising | Turns tests into detection improvement |
| Readiness slippage | Test days lost to unready environments | < 5% | Operational efficiency |
| Vendor score | Average engagement scorecard | Rising; action below threshold | Drives vendor quality |

Report to the board or risk committee quarterly: coverage, open critical and high findings by age, SLA compliance, accepted risks, repeat findings and the top three attack paths found this quarter.

## 8. Tooling options (programme level, vendor-neutral)

| Need | Options |
|---|---|
| Asset discovery | EASM services; cloud inventory APIs; CMDB; certificate transparency monitoring |
| Findings management | The engineering issue tracker (Jira, Azure Boards, GitHub Issues) as the system of record; vulnerability or exposure management platforms that ingest pen test findings alongside scanner results; open-source DefectDojo |
| Reporting | Vendor report portals; collaborative report platforms used by many testing firms; a common finding library |
| Continuous testing | PTaaS platforms, bug bounty and VDP platforms, DAST in CI (CS46) |
| Detection review | SIEM and EDR data mapped to MITRE ATT&CK; ATT&CK Navigator for coverage views |

## 9. Risks and how to handle them

| Risk | Mitigation |
|---|---|
| Production impact from testing | Agreed windows, stop conditions, backups, operational monitoring, staged approach from low-risk to higher-risk activity agreed with the tester |
| Testing outside authority | Signatory check, third-party permissions, scope list with explicit exclusions, source IPs recorded |
| Real attacker mistaken for tester, or tester mistaken for attacker | Deconfliction model, white cell, out-of-band channel, code word, tester IP list |
| Sensitive data in evidence | Redaction at capture, encryption, retention limit, destruction certificate |
| Compliance-only testing | Test objectives tied to threat model; KPIs on outcomes, not test count |
| Automation replacing judgement | Use automated testing for breadth and regression; reserve human testers for authorisation, business logic and chained impact |
| Vendor lock-in or stale eyes | Panel of two or three, rotation of lead tester at intervals |

## 10. Learnings

1. **Start from the question, not the scope list.** A one-sentence objective agreed with the business owner shapes every later choice.
2. **Inventory first.** The most valuable finding is often an asset nobody knew about.
3. **Authorisation is a legal control.** Check the signatory and every third party before testing starts.
4. **Govern safety and coverage, not technique.** Managers add value through readiness, stop conditions, critical-finding handling and coverage checks.
5. **Every test is a free detection exercise** if the SOC records what it saw.
6. **Business risk is a decision, not a score.** Adjust tester severity for exposure, data, exploitation and controls, and record why.
7. **A finding is closed only with retest evidence.** Track repeat findings to prove root causes are fixed.

## References

- PTES, Penetration Testing Execution Standard - http://www.pentest-standard.org/
- NIST, SP 800-115 Technical Guide to Information Security Testing and Assessment (2008) - https://csrc.nist.gov/pubs/sp/800/115/final
- NIST, SP 800-53 Rev. 5 (CA-8 Penetration Testing) - https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- OWASP, Web Security Testing Guide - https://owasp.org/www-project-web-security-testing-guide/
- OWASP, Application Security Verification Standard - https://owasp.org/www-project-application-security-verification-standard/
- OWASP, Mobile Application Security (MASVS and MASTG) - https://mas.owasp.org/
- OWASP, API Security Top 10 (2023) - https://owasp.org/API-Security/
- ISECOM, OSSTMM 3 - https://www.isecom.org/OSSTMM.3.pdf
- CREST, Penetration Testing guidance and buyer's guides - https://www.crest-approved.org/
- PCI Security Standards Council, PCI DSS v4.0.1 and Penetration Testing Guidance - https://www.pcisecuritystandards.org/document_library/
- European Central Bank, TIBER-EU framework - https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html
- Commission Delegated Regulation (EU) on threat-led penetration testing under DORA - https://eur-lex.europa.eu/
- SEBI, Cybersecurity and Cyber Resilience Framework (CSCRF), August 2024 - https://www.sebi.gov.in/
- CERT-In, empanelled information security auditing organisations - https://www.cert-in.org.in/
- UK NCSC, Penetration testing guidance - https://www.ncsc.gov.uk/guidance/penetration-testing
- MITRE ATT&CK - https://attack.mitre.org/
- FIRST, CVSS v4.0 - https://www.first.org/cvss/v4-0/
- AWS, Penetration testing policy - https://aws.amazon.com/security/penetration-testing/
- Microsoft, Penetration testing rules of engagement for Microsoft Cloud - https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement
- Google Cloud, Acceptable Use Policy and security testing - https://cloud.google.com/terms/aup
- Verizon, 2025 Data Breach Investigations Report - https://www.verizon.com/business/resources/reports/dbir/
