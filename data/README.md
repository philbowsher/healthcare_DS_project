# Data Directory

This directory contains healthcare data for analysis.

## Structure

- `raw/`: Raw data files downloaded from various sources (not committed to git)
- `processed/`: Cleaned and processed data ready for analysis

## Data Sources

### 1. Eurostat
- **URL**: https://ec.europa.eu/eurostat/data/database
- **Topics**: Health expenditure, life expectancy, mortality rates
- **Coverage**: All EU member states and some European countries
- **Format**: CSV, XLSX

### 2. WHO European Health Information Gateway
- **URL**: https://gateway.euro.who.int/
- **Topics**: Disease prevalence, healthcare systems, health determinants
- **Coverage**: 53 countries in WHO European Region
- **Format**: CSV, API

### 3. OECD Health Statistics
- **URL**: https://www.oecd.org/health/health-data.htm
- **Topics**: Healthcare quality, resources, utilization
- **Coverage**: OECD member countries in Europe
- **Format**: CSV, XLSX

## Sample Datasets

The `processed/` directory contains example datasets:
- `european_health_expenditure.csv`: Healthcare spending by country (2010-2023)
- `life_expectancy_data.csv`: Life expectancy at birth by country and gender
- `hospital_beds.csv`: Hospital bed availability per 1000 population

## Data Usage

1. Download raw data from sources listed above
2. Place raw data files in the `raw/` directory
3. Use scripts in `src/data_processing/` to clean and process data
4. Processed data will be saved to `processed/` directory

## Notes

- Raw data files are excluded from git commits (see .gitignore)
- Always verify data sources and update dates
- Check license terms for each data source before use
