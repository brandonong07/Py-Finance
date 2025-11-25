# Variable Assignment:
pv = 100
# pv has a value of 100

# Calculate value of this money if annual rate is 1.5%, 3yrs)
pv*(1+0.015)**3

# Python Loops & Conditionals

# Simple Loop Example:
for i in range(5):
    print("Iteration number:", i)

# enumerate() function generates pair of indices starting from 0 and its corresponding value
x=["a", "b", "z"]
for i, value in enumerate (x):
    print(i, value)

# Conditional Example:
age = 15
if age < 18:
    print("Minor")
else:
    print("Adult")

# Data input
# Example: Yahoo Finance pricing IBM

import yfinance as yf
data = yf.Ticker("IBM")
data.history(period="5d")

# Accessing specific columns
print(data.history(period="5d")['Close'])
print(data.history(period="5d")['Volume'])

# Accessing certain days
print(data.history(period="5d").iloc[0]) # First day

# Data manipulation
# help(''.split) Learning more about functions, and using help() function
s = "Hello, World!"
s_list = s.split(",")  # Splits string into list at comma
print(s_list)



