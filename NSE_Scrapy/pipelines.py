# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
import sqlite3
#from datetime import datetime

class NseScrapyPipeline(object):
    
    def open_spider(self,spider):
        print("Creating table...")
        self.connection = sqlite3.connect("NSE.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS EQUITY_HISTORY(Date DATE, Symbol TEXT, Series TEXT, OpenPrice DOUBLE, HighPrice DOUBLE, LowPrice DOUBLE, LastTradedPrice DOUBLE, ClosePrice DOUBLE)")
        self.connection.commit()

    def process_item(self, item, spider):
        print("Inserting records...")
        record = item.get('record')
        #print(record)
        date = datetime.strptime(record.get('Date'), '%d-%b-%Y')
        if(record):
            self.cursor.execute("INSERT INTO EQUITY_HISTORY VALUES(?,?,?,?,?,?,?,?)",(date,record.get('Symbol'),record.get('Series'),record.get('Open Price'),record.get('High Price'),record.get('Low Price'),record.get('Last Traded Price ').strip(),record.get('Close Price')))
            self.connection.commit()
        return item

    def close_spider(self, spider):
        print("Closing Connection...")
        self.connection.close()