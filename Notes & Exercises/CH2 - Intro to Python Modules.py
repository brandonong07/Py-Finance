# Page 31 - 69
# Python modules
# Group of programs written by others to serve specific functions
# Book explains NumPy, SciPPy, matplotlib, statsmodels, and Pandas

# Importing Modules
# imports all functions from math module
# if you want to name it something (import math as m) --> then use m.sqrt() etc.
import math as m 
import time as t
import numpy as np
import scipy as sp
import matplotlib as mp
import yfinance as yf

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

# Introduction to SciPy



