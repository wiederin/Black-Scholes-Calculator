from datetime import datetime, date
import pandas_datareader.data as web
import numpy as np
import black_scholes_model as bs
import cmath

# stock info
stock = 'SPY'
expiry = '06-13-2022'
k = 335


# date info
today = datetime.now()
last_year = today.replace(year=today.year - 1)


# data from web
df = web.DataReader(stock, 'yahoo', last_year, today)
# sort data
df = df.sort_values(by="Date")
# drop not available
df = df.dropna()
# close from day before
# add close from day before to df
df['close_day_before'] = df.Close.shift(1)
# calculate return and add to df
df['returns'] = ((df.Close - df.close_day_before) / df.close_day_before)

# calculate sigma
sigma = float(np.sqrt(252) * df['returns'].std())

# get risk-free interest rate
r = float((web.DataReader("^TNX", 'yahoo', today.replace(day=today.day - 1), today)['Close'].iloc[-1])/100)

# get stock price
s = int(df['Close'].iloc[-1])

# get time to maturity
t = float((datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365)

#print('The d1 is: ', bs.d1(s, k, t, r, sigma))
#print('The d2 is: ', bs.d2(s, k, t, r, sigma))
print('The Option Price is: ', bs.black_scholes_call(s, k, t, r, sigma))
