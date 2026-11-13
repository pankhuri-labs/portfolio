# CS50 companion: adoption and scale-readiness scorecards

Two short self-assessments that go with [CS50](README.md). Score each line 0 (not in place), 1 (partly) or 2 (in place and evidenced). Use them before a purchase or renewal (buyer) and at each planning cycle (vendor).

## 1. Buyer: adoption-readiness scorecard (per tool)

| # | Question | Score 0-2 | Evidence |
|---|---|---|---|
| 1 | Is there a named run owner and an executive sponsor? | | |
| 2 | Is the people time to run the tool (FTE) budgeted alongside the licence? | | |
| 3 | Are two or three outcome KPIs and their baselines agreed? | | |
| 4 | Is coverage measured against a reconciled inventory (assets, repos, cloud accounts, identities)? | | |
| 5 | Was the proof of concept run on our own code, assets and apps, with false-positive rate measured? | | |
| 6 | Are SSO, SCIM, ticketing, SIEM and inventory integrations working, not planned? | | |
| 7 | Do findings arrive in the engineers' workflow (pull requests, IDE, team queue) with an owner and SLA? | | |
| 8 | Is there a tuning plan for the first 90 days? | | |
| 9 | Has an overlapping tool been named for retirement, or a gap proven? | | |
| 10 | Do two people know how to run the tool, with a written runbook? | | |
| 11 | Are licence units modelled for three years, with renewal caps? | | |
| 12 | Are data export, change-of-control and exit terms in the contract? | | |

**Reading the score (out of 24):** 20-24 ready to adopt; 14-19 adopt with a dated plan for the gaps; below 14 fix the operating model before buying or renewing.

## 2. Vendor: scale-readiness scorecard (per product)

| # | Question | Score 0-2 | Evidence |
|---|---|---|---|
| 1 | Is time to first value measured for every new customer? | | |
| 2 | Can a typical customer onboard without vendor engineers (guided setup, onboarding-as-code)? | | |
| 3 | Are open APIs, webhooks and a connector SDK published and versioned? | | |
| 4 | Is connector health monitored, with owners for each connector? | | |
| 5 | Do default policies differ by segment, and is precision tracked per rule? | | |
| 6 | Does consented false-positive and suppression feedback improve detection content? | | |
| 7 | Has the platform been load tested at 10x the largest customer? | | |
| 8 | Are tenant isolation, data residency and customer-managed keys documented and available? | | |
| 9 | Are deployment models (SaaS, private, on-premises, air-gapped) served from one codebase with published parity? | | |
| 10 | Can customers see live usage and forecast licence cost? | | |
| 11 | Is a value milestone instrumented, and are customer success and sales partly rewarded on it? | | |
| 12 | Is there an MSSP mode (multi-tenant console, delegated administration, per-client billing)? | | |
| 13 | Is a trust centre (attestations, SBOM, disclosure policy, incident history) maintained? | | |
| 14 | Are acquired modules integrated at the data and workflow level, not only the console? | | |

**Reading the score (out of 28):** 23-28 ready to scale into large and regulated segments; 16-22 scale in core segments while closing the gaps; below 16 fix onboarding, integrations and adoption measurement before expanding.

## 3. Mutual success plan (one page, agreed at signature)

| Field | Buyer | Vendor |
|---|---|---|
| Named owner | | |
| Executive sponsor | | |
| Inventory and target coverage | | |
| Integrations confirmed | | |
| Outcome KPIs and baseline | | |
| Time-to-first-value milestone and date | | |
| Tuning support until | | |
| Quarterly review dates | | |
| Exit and data-export terms | | |
