import sqlite3

class StockSummary():

    def __init__(self,*args):
        self.symbol = args[0][0]
        self.stockName = args[0][1]
        self.marketPrice = args[0][2]
        self.priceChg = args[0][4]
        self.totalQty = args[0][5]

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

def queryStocks():
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    query = "SELECT * FROM STOCK_SUMMARY"
    results = cursor.execute(query)
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data

def getStockSummary(stockName):
    summary = StockSummary(queryStockSummary(stockName)[0])
    return summary

def queryStockSummary(stockName):
    connection = sqlite3.connect("NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM STOCK_SUMMARY WHERE StockName = ?",(stockName,))
    data = (results.fetchall())
    print(data)
    connection.close()
    return data