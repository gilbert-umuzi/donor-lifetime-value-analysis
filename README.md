# Nonprofit Donor Lifetime Value Analysis

## Project Overview
This project analyzes donor data for a nonprofit organization to develop a Lifetime Value (LTV) model and provide actionable insights for fundraising strategies. The analysis includes donor segmentation, retention analysis, and forecasting of future donations.

## Problem Statement
The nonprofit aims to double its annual fundraising over the next five years. This project addresses the following key questions:
1. How can we accurately estimate donor Lifetime Value?
2. What strategies can be implemented to improve donor retention and increase donations?
3. How can we segment donors effectively to tailor engagement strategies?

## Key Findings
1. Donor Segmentation: Identified three key donor segments (Small, Medium, Large) with distinct behaviors and retention rates.
2. Retention Analysis: Discovered improving retention rates across all segments since 2017, with Major donors showing the highest retention at 85% in 2022.
3. Seasonal Trends: Observed significant concentration of donations in December and Q4.
4. LTV Model: Developed a predictive model for donor LTV, incorporating factors such as first donation amount, donor segment, and retention probability.
5. Sensitivity Analysis: Conducted analysis on how changes in donation amounts and retention rates impact revenue and ROI, providing insights for strategic decision-making.

## Technologies Used
- Python 3.8+
- Pandas for data manipulation
- Scikit-learn for machine learning models
- Matplotlib and Seaborn for data visualization
- Jupyter Notebooks for interactive analysis

## How to Run the Project
1. Clone this repository
2. Install required packages: `pip install -r requirements.txt`
3. Run Jupyter Notebook: `jupyter notebook`
4. Open `donor_ltv_analysis.ipynb` to view the analysis

## Files in the Repository
- `donor_ltv_analysis.ipynb`: Jupyter notebook containing the main analysis
- `ltv_model.py`: Python script with the LTV model implementation
- `utils.py`: Utility functions for data processing and visualization
- `requirements.txt`: List of required Python packages
- `data/`: Directory containing the dataset

## Key Visualizations
- Donor Segmentation Heatmap
- Retention Rate Trends by Segment
- Seasonal Donation Patterns
- Lead Source Effectiveness Scatter Plot
- LTV Prediction vs Actual Scatter Plot
- Revenue and ROI Sensitivity Analysis Heatmaps

## Future Work
- Incorporate more donor demographic data for refined segmentation
- Develop a dynamic dashboard for real-time LTV tracking
- Implement A/B testing framework for engagement strategies
- Explore machine learning techniques for donor churn prediction
- Conduct cohort analysis to understand long-term donor behavior

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
