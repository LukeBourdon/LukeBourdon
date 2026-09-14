# Annex A — technological controls

Baseline: 31 August 2026. All observations are synthetic. Read the [method](assessment-report.md) before interpreting status. IDs identify the reference control; topics below are original shorthand.

## 8.1 — Endpoint hardening

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | 108 of 120 laptops are enrolled in management (SIM-A8.1) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.1: Enrol all supported devices and quarantine unmanaged access |
| Owner / deadline | IT Manager / 2026-10-14 / P1 |
| Closure evidence | Device inventory reconciles to 120 compliant or blocked endpoints |
| Action status | Open |

## 8.2 — Administrative privileges

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Six engineers hold standing production administrator rights (SIM-A8.2) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.2: Remove standing privilege and introduce time-limited elevation |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Elevation expires and six legacy grants are removed |
| Action status | Open |

## 8.3 — Data access boundaries

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Customer exports are readable by all support staff (SIM-A8.3) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.3: Restrict exports by job and customer assignment |
| Owner / deadline | IT Manager / 2026-10-14 / P1 |
| Closure evidence | Positive and negative access tests confirm least privilege |
| Action status | Open |

## 8.4 — Source repository permissions

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Departed contractor remains in a code repository team (SIM-A8.4) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.4: Reconcile code access and enforce protected review paths |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Former contractor cannot access and self-merge is blocked |
| Action status | Open |

## 8.5 — Authentication safeguards

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | MFA covers 85% of workforce and legacy sign-in is enabled (SIM-A8.5) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.5: Enforce MFA and block legacy paths with tested recovery |
| Owner / deadline | IT Manager / 2026-10-14 / P1 |
| Closure evidence | Report 100% coverage or approved exceptions and negative legacy test |
| Action status | Open |

## 8.6 — Resource capacity oversight

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | CPU alerts exist but no demand forecasting or load test (SIM-A8.6) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.6: Set capacity thresholds and test peak load |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Load test meets agreed service latency and headroom targets |
| Action status | Open |

## 8.7 — Malicious software defence

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Endpoint protection excludes the 12 unmanaged laptops (SIM-A8.7) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.7: Deploy protection and verify alert-to-response workflow |
| Owner / deadline | IT Manager / 2026-10-14 / P1 |
| Closure evidence | All endpoints report healthy and safe test alert is triaged |
| Action status | Open |

## 8.8 — Vulnerability treatment

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Patching is quarterly with no exploited-vulnerability prioritisation (SIM-A8.8) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.8: Set risk-based deadlines and scan for closure |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Critical exposure is fixed or isolated within 72 hours and rescanned |
| Action status | Open |

## 8.9 — Secure configuration baselines

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Cloud settings are changed manually without drift checks (SIM-A8.9) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.9: Version approved baselines and alert on drift |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Intentional safe deviation is detected and corrected |
| Action status | Open |

## 8.10 — Data removal

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Customer deletion requests do not cover exports and backups (SIM-A8.10) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.10: Implement deletion workflow with backup expiry and restore re-deletion |
| Owner / deadline | Privacy Lead / 2026-10-14 / P1 |
| Closure evidence | Synthetic record is removed across active stores and lifecycle is evidenced |
| Action status | Open |

## 8.11 — Non-production data protection

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Developers copy identifiable customer records into test (SIM-A8.11) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.11: Replace with synthetic data and restrict exceptional masked datasets |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Scan test stores and verify no unapproved identifiable records |
| Action status | Open |

## 8.12 — Data-exfiltration safeguards

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | No controls detect broad customer exports or public links (SIM-A8.12) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.12: Configure targeted sharing restrictions and leakage alerts |
| Owner / deadline | IT Manager / 2026-10-14 / P1 |
| Closure evidence | Safe test export triggers response and public sharing is blocked |
| Action status | Open |

## 8.13 — Backup assurance

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Nightly backups exist but last full restore was over a year ago (SIM-A8.13) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.13: Protect immutable copies and increase recovery points to meet RPO |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Restore test proves integrity recovery time and data age |
| Action status | Open |

## 8.14 — Service resilience

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Production has one availability-zone dependency (SIM-A8.14) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.14: Design resilience and test failover of critical components |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Zone-failure exercise meets agreed continuity objectives |
| Action status | Open |

## 8.15 — Security log retention

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Authentication logs retain only seven days (SIM-A8.15) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.15: Centralise protected logs with approved risk-based retention |
| Owner / deadline | Security Lead / 2026-10-14 / P1 |
| Closure evidence | Retrieve a 90-day test record and verify restricted deletion rights |
| Action status | Open |

## 8.16 — Detection and response monitoring

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Alerts are reviewed only during office hours (SIM-A8.16) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.16: Route high-severity alerts to an on-call responder |
| Owner / deadline | Security Lead / 2026-10-14 / P1 |
| Closure evidence | Out-of-hours safe test generates acknowledged incident |
| Action status | Open |

