import TradeBook
import sqlite3
import math

def updateTradeProfit(stockName):

    buyTrade = TradeBook.getOpenBuyLowTrade(stockName)
    print("Buy Trade : {}".format(buyTrade))

    if(buyTrade is not None):
        sellTrade = TradeBook.getOpenSellLatestTrade(stockName)
        print("Sell Trade : {}".format(sellTrade))
        
        if(sellTrade is not None):    
            profit = round(buyTrade.netValue + sellTrade.netValue)
            print("Profit : {}".format(profit))
                
            TradeBook.updateBuyTrade(sellTrade.sellPrice, profit, 'Closed', sellTrade.tradeId, stockName, buyTrade.tradeId)
            TradeBook.updateSellTrade(buyTrade.buyPrice, profit, 'Closed', buyTrade.tradeId, stockName, sellTrade.tradeId)
            print("Buy Sell Trade updated for : {}".format(stockName))
    pass

def smartSuggestion(result):
    result.bundleQty = getBundleQty(result.marketPrice1)
    result.crtBundleQty = math.floor((result.totalQty) / (result.bundleQty))
    print("result.crtBundleQty {}: ".format(result.crtBundleQty))

    if(result.profit1M >= 500):
        if(result.crtBundleQty > 2):
            result.qtyLevel = 'Sufficent'
        else:
            result.qtyLevel = 'Lag'
    elif(result.profit1M >= 200):
        if(result.crtBundleQty > 1):
            result.qtyLevel = 'Sufficent'
        else:
            result.qtyLevel = 'Lag'
    else:
        result.qtyLevel = ''

    print("result.qtyLevel {}: ".format(result.qtyLevel))

    if(result.profit == ''):
        if(result.highIn15Days >= 10):
            if(result.totalQty > 0):
              result.sellRmd = 'Sell'    
    else:
        if((result.profit > 100) or (result.highIn15Days >= 10)):
            if(result.totalQty > 0):
                result.sellRmd = 'Sell'
                if(result.marketPrice1 > result.high3Days):
                   result.sellRmd = 'Sell-Now'

    if((result.profitExp >= 300) or (result.lowIn15Days >= 12)): # Change Here to Filter Buy
        if((result.profit == '') or (result.profit <= -100)):
           result.buyRmd = 'Buy'
           if(result.marketPrice1 < result.low3Days):
               result.buyRmd = 'Buy-Now'

    return result
        
def buildSuggestion(result):

    if(result.profitExp >= 100):
        if(result.profit == ''):
            result.buyRmd = 'BuyShort'
        elif(result.profit <= -100):
            result.buyRmd = 'BuyShort'
            result.status = 'MoreLoss'
        elif(result.profit <= 0):
            result.buyRmd = 'BuyShort'
            result.status = 'NormalLoss'
        elif(result.profit <= 100):
            result.buyRmd = 'BuyShort'
            result.status = 'NormalProfit'
        elif(result.profit > 100):
            result.buyRmd = 'BuyShort'
            result.status = 'MoreProfit'
    
    if(result.lowIn15Days >= 10):
        if(result.profit == ''):
            result.buyRmd = 'Buy'
        elif(result.profit <= -100):
            result.buyRmd = 'Buy'
            result.status = 'MoreLoss'
        elif(result.profit <= 0):
            result.buyRmd = 'Buy'
            result.status = 'NormalLoss'
        elif(result.profit <= 100):
            result.buyRmd = 'Buy'
            result.status = 'NormalProfit'
        elif(result.profit > 100):
            result.buyRmd = 'Buy'
            result.status = 'MoreProfit'

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

def getBundleQty(marketPrice):
    bundleQty = 5000/marketPrice
    bundleQty = round(bundleQty)
    print("BundleQty: {}".format(bundleQty))
    return bundleQty
