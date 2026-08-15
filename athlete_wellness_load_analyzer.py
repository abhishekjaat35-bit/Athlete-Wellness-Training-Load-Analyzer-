import pandas as pd
import matplotlib.pyplot as plt


print("=" * 75)
print("          ATHLETE WELLNESS & TRAINING LOAD ANALYZER")
print("=" * 75)


# ------------------------------------------
# Load Data
# ------------------------------------------

data = pd.read_csv("athlete_wellness_data.csv")

data["Date"] = pd.to_datetime(data["Date"])

data = data.sort_values(
    ["Athlete", "Date"]
).reset_index(drop=True)


# ------------------------------------------
# Display Dataset
# ------------------------------------------

print("\n" + "=" * 75)
print("ATHLETE MONITORING DATA")
print("=" * 75)

print(data.to_string(index=False))


# ------------------------------------------
# Calculate Wellness Score
# ------------------------------------------
# Higher values represent better wellness.
#
# Sleep Quality: 1-5
# Muscle Soreness: 1-5
# Fatigue: 1-5
# Stress: 1-5
#
# Soreness, fatigue and stress are reverse scored.

data["Soreness_Score"] = 6 - data["Muscle_Soreness"]

data["Fatigue_Score"] = 6 - data["Fatigue"]

data["Stress_Score"] = 6 - data["Stress"]

data["Wellness_Score"] = (
    data["Sleep_Quality"]
    + data["Soreness_Score"]
    + data["Fatigue_Score"]
    + data["Stress_Score"]
)


# ------------------------------------------
# Calculate Readiness Score
# ------------------------------------------

data["Readiness_Score"] = (
    data["Wellness_Score"] / 20
) * 100


# ------------------------------------------
# Training Load vs Wellness Ratio
# ------------------------------------------

data["Load_per_Wellness"] = (
    data["Training_Load"]
    / data["Wellness_Score"]
)


# ------------------------------------------
# Readiness Classification
# ------------------------------------------

def classify_readiness(score):

    if score >= 85:
        return "High Readiness"

    elif score >= 70:
        return "Moderate Readiness"

    else:
        return "Low Readiness"


data["Readiness_Status"] = (
    data["Readiness_Score"]
    .apply(classify_readiness)
)


# ------------------------------------------
# Display Calculated Results
# ------------------------------------------

print("\n" + "=" * 75)
print("WELLNESS & READINESS ANALYSIS")
print("=" * 75)

display_columns = [
    "Athlete",
    "Date",
    "Training_Load",
    "Sleep_Quality",
    "Muscle_Soreness",
    "Fatigue",
    "Stress",
    "Wellness_Score",
    "Readiness_Score",
    "Readiness_Status"
]

print(
    data[display_columns].to_string(
        index=False,
        formatters={
            "Readiness_Score":
                lambda x: f"{x:.1f}%"
        }
    )
)


# ------------------------------------------
# Athlete Summary
# ------------------------------------------

athlete_summary = (
    data.groupby("Athlete")
    .agg(
        Sessions=("Athlete", "count"),
        Average_Load=("Training_Load", "mean"),
        Average_Wellness=("Wellness_Score", "mean"),
        Average_Readiness=("Readiness_Score", "mean"),
        Average_Sleep=("Sleep_Quality", "mean"),
        Average_Soreness=("Muscle_Soreness", "mean"),
        Average_Fatigue=("Fatigue", "mean"),
        Average_Stress=("Stress", "mean")
    )
    .reset_index()
)


print("\n" + "=" * 75)
print("ATHLETE WELLNESS SUMMARY")
print("=" * 75)

