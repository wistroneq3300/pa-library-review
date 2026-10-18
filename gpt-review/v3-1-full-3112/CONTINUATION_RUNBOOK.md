# V3.1 Review Continuation Runbook

## Runtime limitation

Codex review reasoning runs inside finite conversation or heartbeat turns. A heartbeat schedules a new bounded turn; it is not a persistent worker and cannot keep an ended turn alive. The repository therefore treats each turn as a resumable segment whose durable state is the Git commit, `PROGRESS.json`, Review Records and an expiring lease.

## Evidence from the 1,267 checkpoint diagnosis

- The heartbeat was active at a five-minute interval.
- Recent heartbeat turns completed after roughly 53–150 seconds and each returned after one or two records.
- No `validate_full_review.py`, extraction, or review-runner process remained after a turn. Only the Codex host and the currently executing shell were present.
- The legacy lock contained no PID or expiry, so it could not prove a worker was alive. Its timestamp was refreshed only while a turn was active.
- The full validator passed at 1,267. There were 1,067 unique new record files with continuous review sequences 201–1,267; adding the locked 200-record baseline yielded 1,267.

The stopping cause was therefore bounded Codex turns that explicitly finalized after a small number of records, not validator failure, a review script exit, or a confirmed competing lock holder.

## Repaired continuation model

1. Run `tools/review_run_guard.py status` and the full validator.
2. Acquire a 30-minute lease for the current thread/run. A live lease owned by another run blocks writes.
3. An expired `ACTIVE` lease is reported as `STALE_REQUIRES_AUDIT`; the guard does not delete or replace it. Confirm no review turn/process is active before creating a replacement run.
4. Review at least 10 sequential cases in the bounded turn unless a genuine semantic, safety, integrity, context, or execution-limit stop occurs.
5. For every case: read current and next XLSX rows plus all references, write one record, increment once, validate, protected-source check, commit once, then refresh the lease.
6. At normal turn end mark the lease `IDLE` with exact count, next key, commit and stop reason. The next turn reacquires from that checkpoint.
7. Never claim work continues after a turn ends. The active heartbeat merely schedules the next bounded segment.

The heartbeat interval is 15 minutes and its prompt requires a 10-case segment. This avoids overlapping short turns while preserving resumability. Push checkpoints remain 2,000, 2,500, 3,000 and 3,112.
