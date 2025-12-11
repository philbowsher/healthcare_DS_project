"""
Healthcare Data Visualization Module

This module provides visualization utilities for healthcare data analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from data_processing.data_loader import HealthcareDataLoader

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class HealthcareVisualizer:
    """Create visualizations for healthcare data."""
    
    def __init__(self):
        """Initialize the visualizer with data loader."""
        self.loader = HealthcareDataLoader()
    
    def plot_expenditure_comparison(self, output_path=None):
        """
        Create a bar plot comparing healthcare expenditure across countries.
        
        Args:
            output_path: Optional path to save the figure
        """
        df = self.loader.load_health_expenditure()
        
        # Get latest year average for each country
        latest_year = df['year'].max()
        latest_data = df[df['year'] == latest_year].sort_values('expenditure_pct_gdp', ascending=False)
        
        fig, ax = plt.subplots(figsize=(14, 8))
        bars = ax.bar(latest_data['country'], latest_data['expenditure_pct_gdp'], 
                      color='steelblue', edgecolor='navy', alpha=0.7)
        
        ax.set_xlabel('Country', fontsize=12, fontweight='bold')
        ax.set_ylabel('Healthcare Expenditure (% of GDP)', fontsize=12, fontweight='bold')
        ax.set_title(f'Healthcare Expenditure Across European Countries ({latest_year})', 
                     fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to {output_path}")
        else:
            plt.show()
        
        return fig
    
    def plot_life_expectancy_trends(self, countries=None, output_path=None):
        """
        Plot life expectancy trends over time.
        
        Args:
            countries: List of countries to plot. If None, plots top 5.
            output_path: Optional path to save the figure
        """
        df = self.loader.load_life_expectancy()
        
        if countries is None:
            # Get top 5 countries by latest life expectancy
            latest = df[df['year'] == df['year'].max()]
            countries = latest.nlargest(5, 'life_expectancy_total')['country'].tolist()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        for country in countries:
            country_data = df[df['country'] == country]
            ax.plot(country_data['year'], country_data['life_expectancy_total'], 
                   marker='o', label=country, linewidth=2)
        
        ax.set_xlabel('Year', fontsize=12, fontweight='bold')
        ax.set_ylabel('Life Expectancy (years)', fontsize=12, fontweight='bold')
        ax.set_title('Life Expectancy Trends in European Countries', 
                     fontsize=14, fontweight='bold')
        ax.legend(loc='best', frameon=True)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to {output_path}")
        else:
            plt.show()
        
        return fig
    
    def plot_spending_vs_life_expectancy(self, output_path=None):
        """
        Create scatter plot of healthcare spending vs life expectancy.
        
        Args:
            output_path: Optional path to save the figure
        """
        expenditure = self.loader.load_health_expenditure()
        life_exp = self.loader.load_life_expectancy()
        
        # Merge datasets for latest year
        latest_year = expenditure['year'].max()
        merged = pd.merge(
            expenditure[expenditure['year'] == latest_year],
            life_exp[life_exp['year'] == latest_year],
            on='country'
        )
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        scatter = ax.scatter(merged['expenditure_pct_gdp'], 
                           merged['life_expectancy_total'],
                           s=100, alpha=0.6, c='steelblue', edgecolors='navy')
        
        # Add country labels
        for idx, row in merged.iterrows():
            ax.annotate(row['country'], 
                       (row['expenditure_pct_gdp'], row['life_expectancy_total']),
                       fontsize=8, alpha=0.7, 
                       xytext=(5, 5), textcoords='offset points')
        
        ax.set_xlabel('Healthcare Expenditure (% of GDP)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Life Expectancy (years)', fontsize=12, fontweight='bold')
        ax.set_title(f'Healthcare Spending vs Life Expectancy ({latest_year})', 
                     fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to {output_path}")
        else:
            plt.show()
        
        return fig
    
    def plot_hospital_capacity(self, output_path=None):
        """
        Create horizontal bar chart of hospital bed capacity.
        
        Args:
            output_path: Optional path to save the figure
        """
        df = self.loader.load_hospital_beds()
        
        # Get latest year data
        latest_year = df['year'].max()
        latest_data = df[df['year'] == latest_year].sort_values('hospital_beds_per_1000')
        
        fig, ax = plt.subplots(figsize=(10, 12))
        
        y_pos = range(len(latest_data))
        ax.barh(y_pos, latest_data['hospital_beds_per_1000'], 
               color='coral', edgecolor='darkred', alpha=0.7)
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(latest_data['country'])
        ax.set_xlabel('Hospital Beds per 1000 Population', fontsize=12, fontweight='bold')
        ax.set_title(f'Hospital Bed Capacity in European Countries ({latest_year})', 
                     fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Figure saved to {output_path}")
        else:
            plt.show()
        
        return fig


if __name__ == "__main__":
    print("Creating healthcare visualizations...")
    visualizer = HealthcareVisualizer()
    
    print("\n1. Healthcare Expenditure Comparison")
    visualizer.plot_expenditure_comparison()
    
    print("\n2. Life Expectancy Trends")
    visualizer.plot_life_expectancy_trends()
    
    print("\n3. Spending vs Life Expectancy")
    visualizer.plot_spending_vs_life_expectancy()
    
    print("\n4. Hospital Bed Capacity")
    visualizer.plot_hospital_capacity()
    
    print("\nAll visualizations created successfully!")
