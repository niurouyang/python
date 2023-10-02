import yfinance as yf

ticker ='AAPL'
tkr = yf.Ticker(ticker)
hist = tkr.history(period='1d')

print(hist.iloc[0]['Close'])