# Review run-lock protocol

Only one review runner may mutate the active overlay at a time.

At the start of an interactive or scheduled run, create the untracked
`gpt-review/.review_run_lock.json` with a run id, mode, start time, and heartbeat.
Refresh the heartbeat before each testcase. Remove the lock only after the run
has stopped cleanly or has persisted an invalid-run notice.

If a runner sees an existing lock, it must not write review data. It should
exit quietly when the lock is fresh. A stale or orphaned lock requires a visible
stop/repair decision; it must not be silently overwritten because doing so can
create duplicate or conflicting overlay records.

The lock is intentionally ignored by Git. The durable audit remains in the
per-testcase commits and `progress.json`.
