import pandas_datareader as pdr
spx_index = pdr.get_data_stooq('^SPX','2022-01-03','2022-01-10')
print(spx_index)