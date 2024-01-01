from forex_python.converter import CurrencyRates

def convert_currency():
    c = CurrencyRates()

    print("Currency Converter")
    print("Available Currencies:")
    print(", ".join(c.get_rates("").keys()))

    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    amount = float(input(f"Enter the amount in {from_currency}: "))

    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate

    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    convert_currency()
