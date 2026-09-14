# Evidence-based supplier scoring and decision method

Fictional assessment as at 14 September 2026. Security reviews responses independently; Procurement manages contracts; the business owner accepts operational dependency; Privacy reviews processing. All three example vendors are invented.

## Separate exposure from control assurance

Inherent tier describes the proposed service/data dependency before considering controls. It determines assessment depth and review frequency; it is not calculated by averaging questionnaire answers. High/Critical services require enhanced evidence review and annual reassessment, quarterly action monitoring and reassessment after a material incident or service change.

Response score: **2** = requirement met with current, relevant scenario evidence; **1** = partial implementation, incomplete scope or stale evidence; **0** = absent, declined or unsupported. A bare Yes does not earn 2. Evidence references SIM-A/B/C are fictional review notes, not real reports. No N/A answers are used: every question is relevant to the three hosted services. In future, N/A requires reviewer rationale and adjusts the denominator explicitly.

For each item: weighted gap = weight × (2 − score). Total risk indicator = 100 × sum(weighted gaps) / (2 × sum(weights)). Here sum(weights) = 91, so denominator = 182. Higher means more unresolved assurance gaps. Keep full precision for decisions; display two decimals. This is a local assurance-gap index, not a predicted breach probability.

Bands: 0–15 inclusive Low; above 15–35 Moderate; above 35–60 High; above 60 Critical.

## Mandatory gates override an attractive average

Q03 (MFA), Q06 (processing terms), Q09 (timely incident notice), Q13 (tested recovery), and Q17 (tenant isolation) must score 2 for these services before production onboarding. If any score below 2, final risk is at least High and onboarding is blocked pending evidence/contract resolution. A Critical base score stays Critical. At assessment, Q06 may score 2 for legally reviewed, agreed wording ready for signature; an executed agreement remains a separate mandatory condition before processing, even when the questionnaire rating is Low. Gate closure must be independently verified; commercial urgency is not evidence.

The notification expectation is without undue delay with a contractual outer target of 24 hours after awareness for these cases; it is a procurement requirement, not a universal statutory deadline for every vendor. Recovery expectations are service-specific and must be written into the contract.

Low: business owner/Procurement may recommend approval with ordinary monitoring. Moderate: approve only with time-bound actions and Security concurrence. High: do not start production processing until gates are met and accountable leadership reviews remaining risk. Critical: reject or redesign the service to avoid exposure; any exceptional consideration goes to the Board with Privacy/Legal review. No signature or actual onboarding is asserted here.

Source context: [NIST SP 800-161 Rev. 1 supply-chain guidance](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final). The questionnaire, weights and decision gates are original local design choices.
