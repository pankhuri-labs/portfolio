# CS47 governance templates

Templates a security manager can adapt for each engagement. They cover governance, authorisation and reporting only; test technique is left to the testing team. Back to the [case study](README.md).

## 1. Scoping questionnaire

| Area | Question | Answer |
|---|---|---|
| Objective | What one business question must this test answer? | |
| Driver | Compliance (which requirement), release, significant change, M&A, incident follow-up, customer request? | |
| Asset owner | Who owns each in-scope asset and can authorise testing? | |
| Assets | URLs, API base paths, IP ranges, cloud accounts, mobile builds, environments, version under test | |
| Exclusions | Third-party systems, shared hosting, payment processors, anything fragile | |
| Roles | User roles and tenants to be tested; accounts available per role | |
| Knowledge level | Black-, grey- or white-box; documentation and source available? | |
| Environment | Production or staging; differences from production | |
| Third parties | Cloud, hosting, SaaS, MSP, CDN/WAF providers involved; permission status | |
| Constraints | Change freezes, trading or clinical windows, data residency, fragile systems | |
| History | Previous reports, open findings, recent incidents | |
| Deliverables | Report format, debrief audiences, retest window | |

## 2. Authorisation letter (outline)

1. Organisation name and the signatory's role, with a statement that they have authority over the listed assets.
2. Testing firm and named testers.
3. Scope (attached list) and explicit exclusions.
4. Testing dates, windows and time zone.
5. Source IP addresses the testers will use.
6. Reference to the rules of engagement and the statement of work.
7. Third-party permissions obtained (attached) or confirmation that none are required.
8. Signature, date and an emergency contact.

## 3. Rules of engagement checklist

- [ ] Objective and scope attached; exclusions explicit
- [ ] Testing windows, blackout dates and time zone
- [ ] Tester names and source IP addresses
- [ ] Permitted activity agreed with the testing lead; prohibited activity listed (for example denial-of-service, data destruction, social engineering or physical access unless separately agreed)
- [ ] Approval needed before any higher-risk activity the testing lead flags
- [ ] Data handling: test data preferred; minimal, redacted proof if real data is encountered; encryption; retention period; destruction certificate
- [ ] Stop conditions: service degradation, signs of prior compromise, real data exposure beyond minimal proof, out-of-scope system reached, critical issue with live external exposure
- [ ] Communication plan: daily status, critical-finding reporting time, named contacts on both sides, 24x7 emergency contact, out-of-band channel
- [ ] SOC deconfliction model (announced, partially announced, unannounced), white cell members, verification code word
- [ ] Cleanup: test accounts, files and configuration changes removed or listed
- [ ] Retest window and scope

## 4. Daily status note

| Field | Content |
|---|---|
| Date and window | |
| Coverage so far | Functions, roles, endpoints or hosts covered vs targets |
| Findings so far | Count by technical severity; any critical raised (with time reported) |
| Blockers | Access, accounts, environment issues |
| Safety | Any anomalies observed; stop conditions invoked? |
| Next window | Areas planned |

## 5. Report template

1. **Executive summary**: the objective, the answer, the top attack path in business terms, overall risk, the three decisions requested.
2. **Scope and coverage**: what was tested, what was not and why, environment differences, methodology followed (PTES, NIST SP 800-115, OWASP WSTG or other).
3. **Findings summary**: table of findings with technical severity and business risk.
4. **Finding detail** (one per finding): title, affected assets, description, business impact, evidence (redacted), reproduction steps for the owning engineering team, technical severity with CVSS v4.0 vector and rationale, business risk with rationale, remediation guidance, references.
5. **Detection observations**: tester activities the SOC did and did not detect.
6. **Appendices**: timeline, tester list, tools categories used, cleanup confirmation.

## 6. Risk acceptance record

| Field | Content |
|---|---|
| Finding and rating | |
| Business owner accepting | |
| Reason | |
| Compensating controls (verified) | |
| Expiry or review date | |
| Approved by (risk committee or CISO) | |

## 7. Vendor engagement scorecard (1-5)

| Criterion | Score | Notes |
|---|---|---|
| Findings validity (few false positives, reproducible) | | |
| Coverage against agreed targets | | |
| Depth (business logic, authorisation, chained impact) | | |
| Report quality and executive summary | | |
| Communication and critical-finding handling | | |
| Readiness of their testers on day one | | |
| Retest quality and timeliness | | |
| Data handling and cleanup | | |
