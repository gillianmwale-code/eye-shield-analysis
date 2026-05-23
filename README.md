# Eye Shield Effectiveness Analysis

## Overview
This project analyses experimental data collected to evaluate the effectiveness of different eye shielding materials in reducing light exposure at varying distances. The aim is to compare how well commonly available materials attenuate light relative to an unprotected condition.

## Dataset
The dataset was generated from a small experimental study measuring light radiance (uW/cm²/nm) at four distances (35 cm, 25 cm, 15 cm, and 10 cm) under different shielding conditions.

Materials tested include:
- No shield (baseline)
- Gauze and plaster
- Surgical face masks
- Cotton
- Gold standard eye protection

Each material group contains multiple repeated measurements, allowing comparison of variability and average performance.

## Methods
The analysis was conducted using Python and includes:

- Data loading from Excel
- Cleaning and restructuring of manually formatted experimental data
- Conversion of measurements into analysable numerical format
- Grouping and aggregation to calculate average light exposure by material
- Data visualisation to compare effectiveness and observe trends across distances

## Key Findings
- Cotton and gold standard materials showed complete attenuation of light across all distances
- Gauze and plaster provided partial protection, with variability between samples
- Surgical masks reduced light exposure but still allowed substantial transmission, particularly at closer distances
- Light exposure increased as distance decreased across all materials, as expected

## Project Structure
- `eye_shield_experiment_data.xlsx` — raw experimental dataset  
- `analysis.py` — Python script for data cleaning, analysis, and visualisation  
- `README.md` — project documentation  

## Future Improvements
- Extend analysis with statistical testing (e.g. significance testing between materials)
- Explore variability within groups in more detail
- Implement more advanced visualisations
