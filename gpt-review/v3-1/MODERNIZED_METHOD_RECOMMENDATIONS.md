# V3.1 Modernized Method Recommendations

Modernized recommendations are additive. They never overwrite `Original Procedure` or `Original Command`, and an engineer chooses whether the project uses the original or recommended method.

## Verified public methods

| Cases | Recommendation | Applicability and version rule | Difference / coverage | Official technical reference |
|---|---|---|---|---|
| 193 | Use the installed NVIDIA `gdsio` with a safe mounted file, UUID-confirmed GPU and documented GDS/CPU transfer modes. | Exact CUDA/GDS/driver/filesystem support matrix; use the installed `gdsio -h` semantics. | Corrects ambiguous paths and creates a fair paired comparison; it does not authorize raw-device writes. | [NVIDIA GDS documentation](https://docs.nvidia.com/gpudirect-storage/), [Benchmarking and Configuration Guide](https://docs.nvidia.com/gpudirect-storage/configuration-guide/) |
| 194 | Keep `dmidecode --type 46` when the installed release supports SMBIOS Type 46; capture all handles and parent associations. | SMBIOS 3.5+ structure applicability and decoder support must be recorded. | Strengthens parsing; no functional replacement. | [DMTF SMBIOS DSP0134](https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.5.0.pdf) |
| 195–196 | Prefer the exact platform's advertised/vendor firmware update interface; retain WebUI when it is the tested/supported path. | Only when the target advertises the relevant UpdateService/OEM behavior and component inventory. | API orchestration cannot substitute for WebUI functional coverage or a vendor-specific activation/preservation contract. | [DMTF Redfish Specification](https://redfish.dmtf.org/schemas/DSP0266_1.12.0.html), [Redfish Firmware Update White Paper](https://www.dmtf.org/sites/default/files/standards/documents/DSP2062_1.1.0.pdf) |
| GPU diagnostic cases with an applicable public NVIDIA stack | Prefer project-approved DCGM Diagnostics for the paths it actually covers; preserve private NVQual/NVDiag/MODS scope separately. | Pin DCGM/GPU/driver/plugin availability and project parameters. | DCGM can cover active compute, memory, PCIe, NVLink, power and thermal diagnostics, but does not replace offline vendor qualification or formal engineer verdict. | [NVIDIA DCGM Diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/learn/modules/dcgm-diagnostics.html), [`dcgmi diag` reference](https://docs.nvidia.com/datacenter/dcgm/latest/reference/command-line-reference/dcgmi/dcgmi-diag.html) |
| 185 and other RDMA-mode performance cases | Use the benchmark that matches the approved network mode, with symmetric server/client parameters and explicit endpoints. | Pin perftest/driver/firmware and distinguish InfiniBand, RoCE and native Ethernet. | Prevents `ib_read_bw`, `ib_write_bw` and raw Ethernet from being treated as one test. | [linux-rdma perftest manual](https://github.com/linux-rdma/perftest/blob/master/man/perftest.1), [perftest project](https://github.com/linux-rdma/perftest) |
| Storage fio cases | Use a reviewed fio job against an exact approved file/device with identity and protection interlocks. | Pin fio version/ioengine and project I/O profile. | Adds target safety and reproducibility; official defaults do not supply private performance thresholds. | [fio documentation](https://fio.readthedocs.io/en/latest/fio_doc.html), [fio upstream](https://github.com/axboe/fio) |
| CPU/memory stress cases where stress-ng is selected by the project | Use a pinned stressor set, timeout/load and `--verify` only where that stressor supports verification. | Project-approved version and load/thermal limits. | Does not replace SST/vendor diagnostics or allow generic results to satisfy a private criterion. | [stress-ng upstream manual](https://github.com/ColinIanKing/stress-ng/blob/master/stress-ng.1) |

## Existing/private tool first

- PA Manager Cycle and approved project cycle scripts remain preferred for reboot/power campaigns.
- SST, WAT, NVDiag, NVQual, MODS and OEM firmware tools require their applicable official/private manuals or approved SOPs.
- No command was invented for a private tool. Cases 186, 190 and 191 stay BLOCKED until semantics are recovered.
- A successful tool exit is evidence, not the engineer's formal PASS.

## Functional non-substitution

- WebUI rendering/interaction tests remain WebUI tests; Redfish can provide corroborating data, not replacement coverage.
- BIOS Setup display tests remain firmware-UI observations; OS inventory is corroboration only.
- UID LED requires engineer visual confirmation even if the agent sends the control command.
- Network transport modes, MLPerf model/scenario pairs and firmware component types remain distinct.
