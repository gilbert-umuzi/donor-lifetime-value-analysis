import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(file_path):
    """Load and clean the donor data."""
    df = pd.read_csv(file_path)
    # Add your data cleaning steps here
    return df

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
