import sqlite3

def queryResultsByStock(stockName):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT * FROM RESULTS WHERE ORDERSTATUS = 'Executed' and Symbol = ?", (stockName,))
    data = (results.fetchall())
    print(data)
    connection.close()
    return data

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

def getGrowth(result, symbol):
    sql = "select cast(replace(lasttradedprice,',','') as double) as highprice from Stock_History where symbol = ? order by date desc limit 26"
    ltprices = executeStatement(sql,symbol)
    week1 = ltprices[0][0]
    week2 = ltprices[5][0]
    week3 = ltprices[10][0]
    week4 = ltprices[15][0]
    week5 = ltprices[20][0]
    week6 = ltprices[25][0]
    growthNetWeeks = 0
    if(week1 > week2):
        growthNetWeeks = growthNetWeeks+1
    if(week2 > week3):
        growthNetWeeks = growthNetWeeks+1
    if(week3 > week4):
        growthNetWeeks = growthNetWeeks+1
    if(week4 > week5):
        growthNetWeeks = growthNetWeeks+1
    if(week5 > week6):
        growthNetWeeks = growthNetWeeks+1

    if(week1 > week6):
        growth = 'INC'
    else:
        growth = 'DEC'

    print("Growth {}".format(growth))
    print("GrowthNetWeeks {}".format(growthNetWeeks))
    result.growth = growth
    result.growthNetWeeks = growthNetWeeks

    return result