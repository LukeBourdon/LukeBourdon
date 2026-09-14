# Alder Payroll Services — fictional assessment

Service: Managed payroll and HR processing. Data: Employee bank details and limited HR health information; Restricted. Inherent tier: **Critical** — Restricted employee data and payment processing require enhanced assessment. Recovery/criticality: Payroll processing around pay-run deadlines; proposed RTO 8h / RPO 24h.

Assessment date: 14 September 2026. Fictional vendor respondent: service security contact. Assessor: portfolio analyst role; independent sign-off pending.

Weighted gap: **35/182 = 19.23%**. Base rating: Moderate. Unmet mandatory gates: Q03, Q09, Q13. Final risk: **High**. See [decision report](decision-report.md) for actions and onboarding recommendation.

| Item | Fictional response | Synthetic evidence review | Score / 2 | Weighted gap |
| --- | --- | --- | --- | --- |
| Q01 | Annual policies owned by operations director | SIM-A01: approved register and owner | 2 | 0 |
| Q02 | Assurance report available from last year | SIM-A02: report period expired; no bridge letter | 1 | 4 |
| Q03 | MFA on administrators; two support exceptions remain | SIM-A03: export identifies two password-only support accounts | 1 | 5 |
| Q04 | Quarterly reviews and timed offboarding | SIM-A04: five complete samples | 2 | 0 |
| Q05 | Encrypted service with controlled key administration | SIM-A05: key review and encryption configuration | 2 | 0 |
| Q06 | Processing schedule includes payroll instructions | SIM-A06: reviewed DPA ready to sign | 2 | 0 |
| Q07 | UK hosting with occasional overseas support | SIM-A07: access map supplied; transfer assessment incomplete | 1 | 4 |
| Q08 | Subprocessors listed and advance notice offered | SIM-A08: current list and 30-day notice | 2 | 0 |
| Q09 | Notification promised within 72 hours of confirmation | SIM-A09: confirmation trigger could delay awareness-based notice | 1 | 5 |
| Q10 | Annual incident exercise completed | SIM-A10: May exercise report and closed actions | 2 | 0 |
| Q11 | Critical patch target is 30 days | SIM-A11: no faster route for active exploitation | 1 | 5 |
| Q12 | Independent test and high retest supplied | SIM-A12: relevant payroll application covered | 2 | 0 |
| Q13 | Backup jobs pass but full restore evidence is old | SIM-A13: last full test 18 months ago; no current 8h/24h proof | 1 | 5 |
| Q14 | Manual payroll continuity process exercised | SIM-A14: tabletop confirms process and dual authorisation | 2 | 0 |
| Q15 | Protected logs with on-call alerts | SIM-A15: rota and one test alert record | 2 | 0 |
| Q16 | Deletion covers active database only | SIM-A16: exports and backup lifecycle missing from evidence | 1 | 4 |
| Q17 | Tenant checks demonstrated | SIM-A17: payroll tenant negative tests | 2 | 0 |
| Q18 | Screening and confidentiality records current | SIM-A18: five complete samples | 2 | 0 |
| Q19 | Release approval and rollback documented | SIM-A19: six reviewed changes | 2 | 0 |
| Q20 | Payroll export tested | SIM-A20: usable file and defined exit assistance | 2 | 0 |
| Q21 | Physical responsibilities evidenced | SIM-A21: relevant hosting assurance | 2 | 0 |
| Q22 | Financial and insurance information reviewed | SIM-A22: adequate fictional financial position | 2 | 0 |
| Q23 | Audit rights and material incident history supplied | SIM-A23: contract and signed statement | 2 | 0 |
| Q24 | Dependency scan exists but secrets checks optional | SIM-A24: pipeline settings show non-blocking scan | 1 | 3 |
