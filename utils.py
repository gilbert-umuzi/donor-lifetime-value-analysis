import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the donor data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean and preprocess the donor data."""
    # Rename columns
    df = df.rename(columns={'Totan donations in 2022': 'Total donations in 2022',
                            'Was their first donation an automatically-recurring transaction?': 'recurring'})
    
    # Convert dollar columns to numerical (float)
    dollar_columns = ['Total donations in 2017', 'Total donations in 2018',
                      'Total donations in 2019', 'Total donations in 2020',
                      'Total donations in 2021', 'Total donations in 2022',
                      'Total donations in 2023', 'Amount of first donation',
                      'Amount of last donation', 'Highest amount donated in one year']

    def dollar_to_float(dollar_str):
        if isinstance(dollar_str, str):
            return round(float(dollar_str.replace('$', '').replace(',', '')), 2)
        return dollar_str

    for column in dollar_columns:
        df[column] = df[column].apply(dollar_to_float)

    # Convert date columns to datetime
    date_columns = ['Date of first donation', 'Date of last donation']
    df[date_columns] = df[date_columns].apply(pd.to_datetime, errors='coerce')

    # Handle missing values
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].fillna('Unknown')
        else:
            df[column] = df[column].fillna(0)

    # Create 'Total Gifts' column
    donation_columns = [f'Total donations in {year}' for year in range(2017, 2024)]
    df['Total Gifts'] = df[donation_columns].sum(axis=1)

    return df

# Load and clean the data
df = load_data('/content/donor_data.csv')
df = clean_data(df)

print(df.info())
df.head()

def plot_donation_distribution(df, column, title):
    """Plot the distribution of donations."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.xlabel('Donation Amount')
    plt.ylabel('Frequency')
    plt.show()

def calculate_retention_rate(df, year_col1, year_col2):
    """Calculate retention rate between two years."""
    donors_year1 = set(df[df[year_col1] > 0]['donor_id'])
    donors_year2 = set(df[df[year_col2] > 0]['donor_id'])
    retained_donors = donors_year1.intersection(donors_year2)
    return len(retained_donors) / len(donors_year1)

def segment_donors(df, amount_col):
    """Segment donors based on their total donation amount."""
    def assign_segment(amount):
        if amount < 1000:
            return 'Small'
        elif amount < 10000:
            return 'Medium'
        elif amount < 100000:
            return 'Large'
        else:
            return 'Major'
    
    df['Segment'] = df[amount_col].apply(assign_segment)
    return df

def plot_retention_heatmap(retention_matrix):
    """Plot a heatmap of retention rates."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(retention_matrix, annot=True, cmap='YlGnBu', fmt='.2f')
    plt.title('Donor Retention Rates by Segment and Year')
    plt.xlabel('Year')
    plt.ylabel('Donor Segment')
    plt.show()

# Add more utility functions as needed
