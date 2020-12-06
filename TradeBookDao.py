import sqlite3

def queryTradeBook_BuyOpenByStockAscPrice(stockName):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM TRADE_BOOK WHERE STOCK_NAME = ? and TradeType = ? and STATUS = ? ORDER BY Market_Price ASC",(stockName,'B','Open'))
    data = (results.fetchall())
    print(data)
    connection.close()
    return data

def queryTradeBook_SellOpenByStockDescDate(stockName):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM TRADE_BOOK WHERE TradeType = ? and  STATUS = ? and STOCK_NAME = ? ORDER BY TRADE_DATE DESC",('S','Open',stockName,))
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data
    
def updateTradeBook_Status(stockName,tradeId,status):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("UPDATE TRADE_BOOK set Status = ? WHERE STOCK_NAME = ? and TRADE_ID = ?",(status,stockName,tradeId,))
    data = (results.fetchall())
    print(data)
    connection.commit()
    connection.close()
    return data

def updateTradeBook_Status_Profit(stockName,tradeId,status,sellPrice, profit, sellTradeId):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("UPDATE TRADE_BOOK set Status = ? , SellPrice = ? , Profit = ?, SELL_TRADE_ID = ? WHERE STOCK_NAME = ? and TRADE_ID = ?",(status, sellPrice, profit, sellTradeId, stockName,tradeId,))
    data = (results.fetchall())
    #print(data)
    connection.commit()
    connection.close()
    return data

def queryTradeBook_BuyOpen():
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM TRADE_BOOK WHERE TradeType = 'B' and STATUS = 'Open' ORDER BY TRADE_DATE DESC")
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data

def queryTradeBook_2(stockName):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM TRADE_BOOK WHERE STOCK_NAME = ? ORDER BY TRADE_DATE DESC",(stockName,))
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data