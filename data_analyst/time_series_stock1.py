import yfinance as yf
import numpy as np
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='1mo')

df = df[['Close','Volume']].rename(columns={'Close':'Price'})
df['priceRise'] = np.log(df['Price']/df['Price'].shift(1))
#price difference verse last day
df['volumeRise'] = np.log(df['Volume']/df['Volume'].shift(1))
#volume difference verse last day
print(df)

print(df[abs(df['priceRise'])>0.5])
# print just those rows where priceRise exceeds the threshold
print(df['volumeRise'].mean().__round__(4))
#calculate the average volume change over the entire series
print(df[abs(df['priceRise'])>0.5]['volumeRise'].mean().__round__(4))
#calculate the average volume change for just those rows with above-average changes in price