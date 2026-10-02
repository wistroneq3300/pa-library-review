# Block Judgment Cases

Status: waiting for end-user judgment. These five cases were selected after the historical second-review backfill. They are intentionally different blocker types and are not new execution instructions.

## 1. Wistron-HW-00032-V004

- Source row: `Functionality/row-29`
- Test name: `Latch_on_fault_offset_To_Next_Block`
- Current GPT classification: `BLOCKED`
- Second-review outcome: `CHANGED`
- Blocker type: configuration-field semantics and acceptance value are not identified.

### Original testcase

- Items: `Latch_on_fault_offset_To_Next_Block`
- Procedure:

  ```text
  Before Test
  1. Check that the SUT configuration (e.g., hardware, firmware, drivers, etc.) matches the specifications/recipe definition.
  2. Clear logs (e.g., dmesg, syslog, SEL, etc.).

  During Test
  Offset in bytes from this location to the beginning of the next configuration block

  After Test
  1. Collect test results and photos, and save them to specific folders.
  2. Check if there are unexpected logs (e.g., dmesg, syslog, SEL, etc.) generate after test.
  ```

- Criteria: `Offset in bytes from this location to the beginning of the next configuration block`

### DeepSeek reference

- Classification: `NO`
- Package: `PSU vendor config-block decode tool (operator/vendor)`
- Command/review: verify the offset-in-bytes field between consecutive configuration blocks using the PSU vendor layout/VPD parser; the agent has no tool to dump the PMBus configuration blocks and the value is compared with a specification table.
- Evidence: vendor-tool output showing the offset and comparison to the specification table.

### GPT second review

- Purpose: validate the CRPS latch-on-fault configuration field representing the byte offset from the current block to the next block.
- Required package/input: PSU identity and firmware/VPD, vendor configuration-block layout, field address, block boundaries, byte order, expected offset, compatible read-only decoder, and recovery procedure.
- Test command: blocked until those inputs are supplied and validated; then use only the vendor-approved read-only decode and compare the raw field with the documented value.
- User confirmation: required before any PSU/BMC diagnostic access.
- Risks: guessing a PMBus command or blind-scanning can disturb the PSU interface; clearing logs would destroy evidence.
- Expected evidence: PSU identity/version, vendor tool/version, decoded current/next block locations, byte order, raw offset, documented expected value, and preserved BMC/SEL evidence.
- Blocked conditions: missing field location, block boundary, byte order, expected value, compatible read-only tool, safe recovery path, or confirmed PSU/BMC identity.

### User judgment

1. Should this remain `BLOCKED`, or should the vendor Application Note/Firmware Spec and decoder convert it to `REQUIRES PACKAGE / USER CONFIRMATION`?
2. Which exact minimum fields make the test executable: field address, block boundary, byte order, expected value, or all of them?
3. If the vendor supplies those inputs, should the agent be allowed to perform the read-only decode after explicit `OK`?

## 2. Wistron-HW-00070-V004

- Source row: `Functionality/row-67`
- Test name: `FW upgrade/downgrade`
- Current GPT classification: `BLOCKED`
- Second-review outcome: `CHANGED`
- Blocker type: firmware target identity, image integrity, sequence, and recovery are undefined.

### Original testcase

- Items: `FW upgrade/downgrade`
- Procedure:

  ```text
  Before Test
  1. Check that the SUT configuration (e.g., hardware, firmware, drivers, etc.) matches the specifications/recipe definition.
  2. Clear logs (e.g., dmesg, syslog, SEL, etc.).

  During Test
  1. Enter BMC ip address into web browser. (Must use "https://<BMC ip>") and enter account/password.
  2. Select "Maintenance/HPM firmware update" page.
  3. Update the PSU firmware and click the button to do.
  4. Wait a minutes and reboot the system. Re-login the web page to ensure the PSU firmware update successfully.
  5. Repeat N & N-1 firmware update 5 times.

  After Test
  1. Collect test results and photos, and save them to specific folders.
  2. Check if there are unexpected logs (e.g., dmesg, syslog, SEL, etc.) generate after test.
  ```

- Criteria:

  ```text
  1. Login BMC webUI successfully.
  2. Find the page.
  3. PSU firmware update successfully without issue.
  4. SUT can power cycle without issue.
  ```

### DeepSeek reference

- Classification: `PARTIAL`
- Package: `ipmitool`, user-provided PSU firmware image.
- Command/review: perform a user-supplied PSU firmware upgrade/downgrade through the vendor/BMC flash path, then collect PSU sensor and firmware-version readback over `ipmitool -I lanplus -C 17`.
- Evidence: PSU sensor and firmware-version readback after the user completes the flash.
- Risk: PSU reset/output interruption; maintenance window and recovery plan required.

### GPT second review

