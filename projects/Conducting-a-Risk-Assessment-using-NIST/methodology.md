# Risk assessment method - NIST SP 800-30 Rev. 1 informed

Purpose: prioritise threats to the fictional company's business services and information over the next 12 months. Prepared by Luke Bourdon for a portfolio exercise. Scope and assumptions are in [company context](company-context.md). This is a tailored qualitative method informed by NIST; the 5×5 matrix, thresholds and acceptance authorities are local choices, not a NIST-mandated calculation or certification.

## Assessment process

1. Prepare: agree scope, assets, owners, dependencies, tolerances, sources and risk criteria with management.
2. Conduct: identify threat sources/events, vulnerabilities and predisposing conditions; consider existing safeguards; assess likelihood of an event causing adverse effects and magnitude of harm; document uncertainty and dependencies.
3. Communicate: present the register, highest exposures, treatment options, decision owners and evidence needed to leadership.
4. Maintain: review monthly while remediation is active, then quarterly, and after material incidents, supplier changes, new services or threat changes.

For adversarial risks, consider attacker capability, intent and access; for non-adversarial risks, consider failure frequency and conditions. The overall likelihood below combines event occurrence and whether it would cause harm into one qualitative judgment. It is not a measured annual probability. Scores are ordinal prioritisation aids and must not be summed into a financial loss estimate.

## Likelihood over the next 12 months

| Score | Label | Decision anchor |
| --- | --- | --- |
| 1 | Rare | Unusual combination of circumstances; tested safeguards make successful harm difficult |
| 2 | Unlikely | Credible event but meaningful preventive barriers and limited exposure |
| 3 | Possible | Feasible pathway or dependency failure; safeguards partly effective or uncertain |
| 4 | Likely | Repeated exposure or known significant weakness with limited effective barriers |
| 5 | Almost certain | Persistent exposure with little resistance and strong evidence of recurring events |

## Business impact

Use the highest credible dimension; do not average serious privacy harm away. Monetary values are scenario thresholds, not forecasts of fines. Service disruption uses the customer platform unless a more critical dependency changes the assessment.

| Score | Financial loss | Service interruption | People / information / contractual effect |
| --- | --- | --- | --- |
| 1 | Under £5k | Under 1 hour | Negligible reversible internal inconvenience |
| 2 | £5k to under £25k | 1 to under 4 hours | Limited internal exposure; minor recoverable effect |
| 3 | £25k to under £100k | 4 to under 8 hours | Limited customer harm or contractual disruption; substantial investigation |
| 4 | £100k to under £500k | 8 to under 24 hours | Material customer/privacy harm or major contractual failure |
| 5 | £500k or more | 24 hours or more | Severe/widespread harm or loss of critical identity/integrity assurance |

## Rating and authority

Risk score = likelihood × impact. 1–5 Low; 6–11 Medium; 12–19 High; 20–25 Critical. Some integers are not reachable in a 5×5 matrix; bands remain exhaustive. Matrix cells below show score/rating.

| L / I | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 Low | 2 Low | 3 Low | 4 Low | 5 Low |
| 2 | 2 Low | 4 Low | 6 Medium | 8 Medium | 10 Medium |
| 3 | 3 Low | 6 Medium | 9 Medium | 12 High | 15 High |
| 4 | 4 Low | 8 Medium | 12 High | 16 High | 20 Critical |
| 5 | 5 Low | 10 Medium | 15 High | 20 Critical | 25 Critical |

Proposed appetite: no routine acceptance of High/Critical risk. Escalate Critical immediately for an interim protection decision within 48 hours; High to COO within five business days. Only the Board may exceptionally accept High/Critical exposure with explicit limits, expiry and monitoring. COO may accept Medium within delegated appetite, with review within 90 days. Business owner may accept Low with rationale and quarterly review. All authority awaits fictional Board approval. Legal duties cannot be waived by risk acceptance.

## Three distinct scores

**Inherent** excludes the stated safeguards. **Current residual** accounts only for the existing baseline safeguards. **Target residual** assumes the proposed treatment passes its acceptance tests. It must not replace current risk while work is merely planned. Impact may fall only where measures reduce consequences, such as restoration or data minimisation. Risk owners reassess and independent reviewers check closure evidence. Evidence confidence is Low for every invented case; this means substantial real-world uncertainty, not low risk. Initial milestone dates require treatment progress and interim protection. Full closure follows the linked action deadlines and scenario-specific evidence, including elapsed observation periods.

Treatments can mitigate, avoid, transfer/share or accept. These 16 scenarios use mitigation; the vendor decision pack demonstrates avoidance through a do-not-onboard recommendation. Insurance or contractual allocation does not remove privacy or operational accountability. Correlated risks (for example identity compromise, ransomware and delayed detection) overlap and must not be counted as independent losses.

Source: [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final). The detailed company analysis, ratings and thresholds are original scenario judgments.