## 8.17 — Consistent system time

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Managed hosts use approved time sources and drift alerts (SIM-A8.17) |
| Status | Implemented |
| Gap / implication | No gap identified within the limited fictional sample; continue assurance. |
| Action | ACT-8.17: Maintain time service and monitor exceptions |
| Owner / deadline | IT Manager / 2027-03-13 / P3 |
| Closure evidence | Sample host timestamps agree within defined tolerance |
| Action status | Scheduled assurance |

## 8.18 — Powerful administration tools

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Support can run unrestricted administrative utilities (SIM-A8.18) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.18: Allowlist privileged tools and log approved usage |
| Owner / deadline | IT Manager / 2026-12-13 / P2 |
| Closure evidence | Unapproved utility fails and approved use is attributable |
| Action status | Open |

## 8.19 — Production software installation

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Developers can install production packages interactively (SIM-A8.19) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.19: Require approved pipeline or emergency change route |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Unapproved install is denied and exception is logged |
| Action status | Open |

## 8.20 — Network defence

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Firewall rules have no owner or expiry review (SIM-A8.20) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.20: Remove broad rules and record justified network flows |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Connectivity tests permit only approved flows |
| Action status | Open |

## 8.21 — Network service assurance

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | ISP contract lacks tested incident escalation (SIM-A8.21) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.21: Document security service requirements and supplier escalation |
| Owner / deadline | IT Manager / 2026-12-13 / P2 |
| Closure evidence | Provider contact test and contract review demonstrate response route |
| Action status | Open |

## 8.22 — Network isolation

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Office guest network can reach internal printer management (SIM-A8.22) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.22: Separate guest corporate and administrative networks |
| Owner / deadline | IT Manager / 2026-10-14 / P1 |
| Closure evidence | Guest-to-management negative connectivity test passes |
| Action status | Open |

## 8.23 — Web destination filtering

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | No managed protection against known malicious web destinations (SIM-A8.23) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.23: Deploy filtering with privacy-aware exception process |
| Owner / deadline | IT Manager / 2026-12-13 / P2 |
| Closure evidence | Safe known test category is blocked and exception reviewed |
| Action status | Open |

## 8.24 — Encryption and key governance

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Encryption is enabled but key ownership and rotation are undocumented (SIM-A8.24) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.24: Inventory keys assign owners and test controlled rotation |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Verify encryption configuration and rotation without data loss |
| Action status | Open |

## 8.25 — Secure delivery lifecycle

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Code review exists but security stages are optional (SIM-A8.25) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.25: Define mandatory design build and release security gates |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Two releases show completed gates and risk decisions |
| Action status | Open |

## 8.26 — Application security requirements

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Product specifications omit security acceptance criteria (SIM-A8.26) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.26: Add access logging privacy and abuse requirements |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Sample feature has testable security requirements before build |
| Action status | Open |

## 8.27 — Secure architecture decisions

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | No documented trust boundaries or design principles (SIM-A8.27) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.27: Document boundaries threat models and approved design patterns |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Architecture review traces a threat to design mitigation |
| Action status | Open |

## 8.28 — Coding safeguards

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Peer review lacks input-validation and secrets checklist (SIM-A8.28) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.28: Adopt coding checklist and developer training |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Sample pull requests and static scan show required checks |
| Action status | Open |

## 8.29 — Security release testing

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Functional tests run but penetration findings lack retest (SIM-A8.29) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.29: Add security tests and block releases with unaccepted high findings |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Release evidence includes independent retest of high findings |
| Action status | Open |

## 8.30 — Contract development assurance

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Contract developers have no agreed security acceptance terms (SIM-A8.30) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.30: Contract for secure delivery artefact review and access expiry |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Sample delivered component meets security and access terms |
| Action status | Open |

## 8.31 — Environment separation

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Subscriptions differ but production identities access test data copies (SIM-A8.31) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.31: Separate identities secrets and data flows by environment |
| Owner / deadline | Head of Engineering / 2026-10-14 / P1 |
| Closure evidence | Test identity cannot administer production and test data is sanitised |
| Action status | Open |

## 8.32 — Controlled system changes

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Emergency changes lack retrospective review (SIM-A8.32) |
| Status | Partial |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.32: Require testing approval rollback and prompt emergency review |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Ten changes include evidence and emergency review within one day |
| Action status | Open |

## 8.33 — Test dataset handling

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | No owner retention or cleanup for test datasets (SIM-A8.33) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.33: Approve test-data register minimisation and deletion rules |
| Owner / deadline | Head of Engineering / 2026-12-13 / P2 |
| Closure evidence | Synthetic test dataset is owned time-limited and deleted on expiry |
| Action status | Open |

## 8.34 — Safe audit testing

| Field | Assessment |
| --- | --- |
| Applicability | Applicable — Developed SaaS platform and corporate technology are in scope |
| Current state / evidence | Security testing is performed without written rules of engagement (SIM-A8.34) |
| Status | Missing |
| Gap / implication | The described baseline does not provide complete, repeatable assurance for this topic; treatment below is required. |
| Action | ACT-8.34: Approve scope timing data handling and stop conditions for audits |
| Owner / deadline | Security Lead / 2026-12-13 / P2 |
| Closure evidence | Test plan is authorised and monitoring confirms no unplanned disruption |
| Action status | Open |
