SELECT * FROM TRADE_BOOK WHERE 
STOCK_NAME = 
(Select stock_name from Stocks where stock_symbol = 'HINDPETRO')
ORDER BY TRADE_DATE DESC
;

SELECT * FROM EQUITY_HISTORY
where Symbol = 'ICICIGI'
Order by Date desc
;

select * from RESULTS
where (sellprofit < -200 or Ur_profit < -1000)
;

select strftime("%m-%Y", trade_date) as Month, count(*) as Profit from trade_book
where tradetype = 'B' and status == 'Open'
group by strftime("%Y-%m", trade_date)
;

select strftime("%m-%Y", trade_date) as Month, count(*) as Profit from trade_book
where tradetype = 'B'
group by strftime("%Y-%m", trade_date)
;





PRAGMA foreign_keys;

SELECT * FROM TRADE_BOOK WHERE STOCK_NAME = 'ADANI ENTERPRISES LTD' and TRADE_DATE > '24-Sep-2020';

UPDATE TRADE_BOOK set Status = 'Closed' WHERE STOCK_NAME = 'ADANI ENTERPRISES LTD' and TRADE_DATE = '28-Sep-2020';

SELECT TRADE_DATE FROM TRADE_BOOK WHERE TradeType = 'S' and STOCK_NAME = 'ASIAN PAINTS LIMITED';

SELECT * FROM TRADE_BOOK WHERE TradeType = 'S' and STOCK_NAME = 'ASIAN PAINTS LIMITED' and TRADE_DATE > strftime('%d-%m-%y','28-09-2020');
Select stock_name from Stocks where stock_symbol = 'PERSISTENT';
