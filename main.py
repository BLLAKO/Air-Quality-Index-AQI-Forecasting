from src.data_pipeline import load_data
from src.features import add_features
from src.model import train_model
from src.evaluate import evaluate, plot_forecast

# Load data
df = load_data()
df = add_features(df)

# Split
train = df.iloc[:-60]
test = df.iloc[-60:]
X_train, y_train = train.drop("AQI", axis=1), train["AQI"]
X_test, y_test = test.drop("AQI", axis=1), test["AQI"]

# Train
model = train_model(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate
rmse, mape = evaluate(y_test.values, y_pred)
print(f"RMSE: {rmse:.2f}, MAPE: {mape:.2f}%")

# Plot
plot_forecast(y_test.values, y_pred, test.index)
