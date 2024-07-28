# Donor Data

## Data Source
This directory should contain the donor data file `donor_data.csv`. Due to privacy concerns, the actual data is not included in this repository.

## Data Structure
The `donor_data.csv` file should have the following columns:

- donor_id: Unique identifier for each donor
- first_donation_amount: Amount of the donor's first donation
- first_donation_date: Date of the donor's first donation
- total_donations: Total amount donated to date
- is_recurring: Boolean indicating if the donor has a recurring donation set up
- donation_frequency: Frequency of donations (e.g., monthly, quarterly, annually)
- last_donation_date: Date of the donor's most recent donation

Additional columns for yearly donations:
- donations_2017, donations_2018, ..., donations_2023

## Obtaining the Data
To run this analysis with your own data:

1. Prepare a CSV file with the structure described above.
2. Ensure all monetary values are in the same currency and numerical format.
3. Place the CSV file in this directory with the name `donor_data.csv`.

## Data Preprocessing
Before analysis, the data undergoes the following preprocessing steps:

1. Removal of any rows with missing values
2. Conversion of date strings to datetime objects
3. Calculation of derived features (e.g., donor age, total donation amount)

These steps are handled in the `load_and_clean_data` function in `utils.py`.

## Data Privacy
Ensure that any data used complies with privacy regulations and has been properly anonymized before use.
