# Risk scenario analysis and treatment evidence

All SIM-R observations are synthetic assumptions linked to the baseline. Impact reductions are forecasts only: they assume containment, reduced exposure or faster recovery limits harm, rather than merely reducing the chance of an event.

## R01 — Identity / confidentiality

| Field | Analysis |
| --- | --- |
| Assets | A02, A07 |
| Threat event | External attacker steals a workforce session and accesses customer exports |
| Vulnerability / predisposing condition | MFA coverage 85% and legacy authentication remains available |
| Existing safeguards | Partial MFA and email filtering |
| Evidence | SIM-R01: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Common remote attack route remains available across 15% of accounts; broad identity reach makes impact severe |
| Current exposure | L4 × I5 = 20 (Critical) |
| Treatment / risk owner | Enforce MFA block legacy sign-in restrict sessions and test recovery / IT Manager |
| Control links | 5.16, 5.17, 8.5 |
| Target assumption | Impact held constant: treatment mainly reduces event likelihood. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R02 — Malware / availability

| Field | Analysis |
| --- | --- |
| Assets | A01, A03, A05, A08 |
| Threat event | Ransomware spreads from an unmanaged laptop and disrupts service recovery |
| Vulnerability / predisposing condition | 12 devices unmanaged and backup restoration untested |
| Existing safeguards | Protection on 108 devices and nightly backups |
| Evidence | SIM-R02: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Coverage gaps and uncertain restore capability leave likelihood high and multi-day disruption plausible |
| Current exposure | L4 × I5 = 20 (Critical) |
| Treatment / risk owner | Enrol or block unmanaged devices isolate backups and prove full restoration / IT Manager |
| Control links | 8.1, 8.7, 8.13 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R03 — Data handling / confidentiality

| Field | Analysis |
| --- | --- |
| Assets | A01, A09 |
| Threat event | Support user shares a customer export through a public link |
| Vulnerability / predisposing condition | Exports are unclassified and broad sharing is allowed |
| Existing safeguards | Authenticated internal storage |
| Evidence | SIM-R03: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Routine exports create repeated opportunities; storage authentication does not protect a public share |
| Current exposure | L4 × I4 = 16 (High) |
| Treatment / risk owner | Classify exports restrict named sharing and test leakage alerts / Privacy Lead |
| Control links | 5.12, 5.14, 8.12 |
| Target assumption | Impact held constant: treatment mainly reduces event likelihood. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R04 — Access / integrity

| Field | Analysis |
| --- | --- |
| Assets | A02, A04 |
| Threat event | Former worker changes code or reads retained information after departure |
| Vulnerability / predisposing condition | Two former staff identities and one contractor repository grant remain |
| Existing safeguards | Informal HR notices |
| Evidence | SIM-R04: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Known stale access creates a credible pathway though malicious use is not assumed |
| Current exposure | L3 × I4 = 12 (High) |
| Treatment / risk owner | Disable stale access reconcile HR and repositories and verify revocation / IT Manager |
| Control links | 5.16, 5.18, 8.4 |
| Target assumption | Impact held constant: treatment mainly reduces event likelihood. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R05 — Resilience / availability

| Field | Analysis |
| --- | --- |
| Assets | A03, A08 |
| Threat event | Cloud-zone outage leaves the customer platform unavailable beyond tolerance |
| Vulnerability / predisposing condition | One-zone dependency and no current full restore exercise |
| Existing safeguards | Nightly backup jobs report success |
| Evidence | SIM-R05: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Backup completion does not show recovery; a zone event could breach the 8-hour target |
| Current exposure | L3 × I5 = 15 (High) |
| Treatment / risk owner | Test restore improve recovery points and implement tested failover / Head of Engineering |
| Control links | 5.30, 8.13, 8.14 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R06 — Supplier / privacy

