# Vendor decision report

**Northbridge | Fictional assessments | 14 September 2026 | Recommendations, not executed approvals**

| Vendor | Inherent tier | Weighted gap | Base rating | Unmet gates | Final rating | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| Beacon Support Cloud | High | 7/182 (3.85%) | Low | None | Low | Approve with tracked improvements |
| Alder Payroll Services | Critical | 35/182 (19.23%) | Moderate | Q03, Q09, Q13 | High | Hold onboarding pending gate closure |
| Cedar Insight Analytics | High | 161/182 (88.46%) | Critical | Q03, Q06, Q09, Q13, Q17 | Critical | Do not onboard |

## Beacon Support Cloud

Recommend approval for the stated Confidential support data scope, subject to contract execution and business-owner sign-off. The low gap index does not lower its inherent High tier. Procurement must obtain evidence of backup restore-and-redeletion (Q16) by 14 October 2026 and a complete bulk attachment export test (Q20) by 13 December 2026. Customer Operations owns an alternative contact process. Review quarterly actions and reassess by 14 September 2027 or earlier after a material change. Approval remains a recommendation; no vendor has been onboarded.

## Alder Payroll Services

Hold production onboarding and do not transfer Restricted employee data. Its numerical base score understates the decision significance of incomplete MFA, delayed incident wording and stale restore proof. Require closure of Q03, Q09 and Q13 by 14 October 2026: eliminate support MFA exceptions; agree awareness-based notice without undue delay with a 24-hour outer target; observe a current restore meeting 8h/24h targets. Procurement owns contract changes; IT reviews MFA; People Lead owns the business decision.

Also require Privacy to resolve overseas-access transfer assurance (Q07) before any such access, update independent assurance (Q02), agree faster active-exploitation treatment (Q11), prove full deletion lifecycle (Q16) and enforce secrets checking (Q24). Re-score all changed answers and apply the gates again. No forecast is treated as an achieved residual rating. This decision informs risk R06 in the NIST assessment.

## Cedar Insight Analytics

Recommend rejection of the proposed identifiable-data service. Missing processing terms, location information, enforced MFA, incident commitments, tested recovery and isolation evidence cannot be offset by basic code review or an export function. The analytics service is optional: avoid this exposure or select another provider. A future assessment could consider an architecture using demonstrably anonymised data with no access to Northbridge production; that requires a new scope and privacy validation, not an automatic rating reduction. Procurement records the decision; no production connection should be created.

## Remediation and re-review log

| Action | Owner | Deadline / gate | Evidence for closure | Status |
| --- | --- | --- | --- | --- |
| B-01 Q16 deletion across restore | Beacon service owner / Privacy | 2026-10-14 | Synthetic restore and re-deletion test | Open |
| B-02 Q20 complete export | Customer Operations | 2026-12-13 | Importable export including attachments | Open |
| A-01 Q03 MFA exceptions | IT Manager | Before onboarding, target 2026-10-14 | Full coverage and negative sign-in test | Open |
| A-02 Q09 notification clause | Procurement | Before onboarding, target 2026-10-14 | Agreed contractual wording and contact test | Open |
| A-03 Q13 current restore | People Lead / IT | Before onboarding, target 2026-10-14 | Timed witnessed restore and data-age result | Open |
| A-04 Q07 overseas access | Privacy Lead | Before overseas access | Complete location and transfer assessment | Open |
| A-05 Q02/Q11/Q16/Q24 assurance | Procurement / Security | Target 2026-10-14 before final review | Current assurance, patch SLA, deletion and build evidence | Open |
| C-01 decline proposed scope | Procurement | Before any data transfer | Recorded decision and confirmation no integration created | Recommendation pending |

## Decision record template

Vendor/service/scope; inherent tier; assessment version; evidence reviewed; unresolved findings; final rating and gate result; decision rationale; conditions; risk owner; approver; date; expiry; next review. No approval fields are pre-signed in this portfolio.
