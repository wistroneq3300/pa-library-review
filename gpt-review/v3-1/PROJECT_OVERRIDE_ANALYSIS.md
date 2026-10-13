# V3.1 Project Override Analysis

## Contract

Every record separates four values:

1. `master_default`: immutable source intent/parameters.
2. `project_inputs`: platform-specific values and approved overrides.
3. `actual_execution`: what was actually run; all records currently say `NOT EXECUTED`.
4. `coverage_difference`: the gap between the approved run and Master requirement.

An approved project run may complete even when it is smaller than the Master default. It must not be reported as completion of the larger Master requirement, and no override updates the source library.

## Concrete boundaries

| Seq | Test case | Master default | Permitted project decision | Required coverage accounting |
|---:|---|---|---|---|
| 2 | Power-cycle WebUI test | 5 cycles and WebUI behavior | Approved count/tool and evidence plan | Fewer cycles are complete only for the project; API evidence cannot replace WebUI. |
| 6 | CPU stress | 225 workers, 8 hours | Workers/duration/profile adjusted to target CPU and project plan | Report workers, duration and load difference. |
| 17 | Long-term cycle | Source cycle count/method | Existing PA Manager Cycle or project script and approved count | Preserve all original attempts; extra retry is not a planned loop. |
| 18 | 40C margin test | 12 hours at source margin | Engineer may approve a shorter run | 240-minute Machine Time is not an override; a 4-hour run leaves an 8-hour gap. |
| 76 | CPU temperature | Collect all mapped sensors | Project supplies map/ranges | Missing Expected delays verdict, not Actual collection. |
| 123 | Storage performance | Source I/O profile/duration | Safe file/device and project profile | Target, profile, duration and threshold differences remain explicit. |
| 155 | AMD GPU lifecycle | Source loop/lifecycle intent | Project selects approved existing cycle mechanism | Count and state-transition differences are retained. |
| 176 | Idle stability | 24-hour awake idle | A 12-hour approved run may be executed | Project run can complete; Master still has a 12-hour gap. |
| 178 | Cold reboot margin | 100 cold cycles | Approved lower cycle count if justified | Actual count and missing cycles are reported; no warm substitution. |
| 183 | Warm reboot campaign | Source conflict: 500 cycles and 12 hours | Engineer chooses count, time, or both for the project | Project choice does not resolve the Master conflict. |
| 185 | Network stress | All CX-7/BF3 ports for one hour | Select exactly one of Ethernet/RoCE/InfiniBand with mode-specific tool | Modes and omitted ports cannot be merged into one coverage claim. |

## Approval and execution rules

- One authorized engineer can approve a fully specified run.
- Approval includes target identity, scope, method, important parameters, safety stops, evidence, and recovery.
- A new confirmation is required for a changed target, command, important parameter, destructive action, retry, recovery, installation or system change.
- A planned next loop is not a retry. A failed attempt remains in the ledger.
- Tool defaults are candidate values only after version/applicability/safety review and explicit confirmation.
- Official public documentation cannot replace private project Expected values.
