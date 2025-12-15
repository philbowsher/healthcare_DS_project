# Examples

This directory contains example scripts demonstrating how to use the European Healthcare Data Analysis project.

## Available Examples

### comprehensive_analysis.py

A complete workflow example that demonstrates:
- Loading healthcare datasets
- Performing various analyses
- Extracting key insights
- Generating summary statistics
- Providing analysis recommendations

**Run it:**
```bash
python examples/comprehensive_analysis.py
```

## Creating Your Own Examples

Use the examples in this directory as templates for your own analysis scripts. The basic pattern is:

```python
from src.data_processing.data_loader import HealthcareDataLoader
from src.analysis.healthcare_metrics import HealthcareAnalyzer

# Load data
loader = HealthcareDataLoader()
data = loader.load_health_expenditure()

# Analyze
analyzer = HealthcareAnalyzer()
results = analyzer.analyze_expenditure_trends()

# Display or save results
print(results)
```

## Additional Resources

- See `notebooks/` for interactive Jupyter notebooks
- See `src/` for detailed API documentation in docstrings
- See `QUICKSTART.md` for installation and setup instructions
