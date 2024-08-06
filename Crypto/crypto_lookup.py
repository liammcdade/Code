import requests

def lookup_crypto_price(symbol):
    try:
        # Define the CoinGecko API endpoint
        api_endpoint = "https://api.coingecko.com/api/v3/simple/price"

        # Specify the parameters for the API request
        params = {
            'ids': symbol.lower(),
            'vs_currencies': 'usd',
        }

        # Make the API request
        response = requests.get(api_endpoint, params=params)
        data = response.json()

        # Extract the last price from the response
        last_price = data.get(symbol.lower(), {}).get('usd')

        if last_price is not None:
            return f"Last price for {symbol}: {last_price} USD"
        else:
            return f"Unable to fetch price for {symbol}"

    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    crypto_symbol = "bitcoin"
    result = lookup_crypto_price(crypto_symbol)
    print(result)

