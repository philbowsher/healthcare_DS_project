#!/usr/bin/env python3
"""
Example: Comprehensive Healthcare Data Analysis

This script demonstrates how to use the European Healthcare Data Analysis
project to perform a complete analysis workflow.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from data_processing.data_loader import HealthcareDataLoader
from analysis.healthcare_metrics import HealthcareAnalyzer


def main():
    """Run a comprehensive healthcare data analysis example."""
    
    print("=" * 80)
    print("EUROPEAN HEALTHCARE DATA ANALYSIS - EXAMPLE WORKFLOW")
    print("=" * 80)
    
    # Step 1: Load data
    print("\n1. Loading data...")
    loader = HealthcareDataLoader()
    
    expenditure = loader.load_health_expenditure()
    life_exp = loader.load_life_expectancy()
    beds = loader.load_hospital_beds()
    
    print(f"   ✓ Loaded data for {len(loader.get_countries())} countries")
    print(f"   ✓ Covering years {min(loader.get_years())} - {max(loader.get_years())}")
    
    # Step 2: Perform analysis
    print("\n2. Performing analysis...")
    analyzer = HealthcareAnalyzer()
    
    # Expenditure analysis
    exp_stats = analyzer.analyze_expenditure_trends()
    print(f"   ✓ Analyzed healthcare expenditure trends")
    
    # Life expectancy comparison
    life_comp = analyzer.compare_life_expectancy()
    print(f"   ✓ Compared life expectancy across countries")
    
    # Healthcare capacity
    capacity = analyzer.analyze_healthcare_capacity()
    print(f"   ✓ Evaluated healthcare system capacity")
    
    # Step 3: Display key insights
    print("\n3. Key Insights:")
    print("-" * 80)
    
    # Top spenders
    top_spender = exp_stats.nlargest(1, 'expenditure_pct_gdp_mean').iloc[0]
    print(f"\n   Highest healthcare expenditure:")
    print(f"   • {top_spender['country']}: {top_spender['expenditure_pct_gdp_mean']:.1f}% of GDP")
    
    # Highest life expectancy
    top_life = life_comp.iloc[0]
    print(f"\n   Highest life expectancy:")
    print(f"   • {top_life['country']}: {top_life['life_expectancy_total']:.1f} years")
    print(f"     - Male: {top_life['life_expectancy_male']:.1f} years")
    print(f"     - Female: {top_life['life_expectancy_female']:.1f} years")
    print(f"     - Gender gap: {top_life['gender_gap']:.1f} years")
    
    # Hospital capacity
    top_beds = capacity.iloc[0]
    print(f"\n   Highest hospital bed capacity:")
    print(f"   • {top_beds['country']}: {top_beds['hospital_beds_per_1000']:.1f} beds per 1000 people")
    
    # Step 4: Correlation insights
    print("\n4. Correlation Analysis:")
    print("-" * 80)
    merged = analyzer.correlate_spending_outcomes()
    
    # Step 5: Summary statistics
    print("\n5. Summary Statistics:")
    print("-" * 80)
    
    print(f"\n   Average healthcare expenditure: {expenditure['expenditure_pct_gdp'].mean():.1f}% of GDP")
    print(f"   Average life expectancy: {life_exp['life_expectancy_total'].mean():.1f} years")
    print(f"   Average hospital beds: {beds['hospital_beds_per_1000'].mean():.1f} per 1000 people")
    
    # Calculate ranges
    exp_range = expenditure['expenditure_pct_gdp'].max() - expenditure['expenditure_pct_gdp'].min()
    life_range = life_exp['life_expectancy_total'].max() - life_exp['life_expectancy_total'].min()
    
    print(f"\n   Expenditure range: {exp_range:.1f} percentage points")
    print(f"   Life expectancy range: {life_range:.1f} years")
    
    # Step 6: Recommendations
    print("\n6. Analysis Recommendations:")
    print("-" * 80)
    print("""
   Based on this analysis, you can:
   
   • Investigate why some countries achieve higher life expectancy with
     lower healthcare spending
   
   • Examine the relationship between hospital bed capacity and health
     outcomes during pandemic situations
   
   • Analyze trends over time to identify improving or declining healthcare
     systems
   
   • Compare public vs. private healthcare funding models and their
     effectiveness
   
   • Extend this analysis with additional data sources (WHO, OECD, Eurostat)
     for more comprehensive insights
    """)
    
    print("\n" + "=" * 80)
    print("Analysis complete! See notebooks/ for interactive exploration.")
    print("=" * 80)


if __name__ == "__main__":
    main()
