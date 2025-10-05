import pandas as pd
import numpy as np
import os

# Create directories if they don't exist
os.makedirs("data/raw", exist_ok=True)

# Generate 2 years of daily dates
rng = pd.date_range("2023-01-01", periods=730, freq="D")

# Generate AQI values with seasonality + noise
np.random.seed(42)
aqi_values = (
    50
    + 15 * np.sin(2 * np.pi * rng.dayofyear / 365)  # yearly cycle
    + 5 * np.sin(2 * np.pi * rng.dayofweek / 7)     # weekly cycle
    + np.random.normal(scale=7, size=len(rng))      # noise
)

# Clip values to realistic range [0, 500]
aqi_values = np.clip(aqi_values, 0, 500)

# Create DataFrame
df = pd.DataFrame({"date": rng, "AQI": aqi_values})
df.to_csv("data/raw/air_quality.csv", index=False)

print("Wrote data/raw/air_quality.csv with", len(df), "rows")
