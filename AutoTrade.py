from Result import Result 
import StockSummary 
import StockHistory 
import TradeBook
import AnalysisImpl 

def AutoTrade():
    
    stocksRows = StockSummary.queryStocks()  
    print("Stocks Count : {}".format(len(stocksRows)))

    for stocksRow in stocksRows:
        symbol = stocksRow[0]
        stockName = stocksRow[1]
        
        #if(symbol == 'ADANIENT'):
        if(symbol is not None):
            print("############ Stock Name : {} ############".format(stockName))

            #analysisImpl.insertTradeDetail(result)
            AnalysisImpl.updateTradeProfit(stockName)

            result = Result()           
            result.symbol = symbol
            
            stockSummary = StockSummary.getStockSummary(stockName)
            result.marketPrice1 = stockSummary.marketPrice
            result.marketPrice2 = stockSummary.marketPrice
            result.priceChg = stockSummary.priceChg
            result.totalQty = stockSummary.totalQty
            #print(stockSummary)

            result.high3Days = StockHistory.queryhighXDays(symbol,"3")
            result.low3Days = StockHistory.querylowXDays(symbol,"3") 
            result.high10Days = StockHistory.queryhighXDays(symbol,"10")
            result.low10Days = StockHistory.querylowXDays(symbol,"10") 
            result.highIn15Days = StockHistory.queryHighInXDays(symbol,"15",stockSummary.marketPrice) 
            result.lowIn15Days = StockHistory.queryLowInXDays(symbol,"15",stockSummary.marketPrice) 
            ltprices = StockHistory.get1MonthLTP(symbol)

            result.profit1M = AnalysisImpl.calculateProfit(ltprices[25][0],ltprices[0][0],None,None)
            result.profitExp = AnalysisImpl.calculateProfit(stockSummary.marketPrice,result.high10Days,None,None)
            result.profit10DayHL = AnalysisImpl.calculateProfit(result.low10Days,result.high10Days,None,None)

            buyTrade = TradeBook.getOpenBuyLowTrade(stockName)
            if(buyTrade is not None):
                result.buyQty = buyTrade.tradeQty
                result.buyPrice = buyTrade.buyPrice
                print(buyTrade)
                charges = round(((buyTrade.tradeValue + buyTrade.netValue) * 2))
                print("charges : {}".format(charges))
                result.profit = AnalysisImpl.calculateProfit(buyTrade.buyPrice,
                                stockSummary.marketPrice,buyTrade.tradeQty,charges)

            #result = AnalysisImpl.buildSuggestion(result)
            result = AnalysisImpl.smartSuggestion(result)

            Result.updateResults(result)
            print(result)
    pass

AutoTrade()