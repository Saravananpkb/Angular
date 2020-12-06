import TradeBookDao
import sqlite3

def buildSuggestion(result):
    result['SellRecommend'] = ''
    result['BuyRecommend'] = ''
    if(result['daysHigh'] >= 10):
        if(result['quantity'] > 1):
            #Previous Sell Check, Profit Curve
            if(result['sellProfit'] == ''):
                result['SellRecommend'] = 'Sell'
            elif(result['sellProfit'] >= 100):
                result['SellRecommend'] = 'Sell'
            else:
                pass

    if(result['sellProfit'] == ''):
        pass
    elif(result['sellProfit'] >= 100):
            result['SellRecommend'] = 'Sell'

    if(result['profit_10DH_Mkt'] >= 100):
        if(result['sellProfit'] == ''):
            result['BuyRecommend'] = ''#'BuyShort'
        elif(result['sellProfit'] <= -100):
            result['BuyRecommend'] = ''#'BuyShortOnLoss'
        else:
            result['BuyRecommend'] = ''#'BuyShortNot'
    
    if(result['daysLow'] >= 10):
        if(result['sellProfit'] == ''):
            result['BuyRecommend'] = 'Buy'
        elif(result['sellProfit'] <= -100):
            result['BuyRecommend'] = 'BuyOnLoss'
        else:
            result['BuyRecommend'] = ''#'BuyNot'

    return result

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

def calculateBuyProfit(buyPrice,sellPrice):
   qty = 5000/buyPrice
   unitProfit = sellPrice - buyPrice
   totalProfit = qty * unitProfit
   print(totalProfit)
   return round(totalProfit)

def calculateSellProfit(stockName,marketPrice):
    tradeTable = TradeBookDao.queryTradeBook_2(stockName)
    buyPriceList = []
    for tradeRow in tradeTable:
        if(tradeRow[2] == 'B' and tradeRow[7] != 'Closed'):
            buyPriceList.append(tradeRow[4])
    if(buyPriceList):
        buyPrice = min(buyPriceList)
    for tradeRow in tradeTable:
        if(tradeRow[2] == 'B' and tradeRow[7] != 'Closed' and tradeRow[4] == buyPrice):
            qty = tradeRow[3]
            charges = round(((tradeRow[5] + tradeRow[6]) * 2))
            netProfit = calculateProfit(buyPrice,marketPrice,qty,charges)
            print("Net Sell Profit: {}".format(netProfit))
            sellInfo = {'buyPrice':buyPrice,'sellProfit':netProfit}
            return sellInfo

def formatPrice(rawPrices):
    formattedPrice = []
    for aday in rawPrices:
        if(type(aday) != float):
            if(',' in aday):
                formattedPrice.append(float(aday.replace(',','')))
            else:
                formattedPrice.append(float(aday))
        else:
            formattedPrice.append(aday)
    return formattedPrice

def getHighLowDays(record, historydays, limit):
    highdaysRaw = []
    lowdaysRaw = []
    
    for aday in historydays:
        highdaysRaw.append(aday[4])
        lowdaysRaw.append(aday[5])

    if(limit == "15"):
        record['high15days'] = formatPrice(highdaysRaw)
        print("high15days : {}".format(record['high15days']))
        record['low15days'] = formatPrice(lowdaysRaw)
        print("low15days : {}".format(record['low15days']))
    if(limit == "3"):
        record['High3Days'] = max(formatPrice(highdaysRaw))
        print("High3Days : {}".format(record['High3Days']))
        record['Low3Days'] = min(formatPrice(lowdaysRaw))
        print("Low3Days : {}".format(record['Low3Days']))     
    return record

def getHighDays(result):
    daysHigh = 0
    for aday in result['high15daysSorted']:
        if(result['marketPrice'] > float(aday)):
            daysHigh = daysHigh + 1
    result['daysHigh'] = daysHigh
    print('daysHigh {}'.format(result['daysHigh']))
    return result

def getLowDays(result):
    daysLow = 0
    for aday in result['low15daysSorted']:
        if(result['marketPrice'] > float(aday)):
            pass
        else:
            daysLow = daysLow +1
    result['daysLow'] = daysLow
    print("daysLow : {}".format(result['daysLow']))
    return result

