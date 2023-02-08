import os
import requests

def get_stock_price(symbol):
    api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        stock_data = response.json()
        return float(stock_data['Global Quote']['05. price'])
    else:
        return None

symbol = input("Enter the symbol of the stock: ")
result = get_stock_price(symbol)

if result:
    print(f"The current stock price of {symbol} is ${result:.2f}")
else:
    print("Could not retrieve stock price data.")