import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

class DonorLTVModel:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        
    def preprocess_data(self, df):
        # Add your preprocessing steps here
        # Example:
        df['log_first_donation'] = np.log1p(df['first_donation_amount'])
        df['donor_age'] = (pd.Timestamp.now() - df['first_donation_date']).dt.days / 365
        return df
    
    def engineer_features(self, df):
        # Add your feature engineering steps here
        # Example:
        features = ['log_first_donation', 'donor_age', 'is_recurring']
        X = df[features]
        y = df['total_donations']
        return X, y
    
    def fit(self, X, y):
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
    
    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    def calculate_ltv(self, prediction, retention_rate, time_horizon=5):
        # Implement your LTV calculation logic here
        # Example: Simple NPV calculation
        discount_rate = 0.1  # 10% annual discount rate
        ltv = sum(prediction * (retention_rate ** t) / (1 + discount_rate) ** t 
                  for t in range(1, time_horizon + 1))
        return ltv

# Usage example
if __name__ == "__main__":
    # Load your data
    df = pd.read_csv('data/donor_data.csv')
    
    ltv_model = DonorLTVModel()
    df = ltv_model.preprocess_data(df)
    X, y = ltv_model.engineer_features(df)
    
    ltv_model.fit(X, y)
    
    # Example prediction
    new_donor = pd.DataFrame({
        'log_first_donation': [np.log1p(100)],
        'donor_age': [0.5],
        'is_recurring': [1]
    })
    
    predicted_donation = ltv_model.predict(new_donor)[0]
    ltv = ltv_model.calculate_ltv(predicted_donation, retention_rate=0.8)
    
    print(f"Predicted LTV: ${ltv:.2f}")
