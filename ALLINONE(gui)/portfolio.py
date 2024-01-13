import yfinance as yf

def get_stock_price(symbol):
    try:
        # Create a Ticker object
        ticker = yf.Ticker(symbol)

        # Get historical market data
        history = ticker.history(period="1d")

        # Extract and return the latest stock price
        latest_price = history['Close'].iloc[-1]
        return latest_price
    except Exception as e:
        print(f"Error: {e}")
        return None

def calculate_portfolio_value(portfolio):
    total_value = 0

    for stock, quantity in portfolio.items():
        price = get_stock_price(stock)
        
        if price is not None:
            stock_value = price * quantity
            print(f"Value of {quantity:,} shares of {stock}: ${stock_value:,.2f}")
            total_value += stock_value
        else:
            print(f"Unable to retrieve price for {stock}")

    print(f"\nTotal Portfolio Value: ${total_value:,.2f}")

if __name__ == "__main__":
    my_portfolio = {
        "AAPL": 1031407553,
        "GOOGL": 353034945,
        "MSFT": 533634606
    }  # Replace with your stock symbols and quantities
    calculate_portfolio_value(my_portfolio)
