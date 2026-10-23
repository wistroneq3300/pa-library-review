# Review-event 0200 Integrity Reconciliation

Status: **CHECKPOINT REJECTED; NOT PUSHED; CORRECTION IN PROGRESS**

The required 200-event checkpoint rebuilt the formal 942-case queue from the
approved pending identities and Master-order selection manifest. The rebuilt
queue contains 942 unique Source Keys and reproduces the locked SHA-256
`8f3820c5c7f3bb4e126c32cc6b3385fb1a34f1fff5ae406c4a1eb14e9e9b0afc`.

The overlay first diverges at review event 14: the expected identity is
`Functionality|764|Wistron-BMC-00054-V003` / `8fbac8dbe0aa1e64`, but the event
record reviewed row 765. Across events 1-200, 49 unique records are members of
the formal queue and 151 are outside this requested 942-case scope.

No history is reset, deleted or force-pushed. The 151 records remain immutable
review evidence but are excluded from the 942-case metrics. The 49 formal-queue
records retain exact manifest identity and row hashes and have no exact
anti-template duplicate group. Their corrected effective state is:

- Completed: 49 / 942; remaining: 893.
- Engineering Decision Pending: 900.
- Source Conflict: 885.
- BLOCKED: 184.
- Fully Automatable: 497.
- Requires Package / User Confirmation: 1891.
- Manual Only: 540.

Nineteen early adopted records predate the explicit `project_authority` field
while using the same schema label. The exact exception set is hash-locked in
`SCOPE_RECONCILIATION.json`; their ownership and runtime requirements remain in
their decision basis, packages, safety gate and pending fields. New records may
not use this exception.

The first missing formal identity is queue sequence 14, Functionality row 764,
`Wistron-BMC-00054-V003` / `8fbac8dbe0aa1e64`. Review events remain append-only;
the next event number is 201. Push is withheld until 200 unique formal queue
identities pass the overlay validator.

Protected Master XLSX/formal JSON/GPT V2/historical records are unchanged. No
DUT command, test, log clear, firmware flash, write, reset or power action ran.
