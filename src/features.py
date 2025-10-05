import pandas as pd

def add_features(df, lags=[1,2,3,7], ma_windows=[3,7,14]):
    for lag in lags:
        df[f"lag_{lag}"] = df["AQI"].shift(lag)
    for w in ma_windows:
        df[f"ma_{w}"] = df["AQI"].rolling(w).mean()
    df["dayofweek"] = df.index.dayofweek
    df = df.dropna()
    return df
