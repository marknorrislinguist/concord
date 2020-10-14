# What is concord?

A home for the scripts I write to process/manage the data for the concord typology (static archive at SHAREOK: [Nominal concord](https://shareok.org/handle/11244/320354); academic project archived here: [Nominal concord at OSF](https://osf.io/tm49q/).

## Contents

### conctypo-data/
This directory contains all of the JSON files containing the coded data for the project. 

### lgs_with_wals.csv
This CSV contains all of the processed data as one CSV, including cross-referenced WALS data that is relevant for the project. Some of the WALS data was coded by me (as opposed to the author of the original WALS chapters). Those cells end with an asterisk `*`.

### conctypo-to-csv.py
Processes individual JSON files and saves the data as one CSV. Command to run the script:

`python conctypo-to-csv.py [-s] [-n] [-d]`

Optional arguments for desired sample (s; options are 'WALS-100', 'WALS-174','Hasp-100' or nothing. Defaults to nothing, which gathers all data),  directory where data is locatied (d; defaults to 'conctypo-data/' in the same folder as the script), and filename for the csv (n; defaults to `conctypo-data.csv`).

Output contains relevant classificatory data for the languages (based on [WALS](https://wals.info/) and [Glottolog](https://glottolog.org/)) as well as the values for the each of the CATegories Dem(onstrative), Num(eral > 1), Adj(ective):

  - Exist_CAT: does CAT exist in the language? (primarily relevant for Adjectives, which do not exist in some languages)
  - Gender_CAT: does CAT show gender concord?
  - Number_CAT: does CAT show number concord?
  - Case_CAT: does CAT show case concord?
  
 "Yes" is coded 1, "No" is coded 0.
