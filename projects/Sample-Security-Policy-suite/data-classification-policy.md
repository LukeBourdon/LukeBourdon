# DC-001 — Data classification and handling policy

**Northbridge Cloud Services Ltd | Internal | v1.0 | 14 September 2026**

Owner: Privacy Lead. Approver: Board. Status: draft for approval. Effective: 30 days after approval. Review: annually from approval and following material change. Supersedes: first issue.

## Purpose and application

Apply protection proportionate to business harm, privacy obligations and contractual commitments throughout the information lifecycle. Applies to electronic, paper, verbal and recorded information and all copies, exports and backups.

## Ownership and decisions

Every dataset and repository must have a business owner who records its classification, purpose, authorised audience and retention rule. Classify at creation or receipt and review annually or when use changes. Use the highest applicable level for mixed datasets; if uncertain, treat as Confidential pending an owner decision. Personal data is at least Confidential; special-category HR data, credentials and recovery secrets are Restricted. Classification does not itself establish a lawful basis for processing.

| Level | Examples | Access and sharing | Storage and transmission | Disposal |
| --- | --- | --- | --- | --- |
| Public | Approved website content and published brochures | Release requires content-owner approval | Approved services; integrity and version control still apply | Ordinary disposal unless retained as a business record |
| Internal | Routine internal guidance and non-sensitive planning | Authenticated workforce; external release by owner | Company-managed storage and secure connections | Managed deletion; confidential paper recycling preferred |
| Confidential | Customer contact records, contracts, source code and payroll totals | Named groups with business need; owner-approved external recipients | Encryption in transit and at rest; expiring named shares; no public links or personal storage | Verified deletion by IT; cross-cut shredding or approved secure destruction |
| Restricted | HR health details, identity documents, authentication secrets | Explicit named access; owner approval and monthly review; minimise copies | Approved restricted repository or secrets vault; MFA; external transfer only after owner and Privacy/Security review using an agreed secure route | Logged destruction; evidence for retired media; respect legal holds |

## Handling requirements

Label documents and email with the level using available sensitivity labels or a clear header. Dataset catalogues and system metadata must record classification where a visual label is impractical. Do not put secrets in file names. Owners verify external recipient identity, purpose and minimum necessary fields before sharing. Send decryption secrets by a separate approved channel where file encryption is used. Restricted data must not be placed on removable media without an approved, logged exception and encryption.

Use synthetic or effectively anonymised test data by default. Pseudonymised personal data remains protected as personal data; keep re-identification keys separately. Lowering classification requires documented owner approval and Privacy review for personal data. Removing a label does not lower the underlying sensitivity.

Records must have an approved retention schedule tied to purpose and legal/contractual obligations. The Privacy Lead and Legal validate schedule entries rather than applying one blanket period. On expiry, delete primary data and account for replicas, exports and backup lifecycle. Backup copies may age out under a documented schedule with access restrictions; if restored, reapply required deletions. Suspend destruction when a legal hold applies and record release of the hold. Suppliers must provide deletion confirmation at termination where relevant.

## Operational responsibilities and assurance

Data owners classify and authorise use; IT enforces access, encryption and deletion; Privacy validates personal-data handling; all users minimise and protect information. Within 30 days of approval, owners must classify customer, HR and finance stores; remaining stores within 90 days. Security samples ten external shares monthly for recipient, permission and expiry accuracy. Targets: 100% priority stores with owners and labels, zero unauthorised public links to Confidential/Restricted data, and all overdue retention decisions assigned an owner and deadline.


## Compliance, exceptions and review

Managers must make these requirements available and provide practical support. Personnel must complete induction and acknowledge this policy before unsupervised access, with annual refreshers. Suspected non-compliance must be reported to the Security Lead without delay. HR handles alleged misconduct fairly under the employment process; an accidental report is not itself grounds for punishment. Supplier failures are managed under contract.

Exceptions require the recorded business reason, affected assets, risk assessment, compensating safeguards, owner, expiry and approval described in the [board paper](board-paper.md). No individual may approve their own exception. The owner reports overdue actions monthly to the COO and reviews effectiveness annually. Version changes and approvals are retained in the controlled policy register.