- Purpose: perform the specified PSU firmware upgrade/downgrade sequence through BMC HPM, including the undefined N and N-1 versions repeated five times, then verify firmware and power-cycle recovery.
- Required package/input: exact PSU identity/slot, current firmware, signed N and N-1 images and hashes, compatibility manifest, downgrade authorization, HPM method, five-cycle sequence, maintenance window, qualified operator, redundancy plan, and recovery/replacement path.
- Test command: blocked; do not upload, flash, reset, reboot, or power-cycle until all target and recovery facts are validated. After approval, collect read-only PSU sensor and firmware readback.
- User confirmation: required before every firmware mutation sequence.
- Risks: a PSU flash can reset output; repeated cycles and a SUT power cycle can interrupt workloads or leave the power path unstable.
- Expected evidence: pre/post PSU FRU/slot/version, image hashes, HPM result for each cycle, BMC reconnect, sensor/version readback, SEL/host/power evidence, and controlled recovery.
- Blocked conditions: any missing identity/image/hash/signature, sequence, HPM method, authorization, redundancy, maintenance window, or recovery path.

### User judgment

1. Should this be `BLOCKED` until all firmware and recovery parameters are supplied, or `REQUIRES PACKAGE / USER CONFIRMATION` once the vendor provides the firmware and flash command?
2. Is “repeat N and N-1 five times” itself a blocker until the exact order and success criterion are stated?
3. Which evidence is mandatory before allowing the first flash?

## 3. Wistron-HW-00153-V002

- Source row: `Functionality/row-150`
- Test name: `OS installing`
- Current GPT classification: `BLOCKED`
- Second-review outcome: `CHANGED`
- Blocker type: the requested TPM state transition and installation target are ambiguous and potentially destructive.

### Original testcase

- Items: `OS installing`
- Procedure:

  ```text
  Before Test
  1. Check that the SUT configuration (e.g., hardware, firmware, drivers, etc.) matches the specifications/recipe definition.
  2. Clear logs (e.g., dmesg, syslog, SEL, etc.).

  During Test
  Verify can revise TPM setting or not.

  After Test
  1. Collect test results and photos, and save them to specific folders.
  2. Check if there are unexpected logs (e.g., dmesg, syslog, SEL, etc.) generate after test.
  ```

- Criteria: `Verify can revise TPM setting or not.`

### DeepSeek reference

- Classification: `PARTIAL`
- Package: user-provided OS installer media and `tpm2-tools` for post-install checks.
- Command/review: stage a clean OS installation with TPM enabled, then check `/dev/tpm0`, TPM-related `dmesg`, and `systemd-cryptenroll --tpm2-device list`.
- Evidence: post-install TPM visibility in the installed OS.
- Risk: OS installation may repartition storage; use a dedicated user-designated SUT/drive.

### GPT second review

- Purpose: determine whether a TPM setting can be changed in an OS-installation context, but the source does not identify the setting, starting/final state, installation target, OS image, or success condition.
- Required package/input: exact TPM/BIOS action and states, OS image, dedicated disposable target, TPM/Secure Boot specification, backup, and OOB/reimage recovery.
- Test command: blocked; do not copy the TPM-enabled installation flow, change TPM state, clear TPM, or guess a storage target until the operation is defined and re-reviewed.
- User confirmation: required for any OS installation, storage change, TPM operation, or Secure Boot change.
- Risks: wrong storage target can destroy data; TPM/Secure Boot changes can affect measured boot, keys, and unlock behavior.
- Expected evidence: resolved action/state transition, target/image identity, before/after TPM and boot evidence, target-only storage impact, restoration, and final boot/service health.
- Blocked conditions: missing TPM action/state, OS image/target, acceptance criteria, backup, or recovery path; unsafe/unknown storage target; unapproved key/security impact.

### User judgment

1. Is this a normal hybrid/manual test that should become `REQUIRES PACKAGE / USER CONFIRMATION` after the OS image, target, and TPM action are supplied?
2. Does “revise TPM setting” need an exact BIOS setting and before/after state before review can proceed?
3. Must the dedicated target and recovery plan be treated as prerequisites rather than a permanent block?

## 4. Wistron-HW-00207-V002

- Source row: `Functionality/row-198`
- Test name: `Communication check`
- Current GPT classification: `BLOCKED`
- Second-review outcome: `CHANGED`
- Blocker type: serial electrical identity, parameters, peer behavior, and acceptance response are unspecified.

### Original testcase

- Items: `Communication check`
- Procedure:

  ```text
  Before Test
  1. Check that the SUT configuration (e.g., hardware, firmware, drivers, etc.) matches the specifications/recipe definition.
  2. Clear logs (e.g., dmesg, syslog, SEL, etc.).

  During Test
  Check the communication function
  1. Plug the cable between serial port and client.
  2. Make the connection and input some useful command to check the communication.

  After Test
  1. Collect test results and photos, and save them to specific folders.
  2. Check if there are unexpected logs (e.g., dmesg, syslog, SEL, etc.) generate after test.
  ```

- Criteria: `Make sure the communication work normally.`

