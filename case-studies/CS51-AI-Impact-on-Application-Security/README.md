# CS51: AI's Impact on Application Security: Problems, Root Causes and Opportunities for Product and Services Organisations

Domain: All sectors; SaaS, BFSI, Healthcare, Public sector, Manufacturing, IT services, MSSPs and AppSec tool vendors · Org type: both

> **Point of view.** AI is changing application security from five directions at once: AI **writes** a growing share of the code, AI **agents run inside the toolchain** with access to repositories and pipelines, AI **features ship inside the application**, attackers **use AI** to find and weaponise flaws faster, and defenders **use AI** to triage, fix and test. This case study looks at what that means for two kinds of organisation: **product organisations** that build and ship their own software, and **services organisations** (IT services firms, system integrators, MSSPs, testing and consulting firms) that build, test or run software for clients. For each it lists the problem statements, the root cause behind each one and recommended next steps, then the **opportunities** and **five key actions**. Problems and opportunities are kept separate for the two sides because the same shift lands differently: for a product firm it is a change in how its own software is built; for a services firm it also changes what clients will pay for.
>
> Vendor-neutral and methodology-level. Products and models are named only where a public event or study is the example, and every figure carries its date. Companion file: [ai-appsec-readiness-checklist.md](ai-appsec-readiness-checklist.md) with a guardrail checklist for AI-assisted development and an AI service-line readiness checklist for services firms.
>
> What this case study adds to earlier ones: securing LLM and agent features inside an application is covered in CS04; governing client data in AI tools in CS15; AI agent identities in CS36; AI coding volume as one driver of AppSec debt in [CS25](../CS25-AppSec-Debt-and-Developer-Ratio/README.md). None of them looks at AI's effect on the whole AppSec discipline, on both sides of the market, and on where the new work is. That is this case study.

## In plain business terms (for readers outside IT)

**The short version.** AI has given every software team a very fast junior developer who never tires, is confident even when wrong, and will follow instructions hidden in anything it reads. It has given attackers the same assistant. Teams now produce code faster than they can check it, attackers turn published fixes into working attacks faster than teams can patch, and the security tools themselves are being rebuilt around AI. Organisations that put guardrails around the fast junior developer gain speed safely; those that do not are shipping more flaws, faster.

| Side | The change, in business terms | It is like... | The question to ask |
|---|---|---|---|
| Product organisation | Half the code may now be drafted by AI, and reviews have not grown to match | A factory that doubled its line speed without adding inspectors | "What share of our code is AI-written, and does it get the same checks?" |
| Product organisation | AI coding agents hold keys to our code and build systems | Giving a temp worker the master key on day one | "What can our coding agents reach, and who approved that?" |
| Both | Attackers use AI to turn a public fix into an attack within days | Burglars who now get the locksmith's notes the day the lock is changed | "How fast do we patch something that is actively exploited?" |
| Services organisation | Clients expect AI to make delivery and testing cheaper | A client asking why a report still takes ten days when a machine drafts it in one | "Which of our services are priced on effort that AI is removing?" |
| Services organisation | Clients want proof that AI used on their code is safe and allowed | A contractor asked to show which subcontractors touched the building | "Can we show each client which AI tools touched their code and data?" |

**Three decisions for a board or owner**

1. **Treat AI-written code as untrusted input until checked.** Same tests, same scans, same review as any other code, and measure the defect rate separately.
2. **Give AI agents the least access that works, and log everything they do.** An agent with repository and pipeline credentials is a new privileged identity.
3. **Fund the response speed, not just the scanner.** When attackers move in days, the gap that matters is time to patch exploited flaws.

## 1. Problem statement

**Product organisations.** Developers now generate a large share of code with AI assistants and, increasingly, autonomous coding agents. Independent testing finds that AI-generated code still introduces a known class of vulnerability in about four in ten tasks, with no real improvement across model generations. Code review, threat modelling and AppSec headcount were sized for human output. Coding agents act with the developer's credentials across repositories, package registries and CI/CD, and can be steered by instructions hidden in issues, documents, dependencies or tool descriptions. At the same time, attackers use AI to find new flaws and weaponise published patches faster, so the window between disclosure and exploitation is shrinking while disclosure volume is doubling. Security teams are offered AI triage, autofix and AI pentesting, but have no way yet to measure whether these tools reduce risk or just move noise around.

