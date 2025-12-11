"""
Unit Tests for Healthcare Data Analysis

This module contains tests for the healthcare data analysis components.
"""

import unittest
import pandas as pd
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from data_processing.data_loader import HealthcareDataLoader
from analysis.healthcare_metrics import HealthcareAnalyzer


class TestHealthcareDataLoader(unittest.TestCase):
    """Test cases for HealthcareDataLoader class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.loader = HealthcareDataLoader()
    
    def test_load_health_expenditure(self):
        """Test loading healthcare expenditure data."""
        df = self.loader.load_health_expenditure()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('country', df.columns)
        self.assertIn('year', df.columns)
        self.assertIn('expenditure_pct_gdp', df.columns)
    
    def test_load_life_expectancy(self):
        """Test loading life expectancy data."""
        df = self.loader.load_life_expectancy()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('country', df.columns)
        self.assertIn('year', df.columns)
        self.assertIn('life_expectancy_total', df.columns)
    
    def test_load_hospital_beds(self):
        """Test loading hospital beds data."""
        df = self.loader.load_hospital_beds()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('country', df.columns)
        self.assertIn('hospital_beds_per_1000', df.columns)
    
    def test_get_countries(self):
        """Test getting list of countries."""
        countries = self.loader.get_countries()
        self.assertIsInstance(countries, list)
        self.assertGreater(len(countries), 0)
        self.assertTrue(all(isinstance(c, str) for c in countries))
    
    def test_get_years(self):
        """Test getting list of years."""
        years = self.loader.get_years()
        self.assertIsInstance(years, list)
        self.assertGreater(len(years), 0)
        self.assertTrue(all(isinstance(y, int) for y in years))


class TestHealthcareAnalyzer(unittest.TestCase):
    """Test cases for HealthcareAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = HealthcareAnalyzer()
    
    def test_analyze_expenditure_trends(self):
        """Test expenditure trends analysis."""
        result = self.analyzer.analyze_expenditure_trends()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertGreater(len(result), 0)
        self.assertIn('country', result.columns)
    
    def test_compare_life_expectancy(self):
        """Test life expectancy comparison."""
        result = self.analyzer.compare_life_expectancy()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertGreater(len(result), 0)
        self.assertIn('country', result.columns)
        self.assertIn('life_expectancy_total', result.columns)
        self.assertIn('gender_gap', result.columns)
    
    def test_analyze_healthcare_capacity(self):
        """Test healthcare capacity analysis."""
        result = self.analyzer.analyze_healthcare_capacity()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertGreater(len(result), 0)
        self.assertIn('hospital_beds_per_1000', result.columns)
    
    def test_correlate_spending_outcomes(self):
        """Test correlation between spending and outcomes."""
        result = self.analyzer.correlate_spending_outcomes()
        self.assertIsInstance(result, pd.DataFrame)
        self.assertGreater(len(result), 0)
        self.assertIn('expenditure_pct_gdp', result.columns)
        self.assertIn('life_expectancy_total', result.columns)


if __name__ == '__main__':
    unittest.main()