### DeepSeek reference

- Classification: `NO`
- Package: serial cable and a client terminal/operator.
- Command/review: an operator physically connects the SUT COM port to a client, types commands, and verifies the link; the agent cannot wire or observe the serial link over SSH.
- Evidence: operator connection and bidirectional communication confirmation.

### GPT second review

- Purpose: verify two-way communication between the SUT serial port and a client terminal using an approved cable and protocol.
- Required package/input: serial standard/pinout, exact port, baud/data/parity/stop/flow settings, client role, harmless test payload, expected response, timeout, authorization, and alternate/OOB console.
- Test command: blocked; do not connect an unknown cable or type an unspecified command. Re-review after the serial test definition is complete.
- User confirmation: required before the physical connection and any terminal input.
- Risks: wrong port/electrical path can damage hardware or affect a console; “useful command” is not a reproducible acceptance test.
- Expected evidence: port/pinout/settings, operator connection record, timestamped bidirectional transcript, clean termination/restoration, and no console impact.
- Blocked conditions: missing serial port/standard/pinout, cable, settings, peer role, payload/response, timeout, operator, alternate console, or recovery.

### User judgment

1. Is the missing serial specification a true `BLOCKED` condition, or should the case become `REQUIRES PACKAGE / USER CONFIRMATION` when the vendor/owner supplies it?
2. Is physical cable insertion alone enough to classify this as `MANUAL ONLY`, with the serial parameters treated as operator inputs?
3. What exact harmless payload and expected response should be required?

## 5. Wistron-HW-00210-V002

- Source row: `Functionality/row-201`
- Test name: `Devcie detection`
- Current GPT classification: `BLOCKED`
- Second-review outcome: `CHANGED`
- Blocker type: USB port coverage, test-device identity, BIOS/OS meaning of detection, and safety limits are unspecified.

### Original testcase

- Items: `Devcie detection`
- Procedure:

  ```text
  Before Test
  1. Check that the SUT configuration (e.g., hardware, firmware, drivers, etc.) matches the specifications/recipe definition.
  2. Clear logs (e.g., dmesg, syslog, SEL, etc.).

  During Test
  Check all usb port could detect device
  All USB port can be detected in BIOS/OS

  After Test
  1. Collect test results and photos, and save them to specific folders.
  2. Check if there are unexpected logs (e.g., dmesg, syslog, SEL, etc.) generate after test.
  ```

- Criteria: `Make sure the devices can be detected under OS`

### DeepSeek reference

- Classification: `PARTIAL`
- Package: `usbutils` and an operator to attach the device.
- Command/review: use `lsusb` and `ip link` with the device present; the operator handles physical setup and BIOS view.
- Evidence: OS USB/device list for user confirmation.

### GPT second review

- Purpose: verify every specified USB port detects an approved test device in BIOS and OS.
- Required package/input: physical port/controller map, approved USB device/driver/VID/PID/serial matrix, BIOS/KVM method, definition of “detected,” power/security limits, `usbutils`, operator, and recovery path.
- Test command: blocked; do not attach arbitrary, bootable, storage, input, or security devices and do not claim all-port coverage from one `lsusb` snapshot. Re-review per port after the matrix is supplied.
- User confirmation: required before each physical attachment and any device with storage, boot, input, or security impact.
- Risks: arbitrary devices can mount storage, affect boot/input/security, exceed power limits, or disturb the USB controller; clearing logs destroys useful evidence.
- Expected evidence: per-port operator identity/connection record, BIOS detection capture, OS enumeration/driver evidence, no unexpected mounts/power/controller errors, complete coverage, and restored state.
- Blocked conditions: missing port inventory/controller mapping, device matrix, BIOS/OS acceptance definition, safety/recovery path, approved device, or operator/KVM access.

### User judgment

1. Should this be `BLOCKED` until the port/device/BIOS matrix is defined, or `REQUIRES PACKAGE / USER CONFIRMATION` because the OS `lsusb` portion is automatable after physical setup?
2. Is “detected” enumeration only, or must the device be usable/readable?
3. Should each USB port be split into its own testcase with a known-good device and explicit BIOS/OS evidence?

## Requested response format

For each case, please state: `KEEP BLOCKED` or the replacement classification, the minimum missing inputs, and whether the case should be split into an automatable portion plus a manual/operator portion.

## Judgment received

The end-user judgments for all five selected cases are recorded in
`gpt-review/BLOCKED_FEEDBACK_REREVIEW_001.json`. The confirmed boundary rules
are now incorporated into `gpt-review/BLOCKED_REVIEW_LOGIC_AND_SELECTION_001.md`,
`gpt-review/REVIEW_WORKFLOW_LOGIC_GPT_SECOND_REVIEW.md`, and
`pa-library-review-skill/SKILL.md`. This original prompt is retained as the
historical five-case judgment record; the follow-up file holds the resulting
case-specific classifications and questions.