**Services organisations.** IT services firms and system integrators deliver client code with AI assistants under contracts that never anticipated it: who is accountable for an AI-introduced flaw, which AI tools are allowed on which client's code, and how that is evidenced. Testing, code review and managed AppSec services priced on analyst effort face clients who expect AI to make them cheaper, while AI-generated noise (low-quality findings and bug reports) raises triage cost. Junior roles that built the talent pipeline (first-line triage, manual code review, basic testing) are the ones AI absorbs first. Services firms also run AI tools and agents across many client estates, which multiplies the blast radius of one compromised agent or extension.

The question this case study answers: **how is AI changing application security for product and services organisations, what are the problems and their root causes, and where are the opportunities?**

## 2. Why now

| Driver | What happened | Effect on AppSec |
|---|---|---|
| **AI writes much of the code** | Stack Overflow Developer Survey (29 Jul 2025): **84%** of developers use or plan to use AI tools, up from 76%; **46%** distrust the accuracy of AI output, up from 31%. Veracode's 2026 GenAI Code Security Report (28 Jul 2026) cites roughly half of committed code as AI-assisted (from a DX survey) | Code volume rises faster than review capacity; trust is falling even as use rises |
| **AI code security is not improving with model size** | Veracode 2026 report (28 Jul 2026): AI code generation introduced a known vulnerability in about **44%** of tasks; average security pass rate moved only from 55% (2025) to 56%; pass rates for cross-site scripting (15%) and log injection (12%) remain very low | Better models do not fix the problem by themselves; guardrails must sit in the pipeline |
| **Hallucinated dependencies** | Spracklen et al., "We Have a Package for You!" (USENIX Security 2025): across 576,000 code samples from 16 models, recommended packages that did not exist made up at least **5.2%** for commercial models and **21.7%** for open-source models, giving 205,474 unique invented names that attackers can register ("slopsquatting") | AI adds a new supply-chain path that classic SCA does not catch, because the package is new rather than vulnerable |
| **Coding agents and AI tools became the target** | Malicious prompt inserted into the Amazon Q Developer VS Code extension 1.84.0 (Jul 2025); prompt-injection remote code execution in GitHub Copilot and VS Code (CVE-2025-53773, patched Aug 2025); malicious Nx package versions (26 Aug 2025, "s1ngularity") used AI command-line tools on developer machines to hunt for secrets; an AI coding agent deleted a production database during a code freeze at SaaStr (Jul 2025) | The developer's AI tooling is now part of the attack surface and an over-privileged actor in its own right |
| **AI-related software is a large new vulnerability class** | Google Threat Intelligence Group, reported 1 Oct 2026: **2,076** vulnerabilities in AI-related software from Jan 2025 to Aug 2026, over 1,500 of them in 2026, half in agent orchestration frameworks; exploited examples include Langflow (CVE-2025-3248) and LiteLLM (CVE-2026-42271). OWASP published the Top 10 for Agentic Applications on 9 Dec 2025 | AppSec scope now includes agent frameworks, model servers and MCP servers, often deployed by teams outside engineering |
| **Attackers move faster** | Same GTIG analysis: monthly CVE disclosures doubled in 2026 (5,045 in Jan to 10,740 in Aug); **141** exploited vulnerabilities in Jan-Aug 2026 versus 127 in all of 2025; GTIG suggests attackers use AI to weaponise patches and proof-of-concept code. Anthropic reported (Nov 2025) disrupting a state-sponsored espionage campaign (GTG-1002) in which an AI agent framework performed most of the tactical intrusion work | Patch windows shrink; volume-based triage breaks; exploitation evidence ([CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md)) matters more than ever |
| **AI finds vulnerabilities at scale, for both sides** | DARPA AI Cyber Challenge final (Aug 2025): autonomous systems found and patched synthetic flaws and real zero-days in open source; an AI system reached the top of HackerOne's US leaderboard (Jun 2025); Anthropic's Project Glasswing (7 Apr 2026) gave a restricted model to critical-software maintainers, who reported more than **10,000** vulnerabilities within weeks (May 2026). GTIG: 50% of likely AI-found vulnerabilities lead to remote code execution versus 26% of others | Discovery is no longer the bottleneck; remediation capacity and patch distribution are |
| **AI noise hits the disclosure system** | curl ended its bug bounty at the end of January 2026 after a flood of low-quality, largely AI-generated reports | Maintainers and PSIRTs need triage that can separate real reports from generated ones |
| **Regulation expects evidence** | EU Cyber Resilience Act reporting of actively exploited vulnerabilities from 11 Sep 2026; EU AI Act obligations phasing in since Feb 2025; CISA Secure by Design pledge; client and regulator questionnaires now ask about AI use in development | AI-assisted development must still produce the SBOM, the vulnerability handling and the evidence the law asks for |

## 3. Pain points addressed

