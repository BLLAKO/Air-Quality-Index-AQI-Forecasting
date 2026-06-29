import pandas as pd

def load_data(path="data/raw/air_quality.csv"):
    """Load raw AQI data, set datetime index, ensure daily frequency."""
    df = pd.read_csv(path, parse_dates=["date"])
    df.set_index("date", inplace=True)

    # Here we force daily frequency and fill missing values by interpolation
    df = df.asfreq("D")
    df = df.interpolate(method="time")

    return df
