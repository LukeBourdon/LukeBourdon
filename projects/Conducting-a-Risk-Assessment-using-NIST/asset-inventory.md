# Asset inventory and criticality

Fictional baseline. C/I/A criticality uses the 1–5 business impact scale in the [method](methodology.md), independently of the data label. Store/customer-level inventories would be required operationally.

| ID | Asset | Owner | Classification | C | I | A | Business rationale | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | Customer production database | Head of Engineering | Restricted | 5 | 5 | 4 | 40,000 contacts and workflow records; disclosure harms customers; corruption stops reliable service | Cloud production / identity / backups |
| A02 | Corporate identity and privileged accounts | IT Manager | Restricted | 5 | 5 | 5 | Central access to all services; compromise gives broad reach | Identity provider / recovery accounts |
| A03 | Customer SaaS application | Head of Engineering | Confidential | 4 | 5 | 5 | Revenue-critical service; target RTO 8h and RPO 4h | Cloud / database / deployment pipeline |
| A04 | Source code and delivery pipeline | Head of Engineering | Confidential | 4 | 5 | 4 | Code theft and malicious deployment risk | Repositories / developer identities / dependencies |
| A05 | 120 workforce laptops | IT Manager | Confidential | 4 | 4 | 3 | 12 unmanaged devices create inconsistent security | Identity / endpoint management |
| A06 | HR and payroll information | People Lead | Restricted | 5 | 4 | 3 | Bank details and limited employee health data | HR SaaS / People team access |
| A07 | Email and collaboration | IT Manager | Confidential | 4 | 4 | 4 | Impersonation and external sharing pathways | Identity / email provider |
| A08 | Backups and recovery materials | Head of Engineering | Restricted | 5 | 5 | 5 | Last-resort restore capability and secrets | Cloud backup / encryption keys |
| A09 | Support ticketing and exports | Customer Operations Lead | Confidential | 4 | 4 | 4 | Customer information and service coordination | Support vendor / corporate identity |
| A10 | Office network and equipment | Facilities Lead | Internal | 2 | 3 | 3 | Physical entry and local connectivity | Landlord / ISP / power |
| A11 | Supplier relationships and contracts | Procurement Lead | Confidential | 4 | 4 | 3 | Dependency, contractual and data processing exposure | Procurement / Legal / supplier assurance |
| A12 | People and operational knowledge | COO | Internal | 2 | 4 | 4 | Key-person dependency in recovery and incident response | Training / runbooks / deputies |
