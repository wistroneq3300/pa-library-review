# Engineering Decision Re-review Handoff

- Completed formal queue: **874 / 942**; append-only active review events: **1025**.
- Last valid formal review: Compatibility|453|Wistron-AMD GPU-00150-V003 / 9b8ebbb362e91339 (formal queue sequence 874; review event 1025).
- Next directly verified pending identity: Compatibility|454|Wistron-AMD GPU-00149-V003 / 1cbede19494d71fe (first missing formal queue sequence 875).
- Latest valid disposition: Compatibility row453 is review-resolved as the distinct one-shot UMC replay correctable CRC-read `-b0 -s0 -t4 -a0x800` case. The tuple plus correlated CRC-read event content distinguishes it from adjacent UMC variants; exact target/stack/oracle/recovery remain separate ED-16 bindings. No driver load, injection, query, reset, log clearing or DUT action ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