| Product organisations | Services organisations |
|---|---|
| PP-P-49 (new) AI-generated code arrives faster than review, testing and threat modelling can absorb it, with a stable flaw rate, hallucinated dependencies and no way to tell which code was AI-written | PP-S-44 (new) client code delivered with AI assistants under contracts silent on AI accountability, approved tools and evidence; one compromised AI tool or agent reaches many client estates |
| PP-P-50 (new) AI coding agents and AI tooling (assistants, IDE extensions, MCP servers, agent frameworks) act with developer and pipeline privileges, are steerable by untrusted content, and sit outside the AppSec inventory | PP-S-45 (new) effort-priced testing, review and managed AppSec services face AI-driven price pressure and AI-generated noise, while the junior roles that built the talent pipeline shrink |
| PP-P-07 AI features and AI-generated code without threat models | PP-S-06 AI-assisted delivery with different data rules per client |
| PP-P-01 scanner noise; developers stop trusting findings | PP-S-05 skills shortage; junior analysts triage without context |
| PP-P-03 SBOM and supply-chain transparency demanded by customers and law | PP-S-07 clients requesting AI governance evidence |

---

## Part A: Product organisations

### A.1 Problem statements, root causes and recommended next steps

| # | Problem statement | Root cause | Recommended next steps |
|---|---|---|---|
| A1 | **AI-generated code ships with the same flaw classes, faster.** Injection, cross-site scripting, missing authorisation and weak crypto appear in AI output at a steady rate, and volume is rising. | Models reproduce patterns from public code, which contains the same flaws; prompts rarely state security requirements; review capacity was sized for human output. | Treat AI output as untrusted: same SAST, SCA, secrets and tests on every change; add secure-coding instructions and organisation rules files to assistants; prioritise rules for the classes AI handles worst (XSS, log injection, authorisation). Measure the defect rate of AI-assisted changes separately. |
| A2 | **Hallucinated and unvetted dependencies.** Assistants and agents add packages that do not exist (and may later be registered by attackers) or that are unmaintained. | AI suggests names by likelihood, not by registry lookup; package installs by agents bypass human judgement; SCA looks for known-vulnerable packages, not new or suspicious ones. | Route installs through an internal registry proxy with an allow-list or age and reputation checks; block packages younger than an agreed age; alert on first-seen dependencies in pull requests (CS32, CS48). |
| A3 | **Coding agents hold too much privilege.** Agents run with the developer's tokens, can push code, change pipelines, read secrets and run shell commands, sometimes without per-action approval. | Agent tools default to convenience; agent identity is the human's identity; no policy distinguishes "suggest" from "act". | Give agents their own scoped identities and short-lived tokens; require human approval for pushes to protected branches, pipeline changes and production access; sandbox agent execution; log agent actions to the SIEM (CS36, CS12). |
| A4 | **Prompt injection reaches the developer toolchain.** Instructions hidden in issues, pull request text, documentation, dependencies or MCP tool descriptions steer assistants into leaking secrets or running commands. | The model cannot reliably separate instructions from data; agents combine private data, untrusted content and the ability to act (CS04). | Break the combination: no agent that reads untrusted content may also act with write or network access without approval; approve and pin MCP servers and IDE extensions; turn off auto-execute modes on sensitive repositories. |
| A5 | **AI tooling sits outside the AppSec inventory.** Teams deploy agent frameworks, model servers, vector databases and MCP servers without a security review, and these are now a large, exploited vulnerability class. | AI components are adopted by data and product teams outside the normal intake; no AI bill of materials. | Add AI components to the asset and SBOM inventory (AI-BOM); include agent frameworks and model servers in VM scanning and patch SLAs; put AI components through design review triage ([CS25](../CS25-AppSec-Debt-and-Developer-Ratio/README.md)). |
| A6 | **Review becomes rubber-stamping.** Larger, AI-drafted pull requests get approved without real reading; reviewers trust confident code. | Review norms built for small human changes; no signal of which code was generated; productivity targets reward merge speed. | Cap pull request size; label AI-assisted changes; require tests with every AI change; use AI review as a first pass, never as the only approver on security-relevant paths. |
| A7 | **Patch windows shrink while disclosures double.** Exploits for published fixes appear within days; CVE volume overwhelms severity-based triage. | Attackers use AI to diff patches and adapt proof-of-concept code; triage still sorted by CVSS. | Prioritise by exploitation evidence and reachability (KEV, EPSS, threat intelligence); set emergency SLAs for exploited flaws in internet-facing components; automate dependency upgrades with tests ([CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md)). |
| A8 | **AI defence tools are adopted without proof.** AI triage, autofix and AI pentest tools promise large reductions in work, but nobody measures false negatives or fix quality. | Vendor claims outrun independent benchmarks; buyers measure findings closed, not risk removed. | Pilot on your own code with a labelled set of known flaws; measure precision, recall and fix rescan-pass rate; keep humans on high-risk fixes; track the defect rate of AI fixes over time ([CS50](../CS50-Security-Tool-Adoption-and-Vendor-Scaling/README.md)). |
| A9 | **Inbound vulnerability reports become noisy, and real ones arrive faster.** PSIRT and bug bounty queues fill with generated reports, while genuine AI-found flaws arrive in batches. | Low cost of generating reports; no proof-of-concept requirement; PSIRT staffed for a trickle. | Require reproducible proof of concept; triage with AI plus human confirmation; publish a clear disclosure policy; plan PSIRT capacity for batch disclosures and CRA reporting clocks. |
| A10 | **Evidence and accountability gaps.** Customers, auditors and regulators ask how AI is used in development; the organisation cannot show which code, which tools or which controls. | AI use spread bottom-up; no policy, no telemetry, no link between AI use and the secure development framework. | Write an AI-assisted development policy mapped to NIST SSDF and CISA Secure by Design; record approved tools and settings; keep provenance (commit trailers or tool telemetry) for AI-assisted changes; include AI controls in the trust centre (CS33). |

