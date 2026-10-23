# Engineering Decision Re-review Handoff

- Completed: **27 / 942**
- Last reviewed: `Functionality|837|Wistron-BMC-00127-V004` / `fe77cf6bf08ded24`
- Next source-verified pending identity: `Functionality|838|Wistron-BMC-00128-V005` / `170cd88928d895b9`
- Latest disposition: The general ipmitool live-SOL case is removed from Pending with separate proof of client/payload establishment and recognizable target console content. It preserves its own ipmitool compatibility identity, uses protected password prompting, checks the current session owner, runs one bounded PTY and verifies documented escape/cleanup without `head` or automatic retry.
- Protected sources: unchanged.
- DUT execution: none.
