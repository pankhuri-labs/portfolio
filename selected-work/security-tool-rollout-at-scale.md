# Rolling out a security platform to thousands of developers in four months

**Role:** AGM and Technology Product Manager, Application Security and Vulnerability Management (Dec 2024 to Sep 2026) · **Organisation:** John Deere

## The situation

The company was replacing an incumbent SAST tool and a home-grown secret scanner. The old tools were noisy and unstable, and developers were frustrated with handoffs. The estate covered tens of thousands of repositories, including citizen developers building automations outside IT. Only about a third of application security findings were being fixed within SLA.

## What I did

- Defined the **evaluation criteria** and ran a time-boxed, phased pilot of secret scanning and code scanning.
- Delivered with a new **12-person AppSec engineering team** built by my engineering manager, and guided the evaluation to a **Go / No-Go recommendation** that leadership approved.
- Planned **rollout batches**, owned the KPIs and the severity-based SLA policy, and built a **security champions network of about 100 people** across departments.
- Worked with developers to harden the CI/CD path: branch protection rules, and access and permissions limited to specific directory groups.
- Handled the hard trade-off: business units that couldn't yet move to the cloud got the tools on the on-premises instance, with an agreed path to migrate.

## The result

- Rolled out in **four months, a month ahead of plan**.
- A **major cut in annual licence cost** from retiring two tools.
- **Near-complete secret-scanning coverage** across repositories, with **hundreds of secrets blocked** by push protection, and **near-complete repository coverage** in the targeted departments.
- Findings fixed within SLA **roughly doubled**.
- The rollout won the company's annual **CISO Award**, and the method became the template for the endpoint protection platform rollout.

## What I'd tell another security leader

If adoption of a security tool has stalled, the problem is rarely the tool. It's the rollout plan, the ownership and the metrics.

Deeper write-up: [Scaling a code-scanning platform across a large enterprise](../case-studies/CS35-GitHub-Advanced-Security-Enterprise-Rollout/README.md)

[← Back to portfolio](../README.md)