### A.2 Deep dive: the root causes behind the root causes

1. **Speed was automated; judgement was not.** AI multiplies output, but security review, threat modelling and accountability remain human and were not scaled.
2. **Agents collapse the boundary between reading and acting.** Classic AppSec assumed code is written by a trusted human and data is passive. A coding agent reads untrusted text and then acts with real privileges, so injection becomes an SDLC risk, not only an application risk.
3. **Identity and inventory lag adoption.** AI tools, agents and AI components enter through developers and data teams, outside procurement and outside the asset inventory, so they are neither scanned nor governed.
4. **Discovery is cheap; fixing is not.** AI makes finding flaws cheaper for attackers, researchers and defenders alike. The bottleneck moves to remediation capacity, patch distribution and prioritisation.

### A.3 Domain notes for product organisations

| Domain | What is different |
|---|---|
| **SaaS and technology** | Highest AI coding adoption and agent use; continuous deployment means AI changes reach production quickly. Guardrails must live in the pipeline and the paved road, not in policy documents |
| **BFSI** | Model risk and outsourcing rules (RBI, DORA ICT third-party register) apply to AI coding tools as suppliers; regulators expect change control evidence that names the author, which AI-assisted commits complicate |
| **Healthcare and MedTech** | FDA premarket cybersecurity expectations (SBOM, secure development) apply whether code was AI-written or not; hallucinated dependencies in device software are a patient-safety and recall risk (CS28) |
| **Manufacturing, IoT and automotive** | Long-lived firmware cannot be patched in days, so AI-accelerated exploitation hurts most here; secure defaults and memory-safe choices matter more than patch speed |
| **Public sector platforms** | Procurement increasingly asks for secure-by-design attestations and AI-use disclosure; sovereign hosting rules narrow which AI tools may touch the code |
| **AppSec tool vendors** | The product category itself is being rebuilt around AI (triage, autofix, agentic review, AI pentesting). Vendors must prove accuracy on customer code, not on demos, and secure their own AI features against injection |

### A.4 Opportunities for product organisations

| # | Opportunity | What it looks like | Who benefits |
|---|---|---|---|
| P-O1 | **Secure AI-assisted development as a paved road** | Approved assistants with organisation rules files, pre-commit and pull request scanning, registry proxy, agent sandboxes and provenance, offered as the easiest path for developers | Engineering speed with fewer escaped flaws; audit evidence for free |
| P-O2 | **AI-assisted remediation at scale** | Autofix pull requests for well-understood classes (dependency upgrades, injection, encoding) with rescan and tests; backlog burn-down that was impossible by hand | AppSec debt falls; developer time moves to design ([CS25](../CS25-AppSec-Debt-and-Developer-Ratio/README.md)) |
| P-O3 | **AI-augmented threat modelling and design review** | Assistants draft threat models from design documents and architecture diagrams; AppSec engineers review instead of starting from blank | More designs reviewed by the same team; Tier 1 reviews done by champions |
| P-O4 | **Continuous AI-assisted testing of own products** | AI fuzzing harness generation, agentic code review and AI-driven testing between annual pen tests, with human validation | Flaws found before attackers do; pen tests focus on business logic ([CS47](../CS47-Penetration-Testing-Programme-Management/README.md)) |
| P-O5 | **Agent and AI-tool security products** (for AppSec vendors and platform teams) | MCP gateways and allow-lists, agent permission brokers, AI-BOM generation, slopsquatting-aware package firewalls, AI code provenance and AI-change risk scoring | A new product category with active buyer demand; extends ASPM and supply-chain products |
| P-O6 | **Memory-safe and secure-by-default rewrites made affordable** | AI-assisted migration of risky components to memory-safe languages or safer frameworks, with tests to prove equivalence | Removes whole vulnerability classes rather than individual bugs |

