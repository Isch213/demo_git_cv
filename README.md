# This repository contains a demo data project with the following structure:

![grafik](https://github.com/user-attachments/assets/5f3c0627-8ae6-44cf-b8e3-96b9a12996fe)




**E&L with python and dlt** // Folder structure
- cv_postgres: dbt project folder
- schemas: dlt schema folder
- sources: contains python scripts that generate data (api or py packages)
  - raw_files: the output is then saved to the folder in the corresponding format (json dump for api or csv)
- toPostgres: using dlt, the files are saved to a local postgres which is run in a docker container
  



**Transformations with dbt**
- For each source a source transformation with slight adjustments to the source files are completed (prefix "s_")
- The date table is enriched by joining the holidays data for germany, subdivision (~state) bayern.
- Two snapshots are created for the "items" table. The first is build on the source, the second on a staging model. Both showcase a SCD type 2 table.
  - The snapshots are not triggered via normal "dbt run" command but need to be triggered seperately. Take notice that the second snapshot relies on a model, therefore the snapshot command should be run AFTER the models have been run.


**scheduler**
- As this models an on-prem approach, a scheduler was not implemented. however for ease of use, all the relevant ingestion steps are triggered in the ingestion_run_all.py file.
- Similar, all the dbt relevant commands are triggered via the dbt_all.cmd file.
- Both files can be added to the win autoscheduler to create automatic runs.

