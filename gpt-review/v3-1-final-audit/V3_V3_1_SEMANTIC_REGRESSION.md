# V3 to V3.1 Semantic Regression Audit

## Finding

One case-level semantic regression was found and corrected:

- **Seq 51 / Wistron-BMC-00175-V003** — V3 explicitly required each of
  TEMP_GB_HSC1–10 in both BMC Dashboard and Server Health > Sensor Reading.
  The shorter V3.1 record said only `Per-index UI capture`, which could be read
  as one page. The Final Audit restores both views as mandatory coverage and
  applies ED-31 `MANUAL ONLY`.

One report-only adjacent-domain defect was found:

- **Seq 19** was described as GDS/non-GDS in the V3.1 blocked summary. The V3
  and source row are an LTSSM/Intel SSV case. The actual review record retained
  the LTSSM intent; only the summary was wrong.

## No silent deletion rule

The audit found many concise V3.1 records whose V3 predecessors carry more
specific command tokens, topology fields, durations, evidence and recovery
steps. Treating the short overlay as a replacement would create broad semantic
loss. The logic is therefore corrected to make V3.1 and Final Audit additive:
omitted V3 detail remains effective unless explicitly superseded with a reason
and coverage effect.

The 200 audit records each link the exact V3 and V3.1 record and confirm the
case-specific inherited detail. This prevents abbreviation from deleting, for
example, RAS event types and loci, MLPerf model/scenario identity, fio profiles,
margin duration/coverage, firmware activation, or cycle evidence.

## Result

- Unrepaired intent regressions: **0**.
- Unrepaired command/procedure deletions: **0** under additive overlay order.
- Safety regressions introduced by corrections: **0**.
- Coverage reductions introduced by corrections: **0**.