| Field | Analysis |
| --- | --- |
| Assets | A06, A11 |
| Threat event | Payroll processor exposes employee bank and health information |
| Vulnerability / predisposing condition | Security evidence and incident terms not yet validated |
| Existing safeguards | Procurement review of commercial terms |
| Evidence | SIM-R06: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Sensitive employee data would create serious harm; supplier effectiveness is uncertain |
| Current exposure | L3 × I5 = 15 (High) |
| Treatment / risk owner | Hold onboarding until privacy contract MFA and restore evidence pass review / People Lead |
| Control links | 5.19, 5.20, 5.34 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R07 — Application / integrity

| Field | Analysis |
| --- | --- |
| Assets | A03, A04 |
| Threat event | Attacker exploits an unpatched internet-facing component |
| Vulnerability / predisposing condition | Quarterly patch cycle and no urgency-based treatment |
| Existing safeguards | Peer review and occasional scanning |
| Evidence | SIM-R07: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Public exposure and long patch windows make exploitation plausible; full platform compromise is possible |
| Current exposure | L4 × I5 = 20 (Critical) |
| Treatment / risk owner | Triage exploited exposures within 24h fix or isolate within 72h and rescan / Head of Engineering |
| Control links | 8.8, 8.29 |
| Target assumption | Impact held constant: treatment mainly reduces event likelihood. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R08 — Supply chain / integrity

| Field | Analysis |
| --- | --- |
| Assets | A04, A03 |
| Threat event | Compromised dependency introduces malicious code into a release |
| Vulnerability / predisposing condition | No dependency inventory or enforced security release gate |
| Existing safeguards | General peer review |
| Evidence | SIM-R08: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Build chain is trusted without component assurance; compromise can reach customer workloads |
| Current exposure | L3 × I5 = 15 (High) |
| Treatment / risk owner | Inventory components scan dependencies require signed reviewed builds and rollback tests / Head of Engineering |
| Control links | 5.21, 8.25, 8.28 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R09 — Privileged misuse / confidentiality

| Field | Analysis |
| --- | --- |
| Assets | A01, A03 |
| Threat event | Administrator exports production data outside an approved task |
| Vulnerability / predisposing condition | Six standing production administrators and limited monitoring |
| Existing safeguards | Named accounts and basic cloud logs |
| Evidence | SIM-R09: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Standing access provides opportunity; no allegation of malicious staff behaviour is made |
| Current exposure | L3 × I5 = 15 (High) |
| Treatment / risk owner | Use time-bound elevation independent approval and export monitoring / Head of Engineering |
| Control links | 5.3, 8.2, 8.16 |
| Target assumption | Impact held constant: treatment mainly reduces event likelihood. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R10 — Privacy / retention

| Field | Analysis |
| --- | --- |
| Assets | A01, A06 |
| Threat event | Customer deletion request leaves identifiable copies in test or exports |
| Vulnerability / predisposing condition | No coordinated deletion or backup re-deletion workflow |
| Existing safeguards | Manual primary-record removal |
| Evidence | SIM-R10: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Known copy creation makes incomplete deletion likely and could harm individuals |
| Current exposure | L4 × I4 = 16 (High) |
| Treatment / risk owner | Map copies automate deletion use synthetic test data and retain decision evidence / Privacy Lead |
| Control links | 5.34, 8.10, 8.11, 8.33 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R11 — Fraud / financial integrity

| Field | Analysis |
| --- | --- |
| Assets | A07, A11 |
| Threat event | Impersonator persuades Finance to change vendor bank details |
| Vulnerability / predisposing condition | No documented independent callback and dual-approval check |
| Existing safeguards | Email filtering and staff experience |
| Evidence | SIM-R11: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Plausible business email attack; existing filters do not validate payment instructions |
| Current exposure | L3 × I4 = 12 (High) |
| Treatment / risk owner | Require known-number callback and dual approval; practise payment scenario / Finance Director |
| Control links | 5.3, 6.3 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R12 — Physical loss / confidentiality

