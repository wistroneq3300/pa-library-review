# Invalid Review Run Notice — Sequences 1372–1425

- Detected: 2026-10-18
- Last valid checkpoint: 1371
- Last valid commit: `09c3e67` (`review: independently review sequence 1371`)
- Affected active records: review sequences 1372 through 1425 (54 records)
- Disposition: moved intact into this isolation directory; excluded from effective `completed_count`

## Integrity failures

1. Starting at sequence 1372, a shared record-construction scaffold was used across multiple cases to increase throughput. Although individual source rows were extracted and case-specific text was supplied, this is prohibited by the GPU Server SIT review policy because it creates template pressure and is not an acceptable substitute for one-row-at-a-time independent review.
2. At sequence 1392, the proposed next source identity used an inferred version/variant before the Validator rejected it. The correct next row was subsequently read, but the attempted inferred checkpoint is an integrity trigger.
3. At sequence 1410, the next Variant ID was guessed incorrectly before the Validator rejected it. The progress value was corrected before commit, but the attempt confirms that next-row identity was not consistently copied directly from source before writing.

## Recovery

The active review set and `PROGRESS.json` are restored to checkpoint 1371. The quarantined records remain preserved for audit and are not counted. Re-review must restart at `Functionality|1223|Wistron-BMC-00513-V003` / `2c70d48440102ca8`, reading and committing exactly one XLSX row at a time with the actual next row verified before each write. No Master XLSX, formal JSON, approved engineering decision, or earlier valid Review Record is modified.
