import TradeBookDao
import sqlite3

def calculateBuyProfit(buyPrice,sellPrice):
   qty = 5000/buyPrice
   unitProfit = sellPrice - buyPrice
   totalProfit = qty * unitProfit
   print(totalProfit)
   return round(totalProfit)

def calculateSellProfit(stockName,marketPrice):
    tradeTable = TradeBookDao.queryTradeBook_2(stockName)
    for tradeRow in tradeTable:
        if(tradeRow[2] == 'B' and tradeRow[7] != 'Closed'):
            qty = tradeRow[3]
            buyPrice = tradeRow[4]
            charges = round(((tradeRow[5] + tradeRow[6]) * 2))
            netProfit = calculateProfit(buyPrice,marketPrice,qty,charges)
            print("Net Sell Profit: {}".format(netProfit))
            sellInfo = {'buyPrice':buyPrice,'sellProfit':netProfit}
            return sellInfo

def analysis(symbol,stockName,marketPrice,history15days,price_per,urProfit):
    high15days = []
    low15days = []

    for aday in history15days:
        #print(aday[5])
        #print(type(aday[5]))        
        if(type(aday[4]) != float):
            if(',' in aday[4]):
                high15days.append(float(aday[4].replace(',','')))
            else:
                high15days.append(float(aday[4]))
        else:
            high15days.append(aday[4])

        if(type(aday[5]) != float):
            if(',' in aday[5]):
                low15days.append(float(aday[5].replace(',','')))
            else:
                low15days.append(float(aday[5]))
        else:
            low15days.append(aday[5])

    print("high15days : {}".format(high15days))
    high15days.sort()
    high10Day = high15days[9]
    print("high15days Sorted: {}".format(high15days))
    print("high10Day: {}".format(high10Day))

    print("low15days : {}".format(low15days))
    low15days.sort()
    low15days.reverse();
    print("low15days Sorted Reverse : {}".format(low15days))
    low10Day = low15days[9]
    print("low10Day : {}".format(low10Day))

    cpGhigh = 0;
    cpLhigh = 0;
    for aday in high15days:
        if(marketPrice > float(aday)):
            cpGhigh = cpGhigh + 1
        else:
            cpLhigh = cpLhigh +1

    print("cpGhigh : {}".format(cpGhigh))
   
    cpGLow = 0;
    cpLLow = 0;
    for aday in low15days:
        if(marketPrice > float(aday)):
            cpGLow = cpGLow + 1
        else:
            cpLLow = cpLLow +1
    print("cpLLow : {}".format(cpLLow))
    
    #profit_10DH_Mkt = calculateProfit(marketPrice,high10Day,None,None)
    #print("BuyProfit : {}".format(profit_10DH_Mkt))
    #profit_10DH_L = calculateProfit(low10Day,high10Day,None,None)
    #print("Profit_HL : {}".format(profit_10DH_L))
    sellInfo = calculateSellProfit(stockName,marketPrice)
    print("sellInfo : {}".format(str(sellInfo)))
    buyPrice = None
    sellProfit = None
    if(sellInfo):
        buyPrice = sellInfo['buyPrice']
        sellProfit = sellInfo['sellProfit']
    insertResults(symbol, marketPrice, price_per, cpLLow, profit_10DH_Mkt, cpGhigh, urProfit, buyPrice, sellProfit, low10Day, high10Day, profit_10DH_L)

def insertResults(symbol, marketPrice, price_per, cpLLow, profit_10DH_Mkt, cpGhigh, urProfit, buyPrice, sellProfit, low10Day, high10Day, profit_10DH_L):
    connection = sqlite3.connect("D:\\Software Program\\Workspace\\Python\\NSE_Scrapy\\NSE.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS RESULTS(Symbol TEXT, MarketPrice DOUBLE, Price_Per DOUBLE, NoOfDaysLow DOUBLE, BuyProfit DOUBLE, NoOfDaysHigh DOUBLE, UR_Profit DOUBLE, BuyPrice DOUBLE, SellProfit DOUBLE, Low10Day DOUBLE, High10Day DOUBLE, Profit_HL DOUBLE, Remarks TEXT)")
    connection.commit()
    cursor.execute("INSERT INTO RESULTS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(symbol, marketPrice, price_per, cpLLow, profit_10DH_Mkt, cpGhigh, urProfit, buyPrice, sellProfit, low10Day, high10Day, profit_10DH_L,''))
    connection.commit()
    connection.close()

def calculateProfit(buyPrice,sellPrice,qty,charges):
    if(qty == None):
        print("Qty None")
        qty = 5000/buyPrice
        qty = round(qty)
        print("Qty {}".format(qty))
    unitProfit = sellPrice - buyPrice
    totalProfit = round(qty * unitProfit)
    print("TotalProfit: {}".format(totalProfit))
    if(charges == None):
       charges = -70
    print("charges: {}".format(charges))  
    netProfit = totalProfit + charges  
    print("NetProfit: {}".format(netProfit))
    return netProfit