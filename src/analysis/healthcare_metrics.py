"""
Healthcare Metrics Analysis

This module provides analysis functions for healthcare data.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent directory to path to import data_loader
sys.path.append(str(Path(__file__).parent.parent))
from data_processing.data_loader import HealthcareDataLoader


class HealthcareAnalyzer:
    """Analyze European healthcare data."""
    
    def __init__(self):
        """Initialize the analyzer with data loader."""
        self.loader = HealthcareDataLoader()
    
    def analyze_expenditure_trends(self):
        """
        Analyze healthcare expenditure trends across countries.
        
        Returns:
            DataFrame with expenditure statistics by country
        """
        df = self.loader.load_health_expenditure()
        
        # Calculate statistics for each country
        stats = df.groupby('country').agg({
            'expenditure_pct_gdp': ['mean', 'min', 'max', 'std'],
            'expenditure_per_capita_usd': ['mean', 'min', 'max'],
            'public_share_pct': 'mean'
        }).round(2)
        
        # Flatten column names
        stats.columns = ['_'.join(col).strip() for col in stats.columns.values]
        
        return stats.reset_index()
    
    def compare_life_expectancy(self):
        """
        Compare life expectancy across countries.
        
        Returns:
            DataFrame with life expectancy by country for latest year
        """
        df = self.loader.load_life_expectancy()
        
        # Get latest year data
        latest_year = df['year'].max()
        latest_data = df[df['year'] == latest_year].copy()
        
        # Calculate gender gap
        latest_data['gender_gap'] = (
            latest_data['life_expectancy_female'] - 
            latest_data['life_expectancy_male']
        ).round(2)
        
        # Sort by total life expectancy
        latest_data = latest_data.sort_values('life_expectancy_total', ascending=False)
        
        return latest_data[['country', 'life_expectancy_total', 
                           'life_expectancy_male', 'life_expectancy_female', 
                           'gender_gap']]
    
    def analyze_healthcare_capacity(self):
        """
        Analyze healthcare capacity (hospital beds).
        
        Returns:
            DataFrame with hospital bed statistics by country
        """
        df = self.loader.load_hospital_beds()
        
        # Get latest year data
        latest_year = df['year'].max()
        latest_data = df[df['year'] == latest_year].copy()
        
        # Sort by hospital beds
        latest_data = latest_data.sort_values('hospital_beds_per_1000', ascending=False)
        
        return latest_data[['country', 'hospital_beds_per_1000', 'icu_beds_per_100000']]
    
    def correlate_spending_outcomes(self):
        """
        Analyze correlation between healthcare spending and life expectancy.
        
        Returns:
            DataFrame with merged data and correlation coefficient
        """
        expenditure = self.loader.load_health_expenditure()
        life_exp = self.loader.load_life_expectancy()
        
        # Merge datasets
        merged = pd.merge(
            expenditure[['country', 'year', 'expenditure_pct_gdp', 'expenditure_per_capita_usd']],
            life_exp[['country', 'year', 'life_expectancy_total']],
            on=['country', 'year']
        )
        
        # Calculate correlation
        correlation_gdp = merged['expenditure_pct_gdp'].corr(merged['life_expectancy_total'])
        correlation_capita = merged['expenditure_per_capita_usd'].corr(merged['life_expectancy_total'])
        
        print(f"Correlation between expenditure (% GDP) and life expectancy: {correlation_gdp:.3f}")
        print(f"Correlation between expenditure (per capita) and life expectancy: {correlation_capita:.3f}")
        
        return merged
    
    def generate_summary_report(self):
        """Generate a comprehensive summary report."""
        print("=" * 70)
        print("EUROPEAN HEALTHCARE DATA ANALYSIS SUMMARY")
        print("=" * 70)
        
        # Countries and years
        countries = self.loader.get_countries()
        years = self.loader.get_years()
        print(f"\nDataset Coverage:")
        print(f"  Countries: {len(countries)}")
        print(f"  Years: {min(years)} - {max(years)}")
        
        # Expenditure analysis
        print("\n" + "-" * 70)
        print("Top 5 Countries by Healthcare Expenditure (% of GDP):")
        print("-" * 70)
        exp_stats = self.analyze_expenditure_trends()
        top_5_exp = exp_stats.nlargest(5, 'expenditure_pct_gdp_mean')
        print(top_5_exp[['country', 'expenditure_pct_gdp_mean', 'public_share_pct_mean']].to_string(index=False))
        
        # Life expectancy analysis
        print("\n" + "-" * 70)
        print("Top 5 Countries by Life Expectancy:")
        print("-" * 70)
        life_exp = self.compare_life_expectancy()
        top_5_life = life_exp.head(5)
        print(top_5_life.to_string(index=False))
        
        # Healthcare capacity
        print("\n" + "-" * 70)
        print("Top 5 Countries by Hospital Bed Capacity:")
        print("-" * 70)
        capacity = self.analyze_healthcare_capacity()
        top_5_beds = capacity.head(5)
        print(top_5_beds.to_string(index=False))
        
        # Correlation analysis
        print("\n" + "-" * 70)
        print("Correlation Analysis:")
        print("-" * 70)
        self.correlate_spending_outcomes()
        
        print("\n" + "=" * 70)


if __name__ == "__main__":
    analyzer = HealthcareAnalyzer()
    analyzer.generate_summary_report()
