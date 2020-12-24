import sqlite3
import TradeBookDao as tradeBookDao
import AnalysisImpl as analysisImpl
import DBDao as dbDao
import TradeBookImpl as tradeBookImpl

def autoTrade():
    #Get List of stocks
    stocksRows = dbDao.queryStocks()
    print("Stocks Count : {}".format(len(stocksRows)))
    
    for stocksRow in stocksRows:
        result = {}
        symbol = stocksRow[0]
        stockName = stocksRow[1]
        result['symbol'] = symbol

        #if(symbol == 'NATCOPHARM'):
        if(symbol is not None):
            print("############ Stock Name : {} ############".format(stockName))
            
            #analysisImpl.insertTradeDetail(result)
            tradeBookImpl.updateTradeProfit(stockName)

            equitySummaryTable = dbDao.queryEquitySummaryDetails(stockName)
            if(len(equitySummaryTable) != 0):
                limit15 = "15"
                history15days = dbDao.queryEquityHistory(symbol,limit15)
                limit3 = "3"
                history3days = dbDao.queryEquityHistory(symbol,limit3)

                if(len(history15days) != 0):
                    result = analysisImpl.getHighLowDays(result, history15days, limit15)
                    result = analysisImpl.getHighLowDays(result, history3days, limit3)
                    result['stockName'] = stockName
                    result['marketPrice'] = equitySummaryTable[0][5]
                    result['urProfit'] = equitySummaryTable[0][8]
                    result['price_per'] = equitySummaryTable[0][6]
                    result['quantity'] = equitySummaryTable[0][2]
                    result = analysisImpl.calculateDiffProfits(result)
                    result = analysisImpl.calculateSellProfit(result)    
                    result = analysisImpl.buildSuggestion(result)
                    print("results {} ".format(result))
                    analysisImpl.updateResults(result)
    pass

autoTrade()
#tradeBookImpl.updateTradeProfit('ICICI SECURITIES LIMITED')
#tradeBookImpl.updateTradeProfit('TATA CONSULTANCY SERVICES LIMITED')