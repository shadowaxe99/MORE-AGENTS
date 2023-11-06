
import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data, column):
    data[column] = pd.to_datetime(data[column])
    data.set_index(column, inplace=True)
    return data

def plot_data(data, column):
    plt.figure(figsize=(12,6))
    sns.lineplot(data=data[column])
    plt.title('Time Series Data')
    plt.show()

def simple_exponential_smoothing(data, column):
    fit1 = SimpleExpSmoothing(data[column]).fit(smoothing_level=0.2,optimized=False)
    fcast1 = fit1.forecast(12).rename(r'$\alpha=0.2$')
    return fcast1

def double_exponential_smoothing(data, column):
    fit2 = Holt(data[column]).fit(smoothing_level=0.3, smoothing_slope=0.1)
    fcast2 = fit2.forecast(12).rename("Holt's linear trend")
    return fcast2

def triple_exponential_smoothing(data, column):
    fit3 = ExponentialSmoothing(data[column] ,seasonal_periods=4 ,trend='add', seasonal='add',).fit()
    fcast3 = fit3.forecast(12).rename('Holt-Winters (add-add-seasonal)')
    return fcast3
