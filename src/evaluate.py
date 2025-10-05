import numpy as np
import matplotlib.pyplot as plt

def evaluate(y_true, y_pred):
    rmse = np.sqrt(((y_true - y_pred)**2).mean())
    mape = (np.abs((y_true - y_pred) / y_true).mean()) * 100
    return rmse, mape

def plot_forecast(y_true, y_pred, dates, save_path=None):
    plt.figure(figsize=(12,6))
    plt.plot(dates, y_true, label="Actual", color="blue")
    plt.plot(dates, y_pred, label="Forecast", color="red")
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.title("Air Quality Forecast")
    plt.legend()
    plt.grid(True)
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
        print(f"✅ Forecast plot saved to {save_path}")
    plt.show()