print(
    athlete_summary.to_string(
        index=False,
        formatters={
            "Average_Load": "{:.1f}".format,
            "Average_Wellness": "{:.1f}".format,
            "Average_Readiness": "{:.1f}%".format,
            "Average_Sleep": "{:.1f}".format,
            "Average_Soreness": "{:.1f}".format,
            "Average_Fatigue": "{:.1f}".format,
            "Average_Stress": "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Team Summary
# ------------------------------------------

print("\n" + "=" * 75)
print("TEAM MONITORING SUMMARY")
print("=" * 75)

print(
    f"Average Training Load : "
    f"{data['Training_Load'].mean():.1f} AU"
)

print(
    f"Average Wellness      : "
    f"{data['Wellness_Score'].mean():.1f}/20"
)

print(
    f"Average Readiness     : "
    f"{data['Readiness_Score'].mean():.1f}%"
)

print(
    f"Average Sleep Quality : "
    f"{data['Sleep_Quality'].mean():.1f}/5"
)

print(
    f"Average Soreness      : "
    f"{data['Muscle_Soreness'].mean():.1f}/5"
)

print(
    f"Average Fatigue       : "
    f"{data['Fatigue'].mean():.1f}/5"
)

print(
    f"Average Stress        : "
    f"{data['Stress'].mean():.1f}/5"
)


# ------------------------------------------
# Readiness Status Summary
# ------------------------------------------

status_summary = (
    data["Readiness_Status"]
    .value_counts()
    .reset_index()
)

status_summary.columns = [
    "Readiness_Status",
    "Observations"
]


print("\n" + "=" * 75)
print("READINESS STATUS SUMMARY")
print("=" * 75)

print(
    status_summary.to_string(index=False)
)


# ------------------------------------------
# Lowest Readiness
# ------------------------------------------

lowest_readiness = data.loc[
    data["Readiness_Score"].idxmin()
]


print("\n" + "=" * 75)
print("LOWEST READINESS OBSERVATION")
print("=" * 75)

print(
    f"Athlete   : "
    f"{lowest_readiness['Athlete']}"
)

print(
    f"Date      : "
    f"{lowest_readiness['Date'].date()}"
)

print(
    f"Readiness : "
    f"{lowest_readiness['Readiness_Score']:.1f}%"
)

print(
    f"Training Load : "
    f"{lowest_readiness['Training_Load']} AU"
)


# ------------------------------------------
# Highest Readiness
# ------------------------------------------

highest_readiness = data.loc[
    data["Readiness_Score"].idxmax()
]


print("\n" + "=" * 75)
print("HIGHEST READINESS OBSERVATION")
print("=" * 75)

print(
    f"Athlete   : "
    f"{highest_readiness['Athlete']}"
)

print(
    f"Date      : "
    f"{highest_readiness['Date'].date()}"
)

print(
    f"Readiness : "
    f"{highest_readiness['Readiness_Score']:.1f}%"
)


# ------------------------------------------
# Correlation Analysis
# ------------------------------------------

correlation_variables = [
    "Training_Load",
    "Sleep_Quality",
    "Muscle_Soreness",
    "Fatigue",
    "Stress",
    "Wellness_Score",
    "Readiness_Score"
]

correlation_matrix = data[
    correlation_variables
].corr()


print("\n" + "=" * 75)
print("WELLNESS CORRELATION MATRIX")
print("=" * 75)

print(
    correlation_matrix.round(2).to_string()
)


# ------------------------------------------
# Visualization 1
# Training Load vs Wellness
# ------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    data["Training_Load"],
    data["Wellness_Score"]
)

plt.title("Training Load vs Wellness")
plt.xlabel("Training Load (AU)")
plt.ylabel("Wellness Score")
plt.tight_layout()

plt.savefig(
    "wellness_vs_training_load.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Visualization 2
# Readiness Trend
# ------------------------------------------

plt.figure(figsize=(10, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Readiness_Score"],
        marker="o",
        label=athlete
    )

plt.title("Athlete Readiness Trend")
plt.xlabel("Date")
plt.ylabel("Readiness (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    "readiness_trend.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Export Analysis
# ------------------------------------------

data.to_csv(
    "athlete_wellness_analysis.csv",
    index=False
)

athlete_summary.to_csv(
    "athlete_wellness_summary.csv",
    index=False
)


# ------------------------------------------
# Final Output
# ------------------------------------------

print("\n" + "=" * 75)
print("ANALYSIS COMPLETE")
print("=" * 75)

print("Files created:")
print("1. athlete_wellness_analysis.csv")
print("2. athlete_wellness_summary.csv")
print("3. wellness_vs_training_load.png")
print("4. readiness_trend.png")

print("\n" + "=" * 75)
print("MONITOR • INTERPRET • INFORM TRAINING")
print("=" * 75)