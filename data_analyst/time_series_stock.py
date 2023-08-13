import yfinance as yf
import pandas as pd
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df =tkr.history(period='300d')
# it return a dataframe as a result


# print(pd.concat([df['Close'],df['Close'].shift(2)],axis =1, keys = ['Close','2DaysShift']))
# pd.concat takes [df['Close'],df['Close'].shift(2)] as a first parameter.

import numpy as np
df['2DaysRise'] = np.log(df['Close']/df['Close'].shift(2))
print(df[['Close','2DaysRise']])

df['200DaysAverage'] = df['Close'].shift(1).rolling(200).mean()
# shift 1 so it calculate last 200 days mean, not including today.
print(df[['Close','200DaysAverage']])

# go through a few stocks and add them to stocks dataframe
stocks =pd.DataFrame()
tickers = ['MSFT','TSLA','GM','APPL','ORCL','AMZN']
for ticker in tickers:
    tkr = yf.Ticker(ticker)
    hist = tkr.history(period='1mo')
    print(hist['Close'])
    hist = pd.DataFrame(hist[['Close']].rename(columns={'Close':ticker}))
    if stocks.empty:
        stocks =hist
    else:
        stocks = stocks.join(hist)
print(stocks)

# check the less volatile stocks
stocks_to_keep = []
for i in stocks.columns:
    if stocks[stocks[i]/stocks[i].shift(1)<.97].empty:
        stocks_to_keep.append(i)
print(stocks[stocks_to_keep])        
