# 🌍 Air Quality Index (AQI) Forecasting

This project builds a machine learning pipeline to forecast daily **Air Quality Index (AQI)** values based on past pollution data.

## Pipeline
**Data ingestion** – load raw AQI data
**Preprocessing** – clean missing values, resample to daily
**Feature engineering** – lag features, rolling averages, weekday/seasonal indicators
**Model training** – LightGBM regressor
**Evaluation** – RMSE, MAPE vs naive baseline
**Visualization** – forecast vs actual AQI plot
