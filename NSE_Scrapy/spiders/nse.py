# -*- coding: utf-8 -*-
import scrapy
import sqlite3

def getStocks():
    connection = sqlite3.connect("NSE.db")
    cursor = connection.cursor()
    results = cursor.execute("SELECT STOCK_SYMBOL FROM STOCKS")
    stocks = results.fetchall()
    stockList = []
    for stock in stocks:
        stockList.append(stock[0])
    print(stockList)
    return stockList

class NseSpider(scrapy.Spider):
    name = 'nse'
    allowed_domains = ['www1.nseindia.com']
    start_urls = ['http://www1.nseindia.com/']

    def start_requests(self):
        stocks = getStocks()
        for stock in stocks:
            print(stock)
            #url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+stock+'&series=EQ&fromDate=undefined&toDate=undefined&datePeriod=3day'
            #https://www.nseindia.com/api/quote-equity?symbol=HDFCBANK
            url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol='+stock+'&series=EQ&fromDate=29-Nov-2020&toDate=10-Dec-2020&undefined&hiddDwnld=false'
            print(url)
            yield scrapy.Request(url,callback=self.parse, headers={
                 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            })
    
    def parse(self, response):
        print("Parse method")
        rows = response.xpath("//tbody/tr")
        print(len(rows))
        for row in rows:
            if(rows.index(row) == 0):
                headers = row.xpath(".//th/text()").getall()
            columnValues = row.xpath(".//td/text()").getall()
            #print(columnValues)
            record = createRecord(headers,columnValues)
            #print(type(record))
            yield{
                'record':record
            }

def createRecord(headers,columnValues):
    record = {} 
    for key in headers: 
        for value in columnValues: 
            record[key] = value 
            columnValues.remove(value) 
            break
    print("##################### record ###############################")
    print(record)
    return record