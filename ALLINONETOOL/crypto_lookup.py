# crypto_lookup.py
import yfinance as yf

def lookup_crypto_price(symbol):
    try:
        crypto_data = yf.download(symbol)
        last_price = crypto_data['Close'].iloc[-1]
        return f"Last price for {symbol}: {last_price}"
    except Exception as e:
        return f"Error: {e}"
