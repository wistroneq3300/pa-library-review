# BLOCKED Reclassification — V3 Pilot 200

## Result

- Historical V2 `BLOCKED`: 41 cases.
- V3 `BLOCKED`: 22 cases.
- Historical `BLOCKED` reclassified to a non-BLOCKED capability: 25 cases.
- Historical non-BLOCKED reclassified to V3 `BLOCKED`: 3 cases (79, 80, 92) because V3 identified unresolved semantic or safety conflicts that V2 had not treated as genuine blockers.
- Net BLOCKED reduction: 19. This is an observed result, not the quality target.

## Why 25 historical BLOCKED cases were released

The released cases fall into four evidence-based groups:

1. Missing provisionable SPEC/package/parameters, but a known technical operation remains automatable after handoff. Examples: 1, 2, 3, 5, 31, 41, 44, 46-48, 55-56, 59, 108, 167, 169, 185.
2. The end-to-end test contains an irreducible physical/manual boundary, so the correct capability is `MANUAL ONLY`, while missing inputs remain readiness gates. Examples: 4, 24, 26, 29, 171, 175, 180.
3. Missing Expected Value prevents PASS but not safe read-only Actual collection. Case 194 (`dmidecode --type 46`) is the clearest pilot example and is `FULLY AUTOMATABLE` with `NEEDS_SPEC` readiness.
4. Historical records 3 and 5 retained the user-confirmed non-BLOCKED boundary even though their V3 outcome did not need a cosmetic rewrite.

The full released sequence set is: `1, 2, 3, 4, 5, 24, 26, 29, 31, 41, 44, 46, 47, 48, 55, 56, 59, 108, 167, 169, 171, 175, 180, 185, 194`.

## Why 22 cases remain BLOCKED

V3 keeps BLOCKED only when the execution contract cannot be made safe or meaningful from the available source:

- Core semantics or acceptance absent: 19, 45, 54, 62, 64, 67, 73, 162, 163, 186, 199, 200.
- Contradictory source target/method that cannot be resolved by a parameter alone: 79, 80, 92.
- Fault-injection semantics or expected response not attributable: 103-107.
- WAT power/poll scenarios mix AC/DC tokens or omit the named management-side poll selector: 190-191.

For these cases V3 still permits explicitly listed read-only discovery, but discovery cannot be represented as completion or PASS.

## Safety conclusion

No BLOCKED release authorizes execution immediately. Reclassified cases retain `NEEDS_SPEC`, `NEEDS_PACKAGE`, `NEEDS_INPUT`, `NEEDS_APPROVAL`, `NEEDS_MANUAL_ACTION`, or `SOURCE_CONFLICT` gates as applicable. The release changes capability classification, not permission or readiness.
