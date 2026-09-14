# AC-001 - Access control policy

**Northbridge Cloud Services Ltd | Internal | v1.0 | 14 September 2026**

Owner: IT Manager. Approver: Board. Status: draft for approval. Effective: 30 days after approval. Review: annually from approval and following material change. Supersedes: first issue.

## Purpose and application

Ensure that every person and service has only the access required for an authorised purpose. Applies to corporate and production systems, cloud consoles, code, supplier access and non-human identities.

## Authorisation and lifecycle

Access must be denied by default and assigned to a unique identity through approved roles. The line manager establishes business need; the information or system owner approves the scope; IT provisions it and retains the ticket. Requesters and provisioners must not approve their own access. Finance payment creation and approval, and production change authoring and approval, must be separated. Where staffing prevents separation, the COO approves a time-limited exception with independent review of every affected transaction.

HR must notify IT before the start date and immediately upon a departure decision. Joiners receive access only after identity verification, contractual confidentiality and required induction. Contractors require a named sponsor and automatic expiry no later than the contract end date. Movers have obsolete rights removed by the effective role-change date; retaining old rights requires fresh justification. Leaver access, sessions, tokens and remote connectivity must be revoked by the agreed departure time; for involuntary or high-risk departures, revocation is coordinated with HR at notification. Out-of-hours revocation uses the on-call IT route. Review delegated mailboxes, API keys, shared secrets and group membership as part of closure.

## Authentication and privileges

MFA is mandatory for remote, cloud and privileged access. Privileged and high-risk roles must use phishing-resistant authentication where the service supports it; unsupported services require an approved mitigation and migration plan. Legacy authentication must be blocked after service dependency testing. Passwords must be unique, at least 14 characters where supported and screened against known compromised values. Change passwords on compromise or reset need; arbitrary routine changes are not required. Recovery must verify identity independently and must not bypass MFA through a weak help-desk process.

Use separate named administrator accounts for administrative tasks only. Time-bound elevation must have an approved task and expire within eight hours. Record privileged activity and send security alerts for unusual elevation. Shared administrator accounts are prohibited except controlled emergency accounts. Maintain two emergency accounts with protected credentials, alert on every use, test quarterly and review each use within one business day. Rotate emergency credentials immediately after use, and whenever exposure is suspected.

Service identities require an owner, documented purpose, minimum permissions, non-interactive sign-in and stored secrets in an approved vault. Prefer short-lived workload credentials. Static secrets must have a defined maximum lifetime of 90 days unless a documented technical exception applies; rotate immediately on exposure or relevant staff departure. Secrets must never appear in code or ordinary documents.

## Recertification and supplier access

System owners review privileged and supplier access monthly and all other access quarterly. Reviews must compare current users to HR/contractor records and actual role needs; tick-box confirmation of a group name is insufficient. IT removes inappropriate access within one business day of discovery, immediately where exposure is urgent. Reviewers record the user, entitlement, decision, reason, date and removal ticket. Dormant interactive accounts are disabled after 45 days unless the owner approves a documented exception. Supplier access must be named, time-limited, MFA-protected and logged.

## Verification

Monthly reporting includes the proportion of privileged accounts protected by MFA (100%), leavers disabled on time (100%), overdue review decisions (zero), and orphaned service identities (zero). Security samples ten lifecycle tickets monthly, or all if fewer, and independently tests revoked access. Failed tests create corrective actions; provisioned settings alone do not demonstrate effective removal.


## Compliance, exceptions and review

Managers must make these requirements available and provide practical support. Personnel must complete induction and acknowledge this policy before unsupervised access, with annual refreshers. Suspected non-compliance must be reported to the Security Lead without delay. HR handles alleged misconduct fairly under the employment process; an accidental report is not itself grounds for punishment. Supplier failures are managed under contract.

Exceptions require the recorded business reason, affected assets, risk assessment, compensating safeguards, owner, expiry and approval described in the [board paper](board-paper.md). No individual may approve their own exception. The owner reports overdue actions monthly to the COO and reviews effectiveness annually. Version changes and approvals are retained in the controlled policy register.
