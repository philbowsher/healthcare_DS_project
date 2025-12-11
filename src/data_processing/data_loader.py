"""
Data Loader Module

This module provides utilities for loading and accessing healthcare data.
"""

import pandas as pd
import os
from pathlib import Path


class HealthcareDataLoader:
    """Load and manage healthcare datasets."""
    
    def __init__(self, data_dir=None):
        """
        Initialize the data loader.
        
        Args:
            data_dir: Path to the data directory. Defaults to ../data/processed
        """
        if data_dir is None:
            # Get the path relative to this file
            self.data_dir = Path(__file__).parent.parent.parent / 'data' / 'processed'
        else:
            self.data_dir = Path(data_dir)
    
    def load_health_expenditure(self):
        """
        Load healthcare expenditure data.
        
        Returns:
            DataFrame with healthcare expenditure by country and year
        """
        file_path = self.data_dir / 'european_health_expenditure.csv'
        return pd.read_csv(file_path)
    
    def load_life_expectancy(self):
        """
        Load life expectancy data.
        
        Returns:
            DataFrame with life expectancy by country, year, and gender
        """
        file_path = self.data_dir / 'life_expectancy_data.csv'
        return pd.read_csv(file_path)
    
    def load_hospital_beds(self):
        """
        Load hospital beds data.
        
        Returns:
            DataFrame with hospital bed availability by country and year
        """
        file_path = self.data_dir / 'hospital_beds.csv'
        return pd.read_csv(file_path)
    
    def get_countries(self):
        """
        Get list of all countries in the dataset.
        
        Returns:
            List of country names
        """
        df = self.load_health_expenditure()
        return sorted(df['country'].unique().tolist())
    
    def get_years(self):
        """
        Get list of all years in the dataset.
        
        Returns:
            List of years
        """
        df = self.load_health_expenditure()
        return sorted(df['year'].unique().tolist())


if __name__ == "__main__":
    # Example usage
    loader = HealthcareDataLoader()
    
    print("Loading healthcare data...")
    expenditure = loader.load_health_expenditure()
    life_exp = loader.load_life_expectancy()
    beds = loader.load_hospital_beds()
    
    print(f"\nCountries in dataset: {len(loader.get_countries())}")
    print(f"Years covered: {loader.get_years()}")
    print(f"\nHealthcare Expenditure Data Shape: {expenditure.shape}")
    print(f"Life Expectancy Data Shape: {life_exp.shape}")
    print(f"Hospital Beds Data Shape: {beds.shape}")
