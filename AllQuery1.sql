select count(*) from Equity_history
--where date(datetime(date / 1000 , 'unixepoch')) = date('now')--2020-12-21 00:00:00'
where date = '2020-12-22 00:00:00'
;

SELECT * FROM TRADE_BOOK WHERE stockName = 'ASIAN PAINTS LIMITED' ORDER BY TradeDate DeSC;

SELECT * FROM TRADE_BOOK WHERE
(Select stock_name from Stocks where stock_symbol = 'JBCHEPHARM') --and status = 'Open')
ORDER BY TRADE_DATE DESC
;


SELECT * FROM TRADE_BOOK WHERE StockName = 'TATA CONSULTANCY SERVICES LIMITED' and TradeId = '113'

SELECT * FROM TRADE_BOOK Where tradeType = 'S';

select lowprice from (select cast(replace(lowprice,',','') as DOUBLE) as lowprice from equity_history where symbol = 'DIVISLAB' order by date desc limit 15) where lowprice > 3644;

select replace(lowprice,',','') as a from equity_history where symbol = 'DIVISLAB' order by date desc limit 15;

select lasttradedprice from equity_history where symbol = 'ADANIENT' order by date desc limit 26;


select count(*) from (
select * from Equity_history where symbol = 'ADANIENT' order by date desc limit 15
) where highprice < 462.35


select highPrice from (
select * from Equity_history where symbol = 'ADANIENT' order by date desc limit 3
) order by highPrice desc limit 1;





SELECT strftime(date('%Y-%m-%d')) from equity_history;

SELECT * FROM TRADE_BOOK WHERE STOCK_NAME = 'J B CHEMICALS AND PHARMA' ;



insert into trade_book values ('ICICI LOMBARD GENERAL INSURANCE CO LTD','B',7,1001.75,7012,-7061,'Open',0,0,195,0)

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

/*Defects
LUPIN 2 Buy 1 Sell Matched
*/

PRAGMA foreign_keys;

SELECT * FROM TRADE_BOOK WHERE STOCK_NAME = 'HDFC LIFE INSURANCE COMPANY LIMITED';
-- and TRADE_DATE > '24-Sep-2020';

UPDATE TRADE_BOOK set Status = 'Closed' WHERE STOCK_NAME = 'ADANI ENTERPRISES LTD' and TRADE_DATE = '28-Sep-2020';

SELECT TRADE_DATE FROM TRADE_BOOK WHERE TradeType = 'S' and STOCK_NAME = 'ASIAN PAINTS LIMITED';

SELECT * FROM TRADE_BOOK WHERE TradeType = 'S' and STOCK_NAME = 'ASIAN PAINTS LIMITED' and TRADE_DATE > strftime('%d-%m-%y','28-09-2020');
Select stock_name from Stocks where stock_symbol = 'PERSISTENT';
