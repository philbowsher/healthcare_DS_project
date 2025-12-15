# Quick Start Guide

## European Healthcare Data Analysis Project

This guide will help you get started with analyzing European healthcare data.

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/philbowsher/healthcare_DS_project.git
cd healthcare_DS_project
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Running Your First Analysis

### Option 1: Command Line Analysis

Run the healthcare metrics analysis script:

```bash
python src/analysis/healthcare_metrics.py
```

This will generate a comprehensive summary report showing:
- Healthcare expenditure statistics by country
- Life expectancy comparisons
- Hospital bed capacity analysis
- Correlation between spending and health outcomes

### Option 2: Interactive Jupyter Notebook

1. Start Jupyter:
```bash
jupyter notebook
```

2. Open `notebooks/european_healthcare_analysis.ipynb`

3. Run the cells to explore the data interactively

### Option 3: Python Script

Use the data loader and analyzer in your own scripts:

```python
from src.data_processing.data_loader import HealthcareDataLoader
from src.analysis.healthcare_metrics import HealthcareAnalyzer

# Load data
loader = HealthcareDataLoader()
expenditure_df = loader.load_health_expenditure()

# Analyze
analyzer = HealthcareAnalyzer()
expenditure_stats = analyzer.analyze_expenditure_trends()
print(expenditure_stats)
```

## Available Datasets

The project includes three sample datasets:

1. **european_health_expenditure.csv**: Healthcare spending data
   - Expenditure as % of GDP
   - Per capita spending (USD)
   - Public/private healthcare share

2. **life_expectancy_data.csv**: Life expectancy statistics
   - Total population
   - By gender (male/female)
   - Gender gap calculations

3. **hospital_beds.csv**: Healthcare system capacity
   - Hospital beds per 1000 population
   - ICU beds per 100,000 population

## Running Tests

Verify everything works correctly:

```bash
python -m unittest tests/test_healthcare_analysis.py -v
```

## Visualizations

Create healthcare visualizations:

```python
from src.visualization.healthcare_plots import HealthcareVisualizer

visualizer = HealthcareVisualizer()

# Create various plots
visualizer.plot_expenditure_comparison()
visualizer.plot_life_expectancy_trends()
visualizer.plot_spending_vs_life_expectancy()
visualizer.plot_hospital_capacity()
```

## Next Steps

- Explore the Jupyter notebook for interactive analysis
- Modify the analysis scripts to answer specific questions
- Add your own data from Eurostat, WHO, or OECD
- Create custom visualizations
- Extend the analysis with statistical modeling

## Data Sources

For real-world analysis, download data from:
- **Eurostat**: https://ec.europa.eu/eurostat
- **WHO**: https://gateway.euro.who.int/
- **OECD**: https://www.oecd.org/health/health-data.htm

Place downloaded files in `data/raw/` and use the data processing scripts.

## Support

For issues or questions, please open an issue on GitHub.
