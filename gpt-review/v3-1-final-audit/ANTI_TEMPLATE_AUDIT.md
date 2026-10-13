# Anti-Template and Semantic Audit

## Mechanical candidate discovery

Pairwise similarity was used only to identify pairs for human inspection. It
did not assign an outcome. The highest similarities occurred in legitimately
related but still distinct pairs: cold versus warm reboot (178/181), +5%/40C
versus -5%/0C storage margin (171/180), adjacent MLPerf workloads, adjacent
SMBIOS structures, and adjacent RAS events.

## Manual findings

- No case was accepted solely because wording was unique.
- No classification was changed by keyword or regular expression.
- Similar MLPerf records retain different model, accuracy, scenario, dataset,
  metric and copied-criterion defects.
- Similar RAS records retain different event class, severity, target locus,
  native reporter, containment and stop behavior.
- Similar storage cases retain read/write/mix, QD, block size, target and
  endurance differences.
- Similar margin cases retain temperature, rail sign, device population,
  duration, workload, moisture and restoration differences.
- Similar cycle cases retain warm/cold/AC/DC waveform, count, readiness and
  per-device evidence differences.

## Defects discovered by semantic review

- Seq 19's blocked-summary GDS text was an adjacent-domain copy error.
- Seq 51's shortened evidence omitted the second required WebUI view.
- Ten `SOURCE_CONFLICT` flags conflated missing/unclear information with an
  actual contradiction.
- Seventeen automation labels conflicted with ED-30 or ED-31; each was changed
  only after case-specific review.

## Gate

All 200 records contain a unique `independent_semantic_finding`; exact source
identity and history links are preserved. Similarity candidates were manually
dispositioned and no unresolved neighbor-copy defect remains. **PASS**.

