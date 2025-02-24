# This repository contains a demo data project with the following structure:

git repository:
- sources: contains python scripts that generate data (api or py packages)
-   raw_files: the output is then saved to the folder in the corresponding format (json dump for api or csv)
- toPostgres: using dlt, the files are saved to a local postgres which is run in a docker container


