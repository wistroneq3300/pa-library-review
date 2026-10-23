# Engineering Decision Re-review Handoff

- Completed: **179 / 942**
- Last reviewed: `Functionality|993|Wistron-BMC-00283-V004` / `818840293d936fe4`
- Next source-verified pending identity: `Functionality|994|Wistron-BMC-00284-V004` / `b804dc50fc09ee4a`
- Latest disposition: BMC Cold Reset (IB) is removed from Pending as a parameterized REQUIRES CONFIRMATION case. It preserves raw 0x06/0x02 and requires independent reset/readiness, unchanged MAC/IP/configuration, functional management services and unchanged host power/boot; fixed sleep or mc-info-only proof is rejected. No action ran.
- Protected sources: unchanged.
- DUT execution: none.
