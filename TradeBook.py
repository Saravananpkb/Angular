import sqlite3

class Trade:
  
  def __init__(self,*args):
    self.tradeId = args[0][0]
    self.tradeDate = args[0][1]
    self.stockName = args[0][2]
    self.tradeType = args[0][3]
    self.tradeQty = args[0][4]
    self.buyPrice = args[0][5]
    self.sellPrice = args[0][6]
    self.profit = args[0][7]
    self.status = args[0][8]
    self.tradeValue = args[0][9]
    self.netValue = args[0][10]
    self.otherId = args[0][11]
    pass

  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)

def getOpenBuyLowTrade(stockName):
    openBuyTrade = queryOpenBuyLowTrade(stockName)
    if(len(openBuyTrade)>0):
        trade = Trade(openBuyTrade[0])
        return trade

def queryOpenBuyLowTrade(stockName):
    sql = "SELECT * FROM TRADE_BOOK WHERE StockName = ? and TradeType = ? and Status = ? ORDER BY BuyPrice ASC limit 1"
    return executeStatement(sql,stockName,"B","Open")

def getOpenSellLatestTrade(stockName):
    openSellTrade = queryOpenSellLatestTrade(stockName)
    if(len(openSellTrade)>0):
        trade = Trade(openSellTrade[0])
        return trade

def queryOpenSellLatestTrade(stockName):
    sql = "SELECT * FROM TRADE_BOOK WHERE TradeType = ? and  Status = ? and StockName = ? ORDER BY TradeDate DESC limit 1"
    return executeStatement(sql,'S','Open',stockName)

def updateBuyTrade(tradePrice, profit, status, otherId, stockName, tradeId):
    sql = "UPDATE TRADE_BOOK set SellPrice = ? , Profit = ?, Status = ? , OtherId = ? WHERE StockName = ? and TradeId = ?"
    return executeStatement(sql,tradePrice, profit, status, otherId, stockName, tradeId)

def updateSellTrade(tradePrice, profit, status, otherId, stockName, tradeId):
    sql = "UPDATE TRADE_BOOK set BuyPrice = ? , Profit = ?, Status = ? , OtherId = ? WHERE StockName = ? and TradeId = ?"
    return executeStatement(sql,tradePrice, profit, status, otherId, stockName, tradeId)

def executeStatement(sql,*parameters):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute(sql,(parameters))
    data = (results.fetchall())
    #print(data)
    connection.commit()
    connection.close()
    return data