# Eye Shield Data Analysis
# Investigating effectiveness of different materials in reducing light exposure

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_name = "eye_shield_experiment_data.xlsx"
raw_data = pd.read_excel(file_name, header=None)

# Display first few rows (for understanding structure)
print("Raw data preview:")
print(raw_data.head())

# -----------------------------
# Clean and restructure dataset
# -----------------------------

# Rename columns manually based on your dataset structure
data = raw_data.copy()

data.columns = ["Material", "ID", "35cm", "25cm", "15cm", "10cm"]

# Remove rows that don't have IDs (these are headers or labels)
data = data[data["ID"].notna()]

# Convert distance columns to numeric
for col in ["35cm", "25cm", "15cm", "10cm"]:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Drop rows with missing values
data = data.dropna()

# -----------------------------
# Analysis
# -----------------------------

# Calculate mean light exposure per material
mean_values = data.groupby("Material")[["35cm", "25cm", "15cm", "10cm"]].mean()

print("\nAverage light exposure by material:")
print(mean_values)

# -----------------------------
# Visualisation
# -----------------------------

# Plot 1: Light exposure at closest distance (10cm)
mean_values["10cm"].plot(kind="bar")

plt.title("Light Exposure at 10cm by Material")
plt.xlabel("Material")
plt.ylabel("Light Radiance (uW/cm²/nm)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Plot 2: Trend across distances
mean_values.T.plot()

plt.title("Light Exposure Across Distances")
plt.xlabel("Distance")
plt.ylabel("Light Radiance (uW/cm²/nm)")
plt.legend(title="Material")

plt.tight_layout()
plt.show()
