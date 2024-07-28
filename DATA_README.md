# Donor Data

## Data Source
This directory should contain the donor data file `donor_data.csv` and `cmapaign_data.csv`.

## Data Structure
The `donor_data.csv` file should have the following columns:

- Unique donor ID: Unique identifier for each donor
- Donation amount: Amount of the donor's first donation
- Date of first donation: Date of the donor's first donation
- Was their first donation an automatically-recurring transaction?: Boolean indicating if the donor has a recurring donation set up
- Date of last donation: Date of the donor's most recent donation

## Data Preprocessing
Before analysis, the data undergoes the following preprocessing steps:

1. Removal of any rows with missing values
2. Conversion of date strings to datetime objects
3. Calculation of derived features (e.g., donor age, total donation amount)

These steps are handled in the `load_and_clean_data` function in `utils.py`.
