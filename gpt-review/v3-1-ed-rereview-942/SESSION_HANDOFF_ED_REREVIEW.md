# Engineering Decision Re-review Handoff

- Completed: **84 / 942**
- Last reviewed: `Functionality|895|Wistron-BMC-00185-V003` / `d6ab5472a6fee245`
- Next source-verified pending identity: `Functionality|896|Wistron-BMC-00186-V003` / `2f85faaf14985c9f`
- Latest disposition: SPD_FAN1_R through SPD_FAN16_R are removed from Pending as sixteen separately mapped R-labeled speed channels. The Project must define `_R` rather than the review assuming rear/redundant/reported semantics; `_F`, aggregate/count evidence, generic RPM limits, fan/airflow/load/control changes, log clear and unreviewed Script execution are prohibited.
- Protected sources: unchanged.
- DUT execution: none.
