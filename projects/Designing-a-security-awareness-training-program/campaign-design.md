# Simulated phishing campaign design and rules of engagement

**Design only. No messages sent, live domains registered or credentials collected.** The completed exercise report is a synthetic worked example. Before a real campaign, obtain written sponsor, Security, People and Privacy approval and verify the technical setup with the mail administrator.

## Scope and constraints

Fictional population: 120 staff across five departments. Use a benign document-sharing scenario with a controlled training destination. Exclude third parties, personal addresses, people on leave and anyone requiring an agreed accommodation; adjust denominators in actual deployment. Do not use payroll threats, dismissal notices, medical emergencies or distressing personal themes. Stop on unintended delivery, operational disruption, real credential capture, privacy concern or a concurrent real incident. The Security Lead owns the stop decision.

The live implementation, if separately authorised, must use a company-controlled training domain, safe landing page, scoped allowlisting and access-controlled event collection. Do not broadly disable email protections. Domain and message authentication setup must be reviewed by IT. This repository contains no operational sending script.

## Example message - fictional artefact

From display name: Northbridge Workspace Updates
Subject: Please review the revised team workspace guide

A revised workspace guide is ready for your review before Friday. Open the shared document to confirm you have seen the changes.

Displayed link: Review workspace guide
Illustrative destination: `https://training.northbridge.example/workspace-review`

The `.example` address is a non-operational placeholder. The message is not an exact clone of a real service. A live lure would require authorised design and controlled infrastructure.

## Landing page and measurements

The landing page identifies the exercise and provides a short explanation after the interaction. To illustrate a higher-risk action without collecting secrets, offer a clearly dummy continuation button rather than a password field. The report calls this a **dummy submission**, never a real credential submission. The page must not accept or retain passwords. Because the dummy action is clearly labelled and the page reveals the exercise, this measures interaction with the training page, not willingness to surrender credentials. Capture a pseudonymous participant token, campaign, time and event type only. Prevent or separately classify automated scanner events through a tested method agreed with IT.

## Comparison design

The worked example uses 3 August 2026 baseline and 24 August 2026 follow-up, with learning between them and closure on 31 August. Both use document-sharing themes, similar urgency, comparable timing and the same fictional 120-person cohort. The lure is presumed moderately relevant to office work, but a formal NIST Phish Scale score was not produced. Before live comparison, trained reviewers should rate cues and premise alignment and retain the worksheet. Do not present this example as difficulty-adjusted evidence.

Metrics: unique human clickers / delivered recipients; unique dummy submitters / delivered; unique reporters / delivered; median minutes to first report among reporters. Clickers and reporters can overlap, so percentages need not sum to 100. Per-participant data must distinguish events and allow deduplication. Report bounced deliveries and bot exclusions separately. In this synthetic example all 120 messages are delivered and no bot events are generated.

Source: [NIST Phish Scale user guide context](https://csrc.nist.gov/news/2023/the-nist-phish-scale-user-guide-is-now-available). Lure difficulty and user context affect interpretation of click and report rates.
