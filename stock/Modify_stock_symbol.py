import mysql.connector
import re

stocklist = []
with open('Canadian_dividend_stock_list.txt','r') as stock_list:
    for line in stock_list:
        modified_line = re.sub(r'^\d*\.','',line) # to remove the number and first dot in the string
        stocklist.append(modified_line.strip())
#print(stocklist)

try:
    cnx=mysql.connector.connect(user='root',password='8228198',
                                host='127.0.0.1',
                                database='try')
    cursor = cnx.cursor()
    for index, value in enumerate(stocklist):
        query = ("""update canadian_dividend set stock_symbol = %s where stockID = %s""")
        cursor.execute(query,(value,(index+1)))
    cnx.commit()
    
except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))

finally:
    cursor.close()
    cnx.close()