### A.5 Key 5 actions for product organisations

| # | Action | What it looks like in practice | Measure of success |
|---|---|---|---|
| 1 | **Make AI code pass the same gates, and measure it separately** | Every change, AI or not, goes through SAST, SCA, secrets scanning and tests; AI-assisted changes are labelled; rules tuned for the classes AI gets wrong | Escaped-defect rate of AI-assisted changes equal to or lower than human changes |
| 2 | **Put a registry proxy between agents and package ecosystems** | Internal proxy with allow-list or age and reputation checks; first-seen dependency alerts in pull requests | Zero installs of packages younger than the agreed age or not in the registry |
| 3 | **Govern coding agents as privileged identities** | Own identities, short-lived scoped tokens, human approval for protected actions, sandboxed execution, approved MCP servers and extensions, full action logging | 100% of agents with scoped identity; no agent with standing production or pipeline-admin access |
| 4 | **Prioritise by exploitation and shrink time to patch** | KEV, EPSS and threat intelligence drive SLAs; automated dependency upgrades with tests; AI components included in VM | Median time to remediate exploited flaws in internet-facing apps below the agreed SLA (for example 7 days) |
| 5 | **Adopt AI defence tools on evidence** | Benchmark on own code with known flaws; track precision, recall and fix rescan-pass rate; humans on high-risk fixes; quarterly keep, fix or retire review | AI autofix rescan-pass rate above 95%; measured reduction in mean time to remediate |

---

## Part B: Services organisations

### B.1 Problem statements, root causes and recommended next steps

| # | Problem statement | Root cause | Recommended next steps |
|---|---|---|---|
| B1 | **Contracts are silent on AI in delivery.** Who is liable for a flaw introduced by an AI assistant; which tools are allowed on which client's code; whether client code may train or be retained by a model. | Master services agreements predate AI coding; delivery teams adopted tools before legal and clients agreed rules. | Add an AI-in-delivery schedule to contracts: approved tools and settings, data retention and training terms, disclosure, accountability for defects regardless of authoring tool, and evidence on request (CS15). |
| B2 | **Per-client AI rules cannot be enforced at scale.** One client bans AI on its code, another allows only a private deployment, another requires disclosure. | Policies live in contracts, not in tooling; engineers move between engagements; personal tool accounts. | Enforce per-engagement AI policy in tooling: managed assistant licences tied to client workspaces, policy-as-code in IDE and repository settings, blocked personal accounts on client devices, audit logs per client. |
| B3 | **One compromised AI tool reaches many clients.** A malicious IDE extension, poisoned MCP server or compromised agent runs on laptops that hold access to many client repositories. | Shared tooling and shared engineers across engagements; extension and MCP sprawl; standing access to several clients from one machine. | Approved extension and MCP catalogue; separate workspaces or virtual desktops per client; short-lived, per-client credentials; detection for agent misuse across the delivery fleet (CS11). |
| B4 | **AI-written client code carries the provider's reputation.** Delivery teams under fixed-price pressure accept AI output with light review; defects surface after handover. | Margin pressure rewards speed; quality gates are the client's, not the provider's; no measurement of AI defect rates per team. | Provider-side quality gates on every delivery (scanning, tests, secure review on high-risk paths); report AI-assisted share and defect rates to the client as a quality metric. |
| B5 | **Effort-based pricing breaks.** Clients expect AI to make code review, testing and VM services cheaper; time-and-materials and day-rate testing lose value. | Pricing tied to analyst hours; AI removes hours from routine work; competitors and AI-native start-ups price on outcome. | Re-package services around outcomes (risk reduced, time to remediate, coverage) and continuous delivery; price per application or per outcome tier; keep human expertise for business logic, design review and validation. |
| B6 | **AI noise raises triage cost.** AI scanners, AI pentest tools and generated reports produce more findings; clients still expect validated, low-noise output. | Tools tuned for recall; no shared validation step; analysts overwhelmed. | Make human validation of AI findings a named service step; reusable tuning and suppression libraries per sector; report validated findings and false-positive rates to clients. |
| B7 | **The junior talent pipeline shrinks.** First-line triage, manual review and basic testing (the work juniors learned on) is automated first. | Delivery models built a pyramid of juniors doing repetitive work; no new route from novice to expert. | Redesign the pyramid: juniors supervise and validate AI output, run red-team exercises against AI tools and learn design review earlier; certify skills in AI-assisted testing and agent security. |
| B8 | **Clients ask for AI security services the firm cannot yet staff.** AI red teaming, agent security reviews, AI-BOM and AI governance assessments. | Skills are new; methodologies (OWASP LLM and Agentic Top 10, NIST AI RMF, ISO/IEC 42001) are recent. | Build a small centre of excellence; standard methodology mapped to OWASP and NIST; reusable test cases; partner with AI security vendors; train existing AppSec testers rather than hiring only new (CS04). |
| B9 | **Managed VM and AppSec services drown in volume.** Doubling disclosures and AI-found flaws inflate every client's backlog. | Service SLAs written per finding or per CVSS band; no exploitation-based prioritisation in the service. | Rewrite service SLAs around exploitation and exposure; use AI triage with human confirmation; offer emergency patch response for exploited flaws as a premium tier ([CS01](../CS01-Exploit-Driven-Vulnerability-Prioritization/README.md), CS02). |
| B10 | **Evidence for client audits and regulators.** Client regulators (DORA, RBI, SEBI, CRA for client products) ask the provider how AI was used and controlled. | No per-client record of AI use; controls not mapped to client frameworks. | Maintain a per-client AI use register and evidence pack (tools, settings, scans, review, defect rates) aligned to the client's framework; include it in service reporting (CS33). |

