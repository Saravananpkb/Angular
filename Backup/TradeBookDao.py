import sqlite3

class Trade:
  
  def __init__(self,*args):
    self.tradeDate = args[0][0]
    self.stockName = args[0][1]
    self.tradeType = args[0][2]
    self.tradeQty = args[0][3]
    self.tradePrice = args[0][4]
    self.tradeValue = args[0][5]
    self.netValue = args[0][6]
    self.status = args[0][7]
    self.sellPrice = args[0][8]
    self.profit = args[0][9]
    self.tradeId = args[0][10]
    self.sellTradeId = args[0][11]
    pass

  def __str__(self):
    print ("TradeDate : {}, StockName : {} , TradeType : {} ".format(self.tradeDate, \
        self.stockName, self.tradeType))
    return ""

def insertTrade(trade):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    connection.execute("INSERT INTO TRADE_BOOK (TRADE_DATE,STOCK_NAME,TradeType,Qty,Market_Price,Market_Value,NetAmount) Values (?,?,?,?,?,?,?)",\
        ('2020-12-13','LUPIN LIMITED',trade.tradeType,trade.tradeQty,trade.tradePrice,trade.tradeValue,trade.netValue))
    connection.commit()
    connection.close()

def queryTradeBook_BuyOpenByStockAscPrice(stockName):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM TRADE_BOOK WHERE STOCK_NAME = ? and TradeType = ? and STATUS = ? ORDER BY Market_Price ASC",(stockName,'B','Open'))
    data = (results.fetchall())
    #print(data)
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
    
def updateStatusProfit(stockName,tradeId,status,sellPrice, profit, sellTradeId):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("UPDATE TRADE_BOOK set Status = ? , SellPrice = ? , Profit = ?, SELL_TRADE_ID = ? WHERE STOCK_NAME = ? and TRADE_ID = ?",(status, sellPrice, profit, sellTradeId, stockName,tradeId,))
    data = (results.fetchall())
    #print(data)
    connection.commit()
    connection.close()
    return data











def updateTradeBook_Status(stockName,tradeId,status):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("UPDATE TRADE_BOOK set Status = ? WHERE STOCK_NAME = ? and TRADE_ID = ?",(status,stockName,tradeId,))
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