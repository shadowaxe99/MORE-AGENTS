
import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import matplotlib.pyplot as plt
from utils import load_data, preprocess_data

def forecast_model(data, periods):
    model = ExponentialSmoothing(data, seasonal='add', seasonal_periods=periods)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=12)
    return forecast

def visualize_forecast(data, forecast):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data.values, label='Historical Data')
    plt.plot(forecast.index, forecast.values, label='Forecast')
    plt.legend(loc='best')
    plt.title('Financial Forecast')
    plt.show()

def main():
    data = load_data('financial_data.csv')
    preprocessed_data = preprocess_data(data)
    forecast = forecast_model(preprocessed_data, 12)
    visualize_forecast(preprocessed_data, forecast)

if __name__ == "__main__":
    main()
