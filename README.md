# This repository contains a demo data project with the following structure:

![grafik](https://github.com/user-attachments/assets/5f3c0627-8ae6-44cf-b8e3-96b9a12996fe)




**E&L with python and dlt**
- sources: contains python scripts that generate data (api or py packages)
  - raw_files: the output is then saved to the folder in the corresponding format (json dump for api or csv)
- toPostgres: using dlt, the files are saved to a local postgres which is run in a docker container
- The "ingestion_run_all.py" file showcases a basic file, that runs all .py files in the mother directory. Said script can be run via autoscheduler via Windows in case of an on-prem scenario.


**Transformations with dbt**
- For each source a source transformation with slight adjustments to the source files are completed (prefix "s_")
- The date table is enriched by joining the holidays data for germany, "by".
- Two snapshots are created for the "items" table. The first is build on the source, the second on a staging model. Both showcase a SCD type 2 table.


