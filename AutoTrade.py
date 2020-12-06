import sqlite3
import TradeBookDao as tradeBookDao
import AnalysisImpl as analysisImpl
import DBDao as dbDao
import TradeBookImpl as tradeBookImpl

def autoTrade_V2():
    #Delete Results Table
    #dbDao.deleteResults()
    #Get List of stocks
    stocksTable = dbDao.queryStocks()
    print("Stocks Count : {}".format(len(stocksTable)))
    for stocksRow in stocksTable:
        result = {}
        symbol = stocksRow[0]
        stockName = stocksRow[1]
        #if(symbol == 'APLAPOLLO'):
        if(symbol is not None): # == 'CADILAHC'):
            print("############ Stock Name : {} ############".format(stockName))
            tradeBookImpl.calculate_Trade_Profit(stockName)
            equitySummaryTable = dbDao.queryEquitySummaryDetails(stockName)
            if(len(equitySummaryTable) != 0):
                limit15 = "15"
                history15days = dbDao.queryEquityHistory(symbol,limit15)
                limit3 = "3"
                history3days = dbDao.queryEquityHistory(symbol,limit3)

                if(len(history15days) != 0):
                    result = analysisImpl.getHighLowDays(result, history15days, limit15)
                    result = analysisImpl.getHighLowDays(result, history3days, limit3)
                    result['symbol'] = symbol
                    result['stockName'] = stockName
                    result['marketPrice'] = equitySummaryTable[0][5]
                    result['urProfit'] = equitySummaryTable[0][8]
                    result['price_per'] = equitySummaryTable[0][6]
                    result['quantity'] = equitySummaryTable[0][2]
                    result = analysisImpl.analysis(result)    
                    result = analysisImpl.buildSuggestion(result)
                    print("results {} ".format(result))
                    #analysisImpl.insertResults(result)
                    analysisImpl.updateResults(result)
                    #analysisImpl.prepareOrderBook(result)
    pass

#tradeBookImpl.calculate_Trade_Profit('LUPIN LIMITED')
autoTrade_V2()

#Buy Sell Diff Suggestion
#Buy Suggestion, Sell Suggestion, Short Sell Column, Qty, New Stocks, Track Multiple Buy, Repeat Buy Sell for Profit
#No improvement Stock

#if(HighDay >= 10, Previous Sell Check, Profit Curve) if(ShortBuySell) if(SellProfit < -500) if(SellProfit>X or 150)
#if(LowDay >=10, Check Previous Buy Check(SellProfit))
#TradeBook Automate
#Suggest Sell Price