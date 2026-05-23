# Eye Shield Data Analysis
# This script analyses how effective different materials are at blocking light

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_name = "eye_shield_experiment_data.xlsx"
df = pd.read_excel(file_name)

# Show first few rows
print("Preview of dataset:")
print(df.head())

# Because your file is structured manually, we will reshape it
# We will define column names clearly

df.columns = ["Material", "ID", "35cm", "25cm", "15cm", "10cm"]

# Remove rows that are not actual measurements
df = df.dropna()

# Convert numerical columns to numbers
for col in ["35cm", "25cm", "15cm", "10cm"]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values again after conversion
df = df.dropna()

# Calculate average light for each material
mean_values = df.groupby("Material")[["35cm", "25cm", "15cm", "10cm"]].mean()

print("\nAverage light exposure by material:")
print(mean_values)

# Plot average light at 10cm (most intense exposure)
mean_values["10cm"].plot(kind="bar")

plt.title("Average Light Exposure at 10cm by Material")
plt.xlabel("Material")
plt.ylabel("Light Radiance (uW/cm2/nm)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
