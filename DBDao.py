import sqlite3

def queryEquitySummaryDetails(stockName):
    connection = sqlite3.connect("NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM EQUITY_SUMMARY_DETAILS WHERE STOCK_NAME = ?",(stockName,))
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data

def queryEquityHistory(stock,limit):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM EQUITY_HISTORY WHERE Symbol = ? order by Date desc limit ?", (stock,limit))
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data

def queryStocks():
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    query = "SELECT * FROM STOCKS"
    results = cursor.execute(query)
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data

def queryResults():
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM RESULTS")
    data = (results.fetchall())
    #(data)
    connection.close()
    return data

def deleteResults():
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM RESULTS")
    connection.commit()
    connection.close()  