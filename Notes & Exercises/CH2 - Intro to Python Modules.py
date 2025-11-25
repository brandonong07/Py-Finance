# Page 31 - 69
# Python modules
# Group of programs written by others to serve specific functions
# Book explains NumPy, SciPy, matplotlib, statsmodels, and Pandas

# Importing Modules
# if you want to name it something (import math as m) --> then use m.sqrt() etc.
import math as m 
import time as t
import numpy as np
import scipy as sp
import yfinance as yf
import pandas as pd


num = m.sqrt(23)
print(round(num, 5))

print(dir()) # Shows all modules imported
print(dir(m)) # Shows all functions in math module


# Yfinance & Black-Scholes Example
def bsCall(S, X, T, r, sigma):
    """
    S: Current stock price
    X: Strike Price
    T: Time to maturity (in years)
    r: Risk-free rate (annualized)
    sigma: Volatility of underlying asset (annualized)
    Returns: Black-Scholes call option price (european)
    """

    d1 = (m.log(S/X) + (r + 0.5*sigma**2)*T) / (sigma*m.sqrt(T))
    d2 = d1 - sigma*m.sqrt(T)
    callPrice = S*sp.stats.norm.cdf(d1) - X*m.exp(-r*T)*sp.stats.norm.cdf(d2)
    return callPrice

# Example usage of bsCall function
data = yf.Ticker("AAPL")
current_price = data.history(period="1d")['Close'][0] # Get current stock price
strike = current_price + 5 # Let's say strike is current price + 5
time_to_maturity = 30/365 # 30 days to maturity
risk_free_rate = 0.01 # 1% annual risk-free rate
sigma = 0.2 # 20% annual volatility

call_price = bsCall(current_price, strike, time_to_maturity, risk_free_rate, sigma)
print(f"Black-Scholes Call Option Price: {round(call_price, 2)}")

# Introduction to NumPy
# Finding array size
arr = np.array([[1,2,3],[4,5,6]])
np.size(arr) # Returns 6 (because there are 6 elements)
np.std(arr) # Std. dev of elements
(np.std(arr, 0)) # Std. dev of each row

# Introduction to Matplotlib
# Used to create various types of graphs, outputs in PDF, Postscript, SVG, PNG
import matplotlib.pyplot as plt
import datetime as dt
from mplfinance import *
from matplotlib.dates import MonthLocator, DateFormatter

ticker = "AAPL"
start = dt.date(2022, 1, 1) 
end = dt.date(2024, 12, 31)
months = MonthLocator(range(1,13), bymonthday=1, interval=1) # Every month
monthsFmt = DateFormatter("%b %Y") 
data = yf.Ticker(ticker) 
data = data.history(start=start, end=end) # Get historical data

"""
plot(data, type='candle', style='charles', title=f"{ticker} Price Chart 2022-2024",
     ylabel="Price ($)", mav=(20,50,100))
plots daily candlestick chart with 20, 50, 100 day moving averages
show()
"""

# Introduction to pandas
# Used for data manipulation and analysis, especially with tabular data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(np.mean(data['Age'])) 
# Calculates mean age
# Access data via column name df['Name'], df['Age']
# Access row data via iloc df.iloc[0] for first row




