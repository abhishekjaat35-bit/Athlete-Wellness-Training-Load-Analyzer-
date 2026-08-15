# Athlete Wellness & Training Load Analyzer

A Python sports-performance monitoring project that integrates training load with subjective athlete wellness measures to generate a simple readiness indicator.

## Objective

The project combines:

- Training load
- Sleep quality
- Muscle soreness
- Fatigue
- Stress

to calculate:

- Wellness score
- Readiness score
- Readiness classification
- Athlete-level summaries
- Correlations between monitoring variables

## Data Flow

```text
Training Load
      +
Sleep Quality
      +
Muscle Soreness
      +
Fatigue
      +
Stress
      ↓
Wellness Score
      ↓
Readiness Score
      ↓
Athlete Monitoring
      ↓
Visualization
      ↓
Exported Analysis
```

## Dataset

The sample dataset contains 40 observations from four athletes.

### Variables

| Variable | Description |
|---|---|
| Athlete | Athlete identifier |
| Date | Observation date |
| Training_Load | Training load in arbitrary units |
| Sleep_Quality | Subjective sleep-quality score |
| Muscle_Soreness | Subjective soreness score |
| Fatigue | Subjective fatigue score |
| Stress | Subjective stress score |

The wellness variables use a 1–5 scale.

## Wellness Calculation

Soreness, fatigue and stress are reverse-scored because higher values represent poorer wellness.

```text
Reverse Score = 6 - Raw Score
```

The wellness score is:

```text
Sleep Quality
+
Reverse Soreness
+
Reverse Fatigue
+
Reverse Stress
```

Maximum wellness score:

```text
20
```

## Readiness Calculation

```text
Readiness (%) =
Wellness Score / 20 × 100
```

Readiness classification:

```text
≥ 85%  → High Readiness
70–84% → Moderate Readiness
< 70%  → Low Readiness
```

These thresholds are illustrative rules for this programming project and are not validated universal athlete-monitoring thresholds.

## Technologies

- Python
- Pandas
- Matplotlib
- CSV
- DataFrames
- GroupBy
- Feature engineering
- Conditional logic
- Correlation analysis
- Data visualization

## Installation

Install the required libraries:

```bash
pip install pandas matplotlib
```

## Running the Project

Place the Python script and CSV file in the same directory.

Run:

```bash
python athlete_wellness_load_analyzer.py
```

## Generated Outputs

```text
athlete_wellness_analysis.csv
athlete_wellness_summary.csv
wellness_vs_training_load.png
readiness_trend.png
```

## Example Results

The sample dataset produces an overall average readiness of approximately:

```text
77.5%
```

The lowest readiness observation occurs when a high training load is combined with poor subjective wellness scores.

## Sports Performance Applications

This type of monitoring workflow can support exploratory athlete-monitoring applications involving:

- Strength and conditioning
- Training-load monitoring
- Athlete readiness
- Wellness monitoring
- Fatigue monitoring
- Recovery monitoring
- Sports performance analytics

## Important Limitations

The dataset is synthetic and intended for programming and portfolio development.

Subjective wellness scores are not direct physiological measurements.

A readiness score calculated from these variables should not be treated as a medical or diagnostic measurement.

Real athlete-monitoring systems should consider:

- Individual baselines
- Measurement reliability
- Longitudinal trends
- Contextual factors
- Training history
- Competition schedule
- Objective performance measures
- Appropriate professional interpretation

## Future Development

- Add heart-rate data
- Add HRV
- Add GPS data
- Add jump testing
- Add sprint testing
- Add strength testing
- Add sleep duration
- Add athlete-specific baselines
- Add rolling readiness scores
- Add automated alerts
- Add dashboards
- Add predictive models
- Connect to a database

## Skills Demonstrated

```text
Python
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Conditional Logic
   ↓
GroupBy
   ↓
Correlation
   ↓
Matplotlib
   ↓
Athlete Monitoring
```

## Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

## License

MIT License