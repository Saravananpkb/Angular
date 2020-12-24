import sqlite3

class StockHistory():

    def __init__(self,*args):
        self.highPrice = args[0][4]

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

def get1MonthLTP(symbol):
    sql = "select cast(replace(lasttradedprice,',','') as double) as highprice from Stock_History where symbol = ? order by date desc limit 26"
    ltprices = executeStatement(sql,symbol)
    return ltprices

def queryhighXDays(symbol,limit):
    sql = "select highprice from (select cast(replace(highprice,',','') as double) as highprice from Stock_History where symbol = ? \
           order by date desc limit ?) order by highprice desc limit 1"  
    return executeStatement(sql,symbol,limit)[0][0]

def querylowXDays(symbol,limit):
    sql = "select lowprice from (select cast(replace(lowprice,',','') as double) as lowprice from Stock_History where symbol = ? \
           order by date desc limit ?) order by lowprice asc limit 1"  
    return executeStatement(sql,symbol,limit)[0][0]

def queryHighInXDays(symbol,limit,marketPrice):
    sql = "select count(*) from (select cast(replace(highprice,',','') as double) as highprice from Stock_History where symbol = ? \
           order by date desc limit ?) where highprice < ?"
    return executeStatement(sql,symbol,limit,marketPrice)[0][0]

def queryLowInXDays(symbol,limit,marketPrice):
    sql = "select count(*) from (select cast(replace(lowprice,',','') as double) as lowprice from Stock_History where symbol = ? \
           order by date desc limit ?) where lowprice > ?"
    return executeStatement(sql,symbol,limit,marketPrice)[0][0]
    
def executeStatement(sql,*parameters):
    connection = sqlite3.connect("D:\\Software Program\\Python\\TradeApp\\NSE.db")
    cursor = connection.cursor()
    results = cursor.execute(sql,(parameters))
    data = (results.fetchall())
    #print(data)
    connection.close()
    return data