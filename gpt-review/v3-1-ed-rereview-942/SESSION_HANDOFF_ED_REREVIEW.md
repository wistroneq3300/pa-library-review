# Engineering Decision Re-review Handoff

- Completed: **90 / 942**
- Last reviewed: `Functionality|901|Wistron-BMC-00191-V003` / `b71877c678ef1f6e`
- Next source-verified pending identity: `Functionality|902|Wistron-BMC-00192-V003` / `f08a204556a32718`
- Latest disposition: PWR_STBY_HSC is removed from Pending as one exact state-conditioned standby rail/controller check. It requires the current AC/PSU/host/BMC/HSC tuple and matching Project rule; numbered HSCs or other states cannot substitute, and no power transition or load is authorized.
- Protected sources: unchanged.
- DUT execution: none.
