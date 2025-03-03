# This repository contains a demo data project with the following structure:

git repository:

**E&L with python and dlt**
- sources: contains python scripts that generate data (api or py packages)
  - raw_files: the output is then saved to the folder in the corresponding format (json dump for api or csv)
- toPostgres: using dlt, the files are saved to a local postgres which is run in a docker container


**Transformations with dbt**
- For each source a source transformation with slight adjustments to the source files are completed (prefix "s_")
- The date table is enriched by joining the holidays data for germany, "by".


