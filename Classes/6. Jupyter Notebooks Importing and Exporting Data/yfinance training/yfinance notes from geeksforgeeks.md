From geeksforgeeks

How to Use yfinance API with Python
Last Updated : 23 Jul, 2025

The yfinance API is a powerful tool for accessing financial data from Yahoo Finance. It allows users to download historical market data, retrieve financial information, and perform various financial analyses. This API is widely used in finance, investment, and trading applications for its ease of use and comprehensive data coverage. In this article, we will explore the use yfinance API in Python with detailed examples.
What is yfinance?

yfinance is a Python library designed for accessing and retrieving financial data from Yahoo Finance. It simplifies the process of fetching historical market data, financial statements, and other relevant information for stocks, indices, and securities. Widely utilized in finance, investment, and trading applications, yfinance offers comprehensive data coverage and ease of integration, making it a popular choice among developers and financial analysts alike.
Setting Up yfinance API

To use yfinance, you need to install it first. This can be done using pip:

pip install yfinance

After installation, you can import the library in your Python script:

import yfinance as yf

Fetching Financial Data

With yfinance, you can fetch historical market data and financial information about stocks, indices, and other securities. The primary method for this is the Ticker object.
Example 1: Fetching Historical Market Data of Apple Inc

In this example, we are using the yfinance library in Python to fetch comprehensive financial data for the ticker symbol "AAPL" (Apple Inc.). We begin by creating a Ticker object for "AAPL" and then use it to retrieve historical market data for the last year (period="1y"). The fetched data includes daily Open, High, Low, Close prices, and Volume. Additionally, we fetch basic financial statements (financials) and stock actions (actions) such as dividends and splits related to Apple's stock.

import yfinance as yf

​

# Define the ticker symbol

ticker_symbol = "AAPL"

​

# Create a Ticker object

ticker = yf.Ticker(ticker_symbol)

​

# Fetch historical market data

historical_data = ticker.history(period="1y")  # data for the last year

print("Historical Data:")

print(historical_data)

​

# Fetch basic financials

financials = ticker.financials

print("\nFinancials:")

print(financials)

​

# Fetch stock actions like dividends and splits

actions = ticker.actions

print("\nStock Actions:")

print(actions)

Output
Screenshot-2024-07-13-224538-min
Example 2: Fetching Historical Market Data of Microsoft

In this example, we use yfinance to fetch historical market data for Microsoft Corporation (MSFT). We create a Ticker object for "MSFT" and fetch data for the last month (period="1mo"). The fetched data includes daily Open, High, Low, Close prices, and Volume. The summary output displays these key data points in a concise format, making it easier to analyze short-term trends for Microsoft's stock.

import yfinance as yf

​

# Define the ticker symbol

ticker_symbol = "MSFT"

​

# Create a Ticker object

ticker = yf.Ticker(ticker_symbol)

​

# Fetch historical market data for the last 30 days

historical_data = ticker.history(period="1mo")  # data for the last month

​

# Display a summary of the fetched data

print(f"Summary of Historical Data for {ticker_symbol}:")

print(historical_data[['Open', 'High', 'Low', 'Close', 'Volume']])

Output
OP2-min
Conclusion

In conclusion, the yfinance API proves invaluable for accessing detailed financial data from Yahoo Finance directly into Python applications. It simplifies the process of fetching historical market data, financial statements, and stock actions for various securities such as stocks and indices. By leveraging yfinance, users can efficiently perform financial analyses and gain insights crucial for finance, investment, and trading decisions.
