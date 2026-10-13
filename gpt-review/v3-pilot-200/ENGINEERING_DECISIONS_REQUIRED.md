# Engineering Decisions Required

The following inputs remain outside the reviewer's authority. They must be supplied by the named owner before execution or PASS disposition.

## Platform and acceptance specifications

- Golden SMBIOS/FRU/firmware/inventory values, field-level comparison rules, optional-record policy and applicable platform revision.
- Numeric performance thresholds and tolerances for GEMM, GDS, NIC/RDMA traffic, storage and GPU workloads.
- Exact duration/iteration precedence where source metadata conflicts with procedure text, including cases 170-180 and the 500-cycle/12-hour conflict in case 183.
- Authoritative meaning and command semantics for proprietary AMD, NVIDIA, WAT, MODS, Memeye and vendor BMC/CPLD tools.

## Hardware and topology ownership

- Stable UUID/BDF/slot/controller/enclosure/namespace/port mappings for GPUs, PCIe functions, storage bays, USB paths, NIC/RDMA ports and management-side devices.
- Explicit inclusion, empty/N/A and protected-device disposition for all-bay/all-slot cases.
- Ethernet versus RoCE versus InfiniBand transport, host versus DPU execution location, peer roles and both endpoint commands.
- GPU fabric, storage/GDS compatibility and platform-specific feature applicability; no cross-platform value is assumed.

## Destructive or state-changing operations

- Disposable storage targets, exact I/O ranges, RAID/filesystem/data ownership, integrity method, backup and recovery.
- Fault-injection event/flag/address mapping, expected CE/UE delta, one-injection rule and recovery.
- Reboot/AC/DC waveform, dwell, boot-ready signal, immutable cycle/failure/retry policy and OOB recovery.
- Firmware image provenance, component identity, compatibility, signature/hash, activation sequence, configuration/security preservation and rollback.

## Environmental margin tests

- Named 5 V/3.3 V rails, nominal and margin setpoints, control and independent measurement points, tolerances, calibration, soak/ramp/restore sequence.
- Chamber tolerance, humidity/dew-point and condensation limits, stabilization and controlled warm-up.
- Qualified operator, emergency stop, evidence cadence and device-specific abort thresholds.

## Credentials, packages and evidence

- Approved secret-delivery mechanism; credentials must not appear in commands or retained logs.
- Tool package provenance, version/hash/license, supported platform matrix and authoritative help/SOP.
- Evidence storage capacity, clock synchronization, retention path, log baseline/cursor method and anomaly allowlist.

Read-only discovery may continue only where the individual record permits it. It never resolves a missing acceptance reference by itself.
