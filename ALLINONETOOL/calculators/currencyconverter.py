def currency_converter(amount, exchange_rates, from_currency, to_currency):
    converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

def usd_to_other_currencies():
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'JPY': 110.0,
        'GBP': 0.73,
        'AUD': 1.31,
        'CAD': 1.26,
        'CHF': 0.91,
        'CNY': 6.46,
        'SEK': 8.52,
        'NZD': 1.43,
        'NOK': 9.02,
        'INR': 74.27,
        'BRL': 5.29,
        'RUB': 75.88,
        'ZAR': 15.08,
        'HKD': 7.77,
        'SGD': 1.34,
        'TRY': 13.09,
        'MXN': 21.47,
        'IDR': 14215.00,
        'PLN': 3.97,
        'PHP': 50.19,
        'THB': 32.87,
        'MYR': 4.16,
        'KRW': 1159.50,
        'AED': 3.67,
        'SAR': 3.75,
        'DKK': 6.25,
        'BGN': 1.66,
        'HUF': 304.50,
        'CZK': 22.04,
        'RON': 4.05,
        'ISK': 129.50,
        'HRK': 6.41,
        'CLP': 787.30,
        'COP': 3755.50,
        'ARS': 102.44,
        'IQD': 1457.50,
        'ILS': 3.22,
        'QAR': 3.64,
        'KWD': 0.30,
        'PKR': 289.00,
        'EGP': 15.65,
        'VND': 22661.50,
        'UAH': 27.82,
        'LBP': 15050.00,
        'ZMW': 21.70,
        'BHD': 0.38,
        'DOP': 57.08,
        'GHS': 10.99,
    }

    print("USD to Other Currencies Converter")
    print("Available Currencies:")
    print(", ".join(exchange_rates.keys()))

    to_currency = input("Enter the target currency code: ").upper()

    if to_currency not in exchange_rates:
        print("Invalid currency code. Please enter a valid code.")
        return

    amount_usd = float(input("Enter the amount in USD: "))
    currency_converter(amount_usd, exchange_rates, 'USD', to_currency)

def gbp_to_other_currencies():
    exchange_rates = {
        'USD': 1.41,   # Example exchange rates (GBP to other currencies)
        'EUR': 1.17,
        'JPY': 153.21,
        'GBP': 1.0,
        'AUD': 1.79,
        'CAD': 1.73,
        'CHF': 1.29,
        'CNY': 8.83,
        'SEK': 12.14,
        'NZD': 1.93,
        'NOK': 11.21,
        'INR': 103.71,
        'BRL': 7.14,
        'RUB': 105.11,
        'ZAR': 19.47,
        'HKD': 10.97,
        'SGD': 1.87,
        'TRY': 13.13,
        'MXN': 28.17,
        'IDR': 19944.10,
        'PLN': 5.70,
        'PHP': 73.52,
        'THB': 42.45,
        'MYR': 5.80,
        'KRW': 1579.42,
        'AED': 5.17,
        'SAR': 5.28,
        'DKK': 10.50,
        'BGN': 2.29,
        'HUF': 428.10,
        'CZK': 31.49,
        'RON': 5.79,
        'ISK': 153.73,
        'HRK': 8.98,
        'CLP': 1108.42,
        'COP': 5241.88,
        'ARS': 127.36,
        'IQD': 2085.71,
        'ILS': 4.61,
        'QAR': 5.12,
        'KWD': 0.38,
        'PKR': 229.97,
        'EGP': 26.34,
        'VND': 32157.50,
        'UAH': 45.41,
        'LBP': 2132.94,
        'ZMW': 26.06,
        'BHD': 0.53,
        'DOP': 91.80,
        'GHS': 10.13
    }
    
    print("GBP to Other Currencies Converter")
    print("Available Currencies:")
    print(", ".join(exchange_rates.keys()))

    to_currency = input("Enter the target currency code: ").upper()

    if to_currency not in exchange_rates:
        print("Invalid currency code. Please enter a valid code.")
        return

    amount_gbp = float(input(f"Enter the amount in GBP: "))
    currency_converter(amount_gbp, exchange_rates, 'GBP', to_currency)

def currency_converter_euro():
    exchange_rates = {
        'USD': 1.22,
        'JPY': 128.46,
        'EUR': 1.0,
        'GBP': 0.84,
        'AUD': 1.55,
        'CAD': 1.49,
        'CHF': 1.09,
        'CNY': 7.73,
        'SEK': 10.14,
        'NZD': 1.69,
        'NOK': 10.41,
        'INR': 87.76,
        'BRL': 6.63,
        'RUB': 96.65,
        'ZAR': 18.62,
        'HKD': 9.53,
        'SGD': 1.58,
        'TRY': 12.61,
        'MXN': 24.31,
        'IDR': 17044.60,
        'PLN': 4.56,
        'PHP': 63.14,
        'THB': 37.80,
        'MYR': 4.92,
        'KRW': 1384.63,
        'AED': 4.49,
        'SAR': 4.56,
        'DKK': 7.44,
        'BGN': 1.67,
        'HUF': 369.48,
        'CZK': 26.14,
        'RON': 4.95,
        'ISK': 156.07,
        'HRK': 7.51,
        'CLP': 877.56,
        'COP': 4543.02,
        'ARS': 117.64,
        'IQD': 1766.95,
        'ILS': 4.09,
        'QAR': 4.47,
        'KWD': 0.37,
        'PKR': 229.05,
        'EGP': 23.72,
        'VND': 27256.58,
        'UAH': 32.73,
        'LBP': 1884.00,
        'ZMW': 28.98,
        'BHD': 0.45,
        'DOP': 68.66,
        'GHS': 9.14
    }

    print("Euro to Other Currencies Converter")
    print("Available Currencies:")
    print(", ".join(exchange_rates.keys()))

    to_currency = input("Enter the target currency code: ").upper()

    if to_currency not in exchange_rates:
        print("Invalid currency code. Please enter a valid code.")
        return

    amount_euro = float(input(f"Enter the amount in Euro: "))
    currency_converter(amount_euro, exchange_rates, 'EUR', to_currency)


def main():
    print("Welcome to the Crypto Currency Converter Tool!")

    while True:
        print("\nSelect a category:")
        print("1. USD to Other Currencies")
        print("2. GBP to Other Currencies")
        print("3. Euro to Other Currencies")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            usd_to_other_currencies()
        elif choice == "2":
            gbp_to_other_currencies()
        elif choice == "3":
            currency_converter_euro()
        
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


    
