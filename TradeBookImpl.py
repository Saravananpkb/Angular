import TradeBookDao as tradeBookDao

def calculate_Trade_Profit(stockName):
    tradeTable = tradeBookDao.queryTradeBook_BuyOpenByStockAscPrice(stockName)
    noOfOpenBuy = len(tradeTable)
    print("noOfOpenBuy : {}".format(noOfOpenBuy))
    for i in range(noOfOpenBuy):
            tradeTable = tradeBookDao.queryTradeBook_BuyOpenByStockAscPrice(stockName)
            tradeRow = tradeTable[0]
            if(tradeRow[2] == 'B' and tradeRow[7] != 'Closed'):
                    buyTradeId = tradeRow[10]
                    buyTotalPrice = tradeRow[6]
                    tradeRowsSell = tradeBookDao.queryTradeBook_SellOpenByStockDescDate(stockName)
                    print(len(tradeRowsSell))
                    if(len(tradeRowsSell) >= 1 and tradeRowsSell[0][7] != 'Closed'):
                        sellTradeId = tradeRowsSell[0][10]
                        sellPrice = tradeRowsSell[0][4]
                        sellTotalPrice = tradeRowsSell[0][6]
                        profit = round(buyTotalPrice + sellTotalPrice)
                        print("SellPrice {}".format(sellPrice))
                        print("Profit {}".format(profit))
                        tradeBookDao.updateTradeBook_Status(stockName,sellTradeId,'Closed')
                        tradeBookDao.updateTradeBook_Status_Profit(stockName,buyTradeId,'Closed',sellPrice,profit,sellTradeId)
                        print("Buy Sell Status is Marked Closed for : {}".format(stockName))
    pass

def calculate_TradeBook_Profit():
    tradeTable = tradeBookDao.queryTradeBook_BuyOpen()
    for tradeRow in tradeTable:
        if(tradeRow[1] == 'LUPIN LIMITED'):
            if(tradeRow[2] == 'B' and tradeRow[7] != 'Closed'):
                stockName = tradeRow[1]
                buyTradeDate = tradeRow[0]
                #print((buyTradeDate))
                buyTotalPrice = tradeRow[6]
                tradeRowsSell = tradeBookDao.queryTradeBook_SellOpen(stockName,buyTradeDate)
                #print(len(tradeRowsSell))
                if(len(tradeRowsSell) >= 1 and tradeRowsSell[0][7] != 'Closed'):
                    sellTradeDate = tradeRowsSell[0][0]
                    sellPrice = tradeRowsSell[0][4]
                    sellTotalPrice = tradeRowsSell[0][6]
                    profit = round(buyTotalPrice + sellTotalPrice)
                    print("SellPrice {}".format(sellPrice))
                    print("Profit {}".format(profit))
                    tradeBookDao.updateTradeBook_Status(stockName,sellTradeDate,'Closed')
                    tradeBookDao.updateTradeBook_Status_Profit(stockName,buyTradeDate,'Closed',sellPrice,profit)
                    print("Buy Sell Status is Marked Closed for : {}".format(stockName))
    pass