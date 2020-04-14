# Equity-Portfolio-analysis
This repository is a coded version of Equity Portfolio analysis by Zerodha Varsity. The user can make his or her own stock portfolio by specifying the stock ticker name and its weight in percentage. The program will create a portfolio and find its variance(measure of risk). Additionally, it will parse the historical data over last 2 years and find the performance(returns) of your portfolio. The repository also has an excel file of the same analysis in excel.

The output of the code will be your expected portfolio return, annual portfolio standard deviation(risk) and the live Net asset value(NAV) of your portfolio. You will also be able to see a line chart of your NAV indicating its past performance.

For the theory part of the analysis, you can refer <a href="https://zerodha.com/varsity/module/risk-management/">module 9</a> on Zerodha Varsity.

Example:

[Expected_portfolio_return, Annual_portfolio_stdev, NAV_live] = stock_portfolio(portfolio,start_date,end_date)