| Field | Analysis |
| --- | --- |
| Assets | A05, A06 |
| Threat event | Laptop containing HR export is lost while travelling |
| Vulnerability / predisposing condition | Travel guidance and export minimisation are absent |
| Existing safeguards | Disk encryption on managed devices |
| Evidence | SIM-R12: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Encryption reduces exposure when powered off; active sessions or unmanaged copies remain uncertain |
| Current exposure | L2 × I4 = 8 (Medium) |
| Treatment / risk owner | Verify encryption restrict local exports and test immediate loss response / IT Manager |
| Control links | 6.7, 7.9, 8.1 |
| Target assumption | Impact held constant: treatment mainly reduces event likelihood. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-12-13 / 2026-10-14 |

## R13 — Detection / operational

| Field | Analysis |
| --- | --- |
| Assets | A02, A03, A12 |
| Threat event | Out-of-hours compromise persists until the next working day |
| Vulnerability / predisposing condition | Alerts only reviewed in office hours and logs retained seven days |
| Existing safeguards | Basic cloud alerts |
| Evidence | SIM-R13: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | An attacker or weekend event can exploit a known response gap; delayed containment expands harm |
| Current exposure | L4 × I5 = 20 (Critical) |
| Treatment / risk owner | Route urgent alerts to on-call and retain protected investigation logs / Security Lead |
| Control links | 5.24, 8.15, 8.16 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R14 — Supplier / availability

| Field | Analysis |
| --- | --- |
| Assets | A09, A11 |
| Threat event | Support SaaS outage prevents customer incident coordination |
| Vulnerability / predisposing condition | No tested export or alternative support process |
| Existing safeguards | Supplier uptime promise |
| Evidence | SIM-R14: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Contract promise alone does not provide a usable alternative during outage |
| Current exposure | L3 × I4 = 12 (High) |
| Treatment / risk owner | Test daily export and secure fallback customer contact workflow / Customer Operations Lead |
| Control links | 5.22, 5.29, 5.30 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |

## R15 — Environmental / availability

| Field | Analysis |
| --- | --- |
| Assets | A10, A12 |
| Threat event | Office power or water incident interrupts staff connectivity |
| Vulnerability / predisposing condition | Equipment near sink and no tested utility fallback |
| Existing safeguards | Cloud-hosted application and hybrid working |
| Evidence | SIM-R15: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Remote work limits whole-company impact but local equipment remains exposed |
| Current exposure | L2 × I3 = 6 (Medium) |
| Treatment / risk owner | Relocate equipment and rehearse safe remote continuity / Facilities Lead |
| Control links | 7.5, 7.8, 7.11 |
| Target assumption | Impact held constant: treatment mainly reduces event likelihood. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-12-13 / 2026-10-14 |

## R16 — People / availability

| Field | Analysis |
| --- | --- |
| Assets | A03, A12 |
| Threat event | Key engineer is unavailable during identity or service recovery |
| Vulnerability / predisposing condition | Only one person knows undocumented recovery steps |
| Existing safeguards | Partial deployment runbooks |
| Evidence | SIM-R16: scenario assumes the vulnerability and safeguards stated above. No real test performed. |
| Assessment rationale | Absence can coincide with an outage; deputy capability is unproven |
| Current exposure | L3 × I4 = 12 (High) |
| Treatment / risk owner | Document recovery and have a deputy execute the exercise unaided / COO |
| Control links | 5.37, 6.3, 5.30 |
| Target assumption | Lower impact assumes the proposed containment, minimisation or recovery measures limit the damage; retain current impact until a test demonstrates this. |
| Acceptance evidence | Complete and independently retest the linked Annex A action-register closure tests; attach results before recalculating current risk. |
| Uncertainty | Low — synthetic desk assumptions; obtain configuration exports, source records and owner interviews before operational decisions. |
| Decision / status | Mitigate / Open — treatment proposed |
| Due / next review | 2026-10-14 / 2026-10-14 |
