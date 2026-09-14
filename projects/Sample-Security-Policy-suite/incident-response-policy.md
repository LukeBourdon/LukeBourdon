# IR-001 - Incident response policy

**Northbridge Cloud Services Ltd | Internal | v1.0 | 14 September 2026**

Owner: Security Lead. Approver: Board. Status: draft for approval. Effective: 30 days after approval. Review: annually from approval and following material change. Supersedes: first issue.

## Purpose and application

Provide a coordinated response that limits harm, preserves evidence and supports timely decisions. Applies to suspected and confirmed events affecting confidentiality, integrity or availability, including supplier and personal data incidents.

## Reporting and triage

Users must report immediately through the service desk reporting button or published telephone/on-call route. The IT Manager maintains an offline contact card, tests it quarterly and ensures a 24-hour route for urgent incidents. Staff must not use invented portfolio addresses for actual reporting. A responder opens a uniquely numbered incident record, records discovery and awareness times with timezone, and captures facts separately from assumptions.

| Severity | Illustrative trigger | Internal response target | Escalation |
| --- | --- | --- | --- |
| SEV1 Critical | Active ransomware, privileged compromise, significant data exfiltration or critical service outage likely to exceed tolerance | Acknowledge within 15 minutes; appoint commander within 30 minutes | Security Lead, COO and Privacy Lead immediately; Board chair within 1 hour |
| SEV2 High | Confirmed contained compromise or material supplier incident with uncertain scope | Acknowledge within 1 hour; response team within 2 hours | Security Lead and affected business owner; Privacy Lead if personal data may be involved |
| SEV3 Moderate | Isolated malware blocked or suspicious activity needing investigation | Triage within 4 business hours | IT and Security |
| SEV4 Low | Benign event or low-impact policy issue | Triage within 1 business day | Service desk; record reason if closed |

Targets are internal service objectives, not substitutes for legal deadlines. Reclassify as evidence changes; record who changed severity and why. Uncertainty about active serious harm merits urgent escalation.

## Authority and actions

The Security Lead is incident commander; the IT Manager is deputy. The commander may isolate endpoints, revoke sessions and block malicious activity without waiting for Board approval where necessary to prevent harm. The COO authorises broad business shutdowns, with emergency protective action permitted if delay would materially increase harm and the COO is unreachable. Engineering leads production recovery; the Privacy Lead assesses notification duties; the COO controls external statements with Legal advice. Only authorised spokespeople communicate externally.

1. **Assess:** establish affected assets, data, users, dependencies, likely entry point and scope; record what remains unknown. Preserve logs before retention expiry.
2. **Contain:** choose proportionate isolation and identity measures, document business effects and review effectiveness. For supplier incidents, invoke contractual contacts and obtain a written impact statement.
3. **Preserve evidence:** collect through authorised responders, keep original records read-only, record UTC acquisition times, source, handler, cryptographic hash where appropriate and each transfer. Maintain access-restricted copies and chain of custody. Legal directs forensic retention and legal holds. Do not wipe systems before evidence decisions.
4. **Eradicate:** remove the cause, patch exploitable weaknesses, revoke exposed credentials and verify persistence has been addressed. Preserve relevant artefacts before rebuilding.
5. **Recover:** restore from validated clean sources, test integrity and business function, increase monitoring and obtain system-owner approval before returning service. Record achieved RTO/RPO against business targets.
6. **Learn:** hold a blameless review within ten business days after stabilisation, with root cause, control failures, timeline and named corrective actions. Keep actions open until evidence is retested by someone other than the implementer.

## Personal data and external notification

The Privacy Lead must assess whether a personal data breach is likely to risk individuals' rights and freedoms. As controller, report a reportable breach to the ICO without undue delay and within 72 hours of awareness; provide information in phases if necessary and explain any delay. Where high risk to individuals is likely, notify affected people without undue delay unless a lawful exception applies. As processor, notify the controller without undue delay and meet any shorter contractual requirement. Do not wait for a full forensic report. Record the facts, assessment and reasons even when no notification is required. Legal/Privacy must check any other contractual or sector obligations.

Reference: [ICO personal data breach guidance](https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/). The fictional company role and actual facts determine the duty; not every security event is reportable.

## Closure and assurance

The commander proposes operational closure after containment, recovery and outstanding risks are recorded. COO accepts operational closure; Privacy confirms notification decisions are documented. Open remediation remains tracked separately. Test this plan by a six-monthly tabletop and annual technical recovery exercise. Report acknowledgement times, time to containment, recovery performance and overdue actions; never mark an incident resolved solely because the help-desk ticket was closed.


## Compliance, exceptions and review

Managers must make these requirements available and provide practical support. Personnel must complete induction and acknowledge this policy before unsupervised access, with annual refreshers. Suspected non-compliance must be reported to the Security Lead without delay. HR handles alleged misconduct fairly under the employment process; an accidental report is not itself grounds for punishment. Supplier failures are managed under contract.

Exceptions require the recorded business reason, affected assets, risk assessment, compensating safeguards, owner, expiry and approval described in the [board paper](board-paper.md). No individual may approve their own exception. The owner reports overdue actions monthly to the COO and reviews effectiveness annually. Version changes and approvals are retained in the controlled policy register.
