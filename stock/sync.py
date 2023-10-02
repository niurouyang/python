import pandas as pd
import yfinance as yf
import mysql.connector

try:
    cnx=mysql.connector.connect(user='root',password='8228198',
                                host='127.0.0.1',
                                database='try')
    
    def Get_dividend(tkr):
        dividend = tkr.dividends
        last_dividend = dividend.iloc[-1]
        return last_dividend
    
    def Get_price(tkr):
        hist = tkr.history(period='1d')
        return hist.iloc[0]['Close']


    
    cursor = cnx.cursor()
    query_open_table= ("select * from canadian_dividend")
    cursor.execute(query_open_table)
    rows = cursor.fetchall()
    for Stock_ID in rows: # cursor will contain all the information in canadian_dividend table
        ticker = Stock_ID[1]
        tkr = yf.Ticker(ticker)
        #if tkr is None:
        #    continue
        latest_dividend = Get_dividend(tkr)
        latest_price = Get_price(tkr)
        latest_dividend_rate = latest_dividend*4/latest_price
        query_update_stock=("update canadian_dividend set dividend = %s, stock_price =%s, dividend_rate = %s where stock_symbol = %s")
        cursor.execute(query_update_stock,(latest_dividend,latest_price,latest_dividend_rate,ticker))
    cnx.commit()


    






except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))

finally:
    cursor.close()
    cnx.close()