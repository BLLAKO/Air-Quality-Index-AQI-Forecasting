# 🌍 Air Quality Index (AQI) Forecasting

This project builds a machine learning pipeline to forecast daily **Air Quality Index (AQI)** values based on past pollution data.

## Pipeline
1. **Data ingestion** – load raw AQI data
2. **Preprocessing** – clean missing values, resample to daily
3. **Feature engineering** – lag features, rolling averages, weekday/seasonal indicators
4. **Model training** – LightGBM regressor
5. **Evaluation** – RMSE, MAPE vs naive baseline
6. **Visualization** – forecast vs actual AQI plot
