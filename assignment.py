'''
hdbsjb
'''
#import libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
#import gold and btc 
BTCUSD = pd.read_csv("BTCUSD.csv", parse_dates = ["Date"], index_col = 0)
gold = pd.read_csv("Gold.csv", parse_dates = ["DATE"], index_col = 0)

#1
#log returns 
gold['LN_return'] = np.log(gold.GOLDAMGBD228NLBM) - np.log(gold.GOLDAMGBD228NLBM.shift(1))
BTCUSD['LN_return'] = np.log(BTCUSD['Adj Close']) - np.log(BTCUSD['Adj Close'].shift(1))
#2
#standard deviation of log returns
STD_BTCUSD_returns = np.std(BTCUSD.LN_return.dropna())
STD_gold_returns = np.std(gold.LN_return.dropna())

#3
#not sure what asking, looks like covar(?)

if __name__ == '__main__':
    print (STD_BTCUSD_returns, STD_gold_returns)