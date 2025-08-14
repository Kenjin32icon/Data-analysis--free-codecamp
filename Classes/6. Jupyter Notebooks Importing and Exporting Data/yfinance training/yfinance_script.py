# import yfinance as yf
import yfinance as yf
    # This code imports the yfinance library, which is used to download financial data from Yahoo Finance.  
# # Example usage:  

# # Download historical data for Apple Inc.
# apple_data = yf.download('AAPL', start='2020-01-01', end='2021-01-01')      
# # Display the first few rows of the data
# print(apple_data.head())    

# Define the ticker symbol
ticker_symbol = 'AAPL'  # Apple Inc.

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data
historical_data = ticker.history(period='1y')  # Last 1 year of data    
# Display the first few rows of the historical data
print(historical_data.head()) # This code fetches the last year of historical market data for Apple Inc. and prints the first few rows of the data. 

# Fetch basic financials
financials = ticker.financials
print(financials.head()) # This code fetches the basic financials of Apple Inc. and prints the first few rows of the financial data.

# Fetch company info
company_info = ticker.info
print(company_info)  # This code fetches the company information for Apple Inc. and prints the information.
# Fetch dividends
dividends = ticker.dividends
print(dividends.head())  # This code fetches the dividend data for Apple Inc.
# and prints the first few rows of the dividend data.

