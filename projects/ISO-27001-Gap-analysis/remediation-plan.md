# Remediation programme — proposed, not implemented

**Programme owner: COO | Review: weekly for P1, monthly thereafter | Baseline: 14 September 2026**

## Delivery workstreams

| Workstream | Key action references | Sequence and dependency | Owner | Planning effort | Success condition |
| --- | --- | --- | --- | --- | --- |
| Governance and ownership | ACT-5.1, 5.2, 5.9, 5.31, 5.36 | Approve scope, owners and rules before broad compliance reporting | Security Lead | 15 staff-days | Owned assets, approved rules and first evidence-based review |
| Identity and endpoint containment | ACT-5.16–5.18, 8.1, 8.2, 8.5, 8.7 | Inventory identities/devices; fix stale access; enforce MFA; test recovery | IT Manager | 20 staff-days | No orphaned active access; all endpoints controlled; authentication tests pass |
| Customer and HR data protection | ACT-5.12–5.14, 5.34, 8.10–8.12 | Classify stores; restrict sharing; remove test copies; implement deletion | Privacy Lead | 18 staff-days | Synthetic handling and deletion tests pass |
| Response and resilience | ACT-5.24–5.30, 8.13–8.16 | Contact routes and protected logs first; restore and tabletop next | Security Lead / Engineering | 25 staff-days | Out-of-hours response and timed restoration independently observed |
| Supplier assurance | ACT-5.19–5.23, 8.30 | Tier suppliers; obtain evidence; resolve contract blockers before onboarding | Procurement Lead | 12 staff-days | Critical supplier decisions have evidence, conditions and owners |
| Secure engineering | ACT-5.3, 8.8, 8.9, 8.25–8.34 | Stabilise vulnerability/configuration management; enforce delivery gates | Head of Engineering | 30 staff-days | A release demonstrates separation, security tests and rollback |
| People and office assurance | ACT-6.1–6.8, 7.1–7.14 | Close urgent media/disposal risks, then induction and physical process checks | People / Facilities Leads | 15 staff-days | Sampled workforce and office processes meet approved rules |

Total planning effort: 135 internal staff-days across 180 days; assumptions need owner validation. Initial external/tool allowance: £35,000 implementation plus £2,000/month recurring, inclusive of the policy suite's overlapping allowance. These are scenario estimates, not quotations. Finance must avoid double counting shared technology and obtain actual costs before spending. The action register is the authoritative item-level scope; ranges above are navigation shorthand.

## First 30 days

Within 48 hours, the IT Manager should remove the two fictional stale employee accounts and the departed contractor's repository access; rotate the exposed deployment secret; restrict unmanaged-device access; preserve relevant logs. These are proposed urgent actions, not completed changes.

By day 7, assign data and service owners, reconcile privileged identities, establish on-call response and block unapproved public customer-data links. Engineering should isolate any actively exploited exposure pending a fix. By day 14, complete privileged MFA and first restoration rehearsal. By day 30, validate all P1 acceptance tests or submit a documented exception with interim protection and a realistic completion date. Complex resilience changes may need interim recovery controls and escalation rather than a false completion claim.

## Closure procedure

The implementer attaches configuration/ticket/test evidence to the action ID. Security or an independent peer checks that the evidence covers the intended population and reproduces the stated test. The asset owner reassesses residual risk. Only then may the reviewer set Verified closed, record reviewer/date and schedule ongoing monitoring. Failed or incomplete tests remain Open. A supplier promise, purchased licence or drafted document is insufficient.

If risk remains High or Critical, submit to the Board with options, consequence, compensating measures and time-limited acceptance request. The COO may accept Medium exposure within delegated appetite and a review date; owners may accept Low with documented rationale. No risk acceptance cancels an applicable legal obligation. All acceptance authority is proposed for this fictional case.

## Example closure record — template

Action ACT-8.5; population: all interactive workforce and administrative identities; implementer: IT Manager; change reference: pending; coverage export: pending; negative legacy-auth test: pending; emergency recovery test: pending; exceptions: pending; independent reviewer: pending; residual risk decision: pending. **Status remains Open.**

Monthly Board dashboard: P1 overdue count, verified closures, failed retests, accepted exceptions and expiry, current High/Critical risks, and cost/effort against plan. Report denominator changes when scope expands.