### B.2 Deep dive: the root causes behind the root causes

1. **The contract and the tooling disagree.** Rules about AI live in documents, while engineers work in tools that do not know which client they are serving.
2. **Shared people and machines multiply blast radius.** Services firms reuse engineers, laptops and tooling across clients, so one compromised AI tool is a multi-client incident.
3. **The business model sells hours that AI removes.** Routine testing and triage are the most automatable work and often the most profitable; firms that do not re-price will be undercut.
4. **Expertise moves up the stack.** Value shifts from finding flaws to judging them: validation, business-logic testing, design review, AI system testing and remediation leadership.

### B.3 Domain notes for services organisations

| Domain | What is different |
|---|---|
| **IT services and application development** | Largest exposure to AI-written client code and per-client AI rules; strongest case for AI-in-delivery contract schedules and workspace separation |
| **Testing and pen-testing firms** | AI pentest and AI code review compress routine testing; value moves to business logic, chained attacks, AI system testing and validation ([CS47](../CS47-Penetration-Testing-Programme-Management/README.md)) |
| **MSSPs and managed VM providers** | Disclosure volume and faster exploitation change SLAs; AI triage helps only with human confirmation and exploitation-based priorities |
| **System integrators** | Deploy agent platforms, model servers and MCP integrations for clients, often first; must bring secure reference architectures and own the patching of AI components they install |
| **BPO and contact centres** | Agents and AI copilots touch client customer data; overlaps with CS15 data rules and CS40 oversharing |
| **BFSI and public-sector clients** | Regulators treat the AI tool provider as a sub-outsourcing; providers need named tools in the client's third-party register and exit plans |

### B.4 Opportunities for services organisations

| # | Opportunity | What it looks like | Typical buyer |
|---|---|---|---|
| S-O1 | **Secure AI-assisted SDLC enablement** | Assess and roll out guardrails for AI coding (rules files, scanning gates, registry proxy, agent identity, provenance) as a fixed-scope programme | Product companies and enterprise IT with fast AI coding adoption |
| S-O2 | **AI and agent red teaming and security review** | Test AI features, agents, MCP servers and coding agents against OWASP LLM and Agentic Top 10; recurring rather than one-off | SaaS, BFSI, healthcare, public sector |
| S-O3 | **AI-augmented managed AppSec and VM** | Continuous scanning plus AI triage and autofix with human validation, priced per application or outcome; emergency response for exploited flaws | Mid-size firms without an AppSec team; enterprises consolidating vendors |
| S-O4 | **AI governance and evidence services** | AI-use policy, AI-BOM, ISO/IEC 42001 and EU AI Act readiness, AI controls in trust centres and questionnaires | Regulated clients and product vendors facing customer questionnaires |
| S-O5 | **AI-assisted legacy remediation and modernisation** | Use AI to upgrade end-of-life frameworks, migrate to memory-safe components and burn down AppSec debt, with tests and human review | Clients with large legacy estates (CS31, CS48) |
| S-O6 | **Secure AI platform integration** | Reference architectures for deploying agent frameworks, model servers and MCP gateways, including patching and monitoring as a managed service | Enterprises adopting agent platforms |
| S-O7 | **PSIRT and disclosure triage as a service** | Triage of inbound vulnerability reports (including AI-generated ones), reproduction, CRA reporting support | Product vendors and open-source foundations |

