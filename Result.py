import sqlite3

class Result:
  
  def __init__(self):
    self.symbol = ''
    self.sellRmd = ''
    self.highIn15Days = ''
    self.profit = ''
    self.marketPrice1 = ''
    self.high3Days = ''
    self.buyPrice = ''
    self.buyQty = ''
    self.totalQty = ''
    self.buyRmd = ''
    self.profit1M = ''
    self.status = ''
    self.profitExp = ''
    self.lowIn15Days = ''
    self.marketPrice2 = ''
    self.low3Days = ''
    self.profit10DayHL = ''
    self.low10Days = ''
    self.high10Days = '' 
    self.priceChg = ''
    self.bundleQty = ''
    self.crtBundleQty = ''
    self.qtyLevel = ''

    pass

  def __str__(self):
    return str(self.__class__) + ": " + str(self.__dict__)
  
  def updateResults(result):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    
    cursor.execute("UPDATE RESULTS SET \
    SellRmd = ?, daysHigh = ?,  sellProfit = ?, marketPrice1 = ?, buyPrice = ?, buyQty = ?, bundleQty = ?, \
    TotalQty = ?, High3Days = ?, BuyRmd = ?, profit1M = ?, qtyLevel = ?, daysLow = ?, marketPrice2 = ?,\
    Low3Days = ?, buyProfit =?, profit_HL=?, price_per =?, low10Day=?, high10day=? where Symbol = ?",
    (result.sellRmd, result.highIn15Days, result.profit, result.marketPrice1, result.buyPrice, result.buyQty, result.bundleQty,
    result.totalQty, result.high3Days, result.buyRmd, result.profit1M, result.qtyLevel, result.lowIn15Days, result.marketPrice2,
    result.low3Days, result.profitExp, result.profit10DayHL, result.priceChg, result.low10Days, result.high10Days, result.symbol))

    connection.commit()
    connection.close()