def analysis(result):
    high15daysSorted = []
    low15daysSorted = []
    
    high15daysSorted = result['high15days']
    high15daysSorted.sort()
    result['high15daysSorted'] = high15daysSorted
    print("high15days Sorted: {}".format(result['high15daysSorted']))
    
    result['high10Day'] = result['high15daysSorted'][9]
    print("high10Day: {}".format(result['high10Day']))

    low15daysSorted = result['low15days']
    low15daysSorted.sort()
    low15daysSorted.reverse()
    result['low15daysSorted'] = low15daysSorted
    print("low15days Sorted Reverse : {}".format(result['low15daysSorted']))
    
    result['low10Day'] = result['low15daysSorted'][9]
    print("low10Day: {}".format(result['low10Day']))

    result = getHighDays(result)
    result = getLowDays(result)
    
    profit_10DH_Mkt = calculateProfit(result['marketPrice'],result['high10Day'],None,None)
    print("BuyProfit : {}".format(profit_10DH_Mkt))

    profit_10DH_L = calculateProfit(result['low10Day'],result['high10Day'],None,None)
    print("Profit_HL : {}".format(profit_10DH_L))

    sellInfo = calculateSellProfit(result['stockName'],result['marketPrice'])
    print("sellInfo : {}".format(str(sellInfo)))

    buyPrice = ''
    sellProfit = ''
    if(sellInfo):
        buyPrice = sellInfo['buyPrice']
        sellProfit = sellInfo['sellProfit']

    result['profit_10DH_Mkt'] = profit_10DH_Mkt
    result['sellProfit'] = sellProfit
    result['buyPrice'] = buyPrice
    result['profit_10DH_L'] = profit_10DH_L
    return result

def updateResults(result):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE RESULTS SET High3Days = ? , Low3Days = ? , SellRmd = ?, BuyRmd = ?, marketPrice = ?, daysHigh = ?, sellProfit = ?, daysLow =?, buyProfit =?, price_per =?, Qty=?, UR_Profit =?, buyPrice =?, low10Day=?, high10day=?, profit_HL=? where Symbol = ?",(result['High3Days'], result['Low3Days'],result['SellRecommend'],result['BuyRecommend'],result['marketPrice'], result['daysHigh'], result['sellProfit'],  result['daysLow'], result['profit_10DH_Mkt'], result['price_per'], result['quantity'], result['urProfit'], result['buyPrice'], result['low10Day'], result['high10Day'], result['profit_10DH_L'],result['symbol'],))
    connection.commit()
    connection.close()

def insertResults(result):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS RESULTS(High3Days DOUBLE, Low3Days DOUBLE, Symbol TEXT, Suggestion TEXT, MarketPrice DOUBLE, DaysHigh DOUBLE, SellProfit DOUBLE, DaysLow DOUBLE, BuyProfit DOUBLE, Price_Per DOUBLE,  Qty DOUBLE, UR_Profit DOUBLE,  BuyPrice DOUBLE, Low10Day DOUBLE, High10Day DOUBLE, Profit_HL DOUBLE, Remarks TEXT)")
    connection.commit()
    cursor.execute("INSERT INTO RESULTS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(result['High3Days'], result['Low3Days'],result['symbol'], result['suggestion'], result['marketPrice'], result['daysHigh'], result['sellProfit'],  result['daysLow'], result['profit_10DH_Mkt'], result['price_per'], result['quantity'], result['urProfit'], result['buyPrice'], result['low10Day'], result['high10Day'], result['profit_10DH_L'],''))
    connection.commit()
    connection.close()

def prepareOrderBook(result):
    if(result['suggestion'] in ['Sell','Buy','BuyShort','BuyOnLoss','BuyShortOnLoss']):
        order = {}
        order['ORDER_DATE'] = 2020-10-15
        order['STOCK_NAME'] = result['symbol']
        order['OrderType'] = result['suggestion']
        order['Qty'] = result['quantity']
        order['MarketPrice'] = result['marketPrice']
        order['Status'] = ''
        insertOrderBook(order)

def insertOrderBook(order):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO ORDER_BOOK VALUES(?,?,?,?,?,?)",(order['ORDER_DATE'], order['STOCK_NAME'],order['OrderType'], order['Qty'], order['MarketPrice'], order['Status']))
    connection.commit()
    connection.close()