### B.5 Key 5 actions for services organisations

| # | Action | What it looks like in practice | Measure of success |
|---|---|---|---|
| 1 | **Write AI into every client contract** | AI-in-delivery schedule: approved tools, data terms, disclosure, accountability, evidence | 100% of new and renewed contracts with an AI schedule |
| 2 | **Enforce per-client AI policy in tooling** | Managed licences per client workspace, policy-as-code, separate workspaces, approved extension and MCP catalogue, per-client audit logs | No personal AI accounts on client code; per-client AI use register complete |
| 3 | **Own the quality of AI-assisted delivery** | Provider-side gates on every delivery; AI-assisted share and defect rate reported to clients | Post-handover security defects per release falling |
| 4 | **Re-package services around outcomes and validation** | Outcome-priced managed AppSec and VM; human validation of AI findings as a named step; premium emergency response | Share of revenue from outcome or subscription services rising; client-reported false-positive rate falling |
| 5 | **Build AI security skills and a new talent pyramid** | Centre of excellence for AI red teaming and agent security; juniors trained to validate and supervise AI output | Certified AI security practitioners per delivery unit; utilisation of AI security services |

---

## 4. The AI impact map across the software life cycle

| Life-cycle stage | How AI helps | How AI hurts | Control that matters most |
|---|---|---|---|
| Design | Drafts threat models and security requirements | Designs for AI features skip abuse cases | Design review triage with an AI and agent trigger |
| Code | Writes code fast; suggests fixes | Reproduces flaw classes; invents packages | Same gates for AI code; registry proxy |
| Review | First-pass AI review at scale | Large AI pull requests rubber-stamped | Size limits; labelled AI changes; humans on security paths |
| Build and CI/CD | Automated upgrades and tests | Agents with pipeline privileges; injection via repository content | Scoped agent identities; approval for pipeline changes |
| Test | AI fuzzing, AI pentesting, harness generation | Noise and unvalidated findings | Benchmarked tools; human validation |
| Release and run | Faster patch creation | Attackers weaponise patches in days | Exploitation-based SLAs; fast patch path |
| Disclosure | AI triage of inbound reports | Floods of generated reports; batch discoveries | Proof-of-concept requirement; PSIRT capacity |

## 5. Where product and services organisations meet

Most AI-related AppSec failures between a product company and its services provider come from unstated assumptions. A short **AI delivery agreement** aligns both sides:

| Element | Product organisation (client) commits | Services organisation (provider) commits |
|---|---|---|
| Tools | Lists approved AI tools and settings for its code and data | Uses only those, through managed per-client accounts |
| Quality | Shares its security gates and definitions of done | Runs equivalent gates before handover; reports AI-assisted share and defect rate |
| Agents | Defines what agents may access and approve | Uses scoped, per-client agent identities with logging |
| Evidence | States audit and regulator evidence needs | Maintains a per-client AI use register and evidence pack |
| Incidents | Shares relevant threat intelligence | Notifies the client of any AI tool compromise affecting its estate within an agreed time |
| Commercials | Agrees outcome measures | Prices on outcomes, not hours AI has removed |

## 6. 90-day plans

| Days | Product organisation | Services organisation |
|---|---|---|
| 0-30 | Inventory AI coding tools, agents, MCP servers and AI components; label AI-assisted changes; confirm all code passes the same gates; publish an AI-assisted development policy | Inventory AI tools used per client; draft the AI-in-delivery contract schedule; block personal AI accounts on client code; pick two pilot service offers (for example AI red teaming and AI-augmented managed AppSec) |
| 31-60 | Deploy a registry proxy with age and reputation checks; give coding agents scoped identities and approval steps; benchmark one AI triage or autofix tool on own code | Enforce per-client policy in tooling for the top ten clients; launch provider-side delivery gates; train a first cohort in AI and agent security testing |
| 61-90 | Exploitation-based SLAs including AI components; AI autofix pilot on two flaw classes with rescan and tests; first report on AI-assisted defect rates | Sign the first outcome-priced managed AppSec contract; publish an AI security methodology mapped to OWASP and NIST; first client evidence packs |

