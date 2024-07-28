# Donor Data

## Data Source
This directory should contain the donor data file `donor_data.csv` and `cmapaign_data.csv`.

## Data Structure
The `donor_data.csv` file should have the following columns with a sample of donor records:

- Unique donor ID: Unique identifier for each donor
- Total donations in {year} 2017-2023
- Amount of first donation
- Date of first donation
- Was their first donation an automatically-recurring transaction?: Boolean indicating if the donor has a recurring donation set up
- Amount of last donation
- Date of last donation
- Year with the most dollars donated
- Highest amount donated in one year

The `campaign_data.csv` file should have the following columns with 10 donor records collected in a recent donations campaign:

- Unique donor ID: Unique identifier for each donor
- Donation amount
- Date of first donation
- Date of last donation
- Was their first donation an automatically-recurring transaction?: Boolean indicating if the donor has a recurring donation set up

## Data Preprocessing
Before analysis, the data undergoes the following preprocessing steps:

1. Removal of any rows with missing values
2. Conversion of date strings to datetime objects
3. Calculation of derived features (e.g., donor age, total donation amount)

These steps are handled in the `load_and_clean_data` function in `utils.py`.
