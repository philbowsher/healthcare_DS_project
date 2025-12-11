# European Healthcare Data Analysis Project

A comprehensive data science project analyzing public healthcare data across Europe. This project provides tools, scripts, and analysis for understanding healthcare systems, outcomes, and trends in European countries.

## Overview

This project analyzes publicly available healthcare data from European countries to identify patterns, trends, and insights about:
- Healthcare expenditure and funding
- Life expectancy and mortality rates
- Healthcare system performance
- Disease prevalence and prevention
- Healthcare access and quality indicators

## Project Structure

```
healthcare_DS_project/
├── data/                    # Data directory
│   ├── raw/                # Raw data files (not committed)
│   ├── processed/          # Cleaned and processed data
│   └── README.md           # Data sources and descriptions
├── notebooks/              # Jupyter notebooks for analysis
├── src/                    # Source code
│   ├── data_processing/   # Data cleaning and preparation
│   ├── analysis/          # Analysis scripts
│   └── visualization/     # Visualization utilities
├── docs/                   # Documentation
├── tests/                  # Unit tests
└── requirements.txt        # Python dependencies
```

## Data Sources

This project uses publicly available healthcare data from:
- **Eurostat**: European statistical database
- **WHO**: World Health Organization European Region
- **OECD**: Organisation for Economic Co-operation and Development
- **European Health Information Gateway (HIS)**

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/philbowsher/healthcare_DS_project.git
cd healthcare_DS_project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the example analysis:
```bash
python src/analysis/healthcare_metrics.py
```

## Key Analyses

1. **Healthcare Expenditure Analysis**: Compare healthcare spending across European countries
2. **Life Expectancy Trends**: Analyze life expectancy changes over time
3. **Healthcare System Performance**: Evaluate healthcare outcomes and efficiency
4. **Disease Burden Analysis**: Study prevalence and impact of major diseases

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is for educational and research purposes.

## Contact

For questions or collaboration, please open an issue on GitHub.
