# GPT Second Review Batch 002

- Scope: Functionality source rows 17-216 (200 cases).
- Reviewed this batch: 200
- Classification summary: BLOCKED: 5, FULLY AUTOMATABLE: 3, MANUAL ONLY: 88, REQUIRES PACKAGE / USER CONFIRMATION: 104
- Original source files: unchanged and hash-verified.

## Review rules applied

- Testcase records remain in English; the later agent reports pre-check facts and requests OK in Chinese before execution.
- BMC/I2C/I3C, firmware, power, network, thermal, stress, and service-impacting actions require the applicable specification, parameters, recovery path, and user approval.
- Physical actions are MANUAL ONLY; the agent may collect evidence after an operator performs them.
- The Ubuntu DUT constraint blocks Windows-only BitLocker/VGA-driver/PassMark procedures unless an approved Linux replacement is supplied.
- PASS / FAIL / BLOCKED remain end-user decisions; the agent returns evidence only.

## Common findings

- The source library frequently uses generic criteria such as "match SPEC" without naming the specification, target, address, threshold, or expected output.
- DeepSeek YES/PARTIAL is not sufficient authorization for state-changing operations.
- BMC/LAN changes require an out-of-band recovery path so the agent does not disconnect itself.
- Firmware, thermal, power-cycle, stress, and fault-injection cases require explicit approval and recovery planning.

The next sequential case is Wistron-HW-00226-V002.