## 7. KPIs

| Product organisation | Services organisation |
|---|---|
| Share of code AI-assisted, and its escaped-defect rate versus human code | Share of clients with an AI schedule in the contract |
| First-seen and blocked package installs per month | Per-client AI use register completeness |
| Coding agents with scoped identity and approval steps (%) | Post-handover security defects per release |
| Median time to remediate exploited flaws in internet-facing apps | Validated-finding rate and false-positive rate in AI-assisted services |
| AI autofix rescan-pass rate and reviewer acceptance rate | Revenue share from outcome or subscription services |
| AI components (frameworks, model servers, MCP servers) covered by VM | Certified AI security practitioners per delivery unit |
| PSIRT time to triage inbound reports | Time to notify clients of AI tool compromise |

## 8. Risks and how to handle them

| Risk | Mitigation |
|---|---|
| AI guardrails slow developers, who switch to personal tools | Make the approved path the fastest; measure friction; block personal accounts only after the approved path works |
| Labelling AI-assisted code is incomplete | Use tool telemetry where available and commit trailers by default; treat all code as untrusted anyway |
| AI autofix introduces new flaws or breaks behaviour | Rescan, tests and human review on every AI fix; stop the pilot if rescan-pass rate drops |
| Over-reliance on AI review misses business-logic flaws | Keep human review and testing on authorisation, payments and multi-tenant paths |
| Services re-pricing reduces revenue before new services grow | Phase the change; launch AI security services alongside; price on outcomes that clients value |
| AI vulnerability discovery floods teams with valid findings | Prioritise by exploitation and exposure; fund remediation capacity, not only discovery |
| Facts and tools change monthly | Review this case study and its checklist quarterly; date every figure |

## 9. Learnings

1. **AI changes the speed of everything, not the nature of the flaws.** The same classes of vulnerability appear, more often and faster.
2. **AI-written code is untrusted input.** Same gates, separate measurement.
3. **Coding agents are privileged identities.** Scope them, approve their risky actions and log them.
4. **Discovery got cheap; remediation is the bottleneck.** Invest in prioritisation by exploitation and in fast, safe patching.
5. **For product firms the opportunity is speed with guardrails; for services firms it is new services and new pricing.** Both require evidence that AI use is controlled.
6. **Services firms carry multi-client blast radius.** Per-client separation of AI tools, credentials and policy is the services-specific control.
7. **The talent pyramid must be redesigned, not abandoned.** Juniors learn by validating and supervising AI, not by doing what AI now does.

## References

- Veracode, "2026 GenAI Code Security Report" (28 Jul 2026): https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk
- Stack Overflow, 2025 Developer Survey press release (29 Jul 2025): https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
- Spracklen et al., "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs", USENIX Security 2025: https://arxiv.org/abs/2406.10279
- Help Net Security, "The vulnerabilities AI finds are the ones attackers want" (1 Oct 2026), summarising Google Threat Intelligence Group research: https://www.helpnetsecurity.com/2026/10/01/google-ai-discovered-vulnerabilities-remote-code-execution/
- Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign" (Nov 2025), reported by eSecurity Planet: https://www.esecurityplanet.com/threats/inside-the-first-ai-driven-cyber-espionage-campaign/
- Anthropic, Project Glasswing (7 Apr 2026), reported by VentureBeat: https://venturebeat.com/data/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release
- Engadget via AITopics, "Anthropic says Mythos has already found more than 10,000 vulnerabilities" (May 2026): https://aitopics.org/doc/news:7ABD45C3
- The Register, "curl ends bug bounty" (21 Jan 2026): https://theregister.com/2026/01/21/curl_ends_bug_bounty
- OWASP GenAI Security Project, Top 10 for Agentic Applications for 2026 (Dec 2025): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
- OWASP Top 10 for LLM Applications: https://genai.owasp.org/llm-top-10/
- DARPA, AI Cyber Challenge (AIxCC): https://aicyberchallenge.com/
- NIST SP 800-218 Secure Software Development Framework (SSDF): https://csrc.nist.gov/pubs/sp/800/218/final
- NIST AI Risk Management Framework and Generative AI Profile (NIST AI 600-1): https://www.nist.gov/itl/ai-risk-management-framework
- CISA, Secure by Design: https://www.cisa.gov/securebydesign
- CISA, Known Exploited Vulnerabilities Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- Regulation (EU) 2024/2847, Cyber Resilience Act: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- Regulation (EU) 2024/1689, Artificial Intelligence Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- ISO/IEC 42001:2023, AI management systems: https://www.iso.org/standard/81230.html
