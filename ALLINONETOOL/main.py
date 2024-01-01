# main_script.py
from calculator import calculate_average, perform_calculation
from fileorganizer import organize_files
from crypto_lookup import lookup_crypto_price
from portfolio import load_portfolio, save_portfolio
from qrcodegenerator import generate_qr_code
from weather import get_weather
from wagecalculator import calculate_net_income
from quiz import Quiz, quiz_questions
from unitconverter import length_converter, weight_converter, temperature_converter
from currencyconverter import usd_to_other_currencies, currency_converter, gbp_to_other_currencies, currency_converter_euro
from englishtospanish import create_translator_spanish, translate_text

def calculate_wage():
    """Calculate net income after tax and NIC."""
    try:
        annual_income = float(input("Enter annual income: £"))
    except ValueError:
        print("Invalid input. Please enter a valid annual income.")
        return

    net_income = calculate_net_income(annual_income)
    print(f"Net income after tax and NIC: £{net_income:.2f}")

def main():
    # Create a translator for English to Spanish
    english_to_spanish_translator = create_translator_spanish()

    while True:
        # Display the main menu
        print("\nSelect a tool:")
        print("1. Organize Files by Extension")
        print("2. Calculator")
        print("3. Cryptocurrencies Lookup")
        print("4. Portfolio Tracker")
        print("5. Calculate Average")
        print("6. Create a QR Code")
        print("7. Get Weather")
        print("8. Calculate Wage after tax and NIC")
        print("9. Quiz")
        print("10. Unit Converter")
        print("11. Currency Converter")
        print("12. English to Spanish Translator")
        print("13. Exit")

        # Get user input for the selected tool
        choice = input("Enter your choice (1-13): ")

        # Perform actions based on the user's choice
        if choice == "1":
            # Tool 1: Organize Files by Extension
            source_folder = input("Enter the source folder path: ")
            destination_folder = input("Enter the destination folder path: ")
            organize_files(source_folder, destination_folder)
            print("Files organized successfully.")
        elif choice == "2":
            # Tool 2: Calculator
            result = perform_calculation()
            print(f"Result: {result}")
        elif choice == "3":
            # Tool 3: Cryptocurrencies Lookup
            while True:
                symbol = input("Enter the cryptocurrency symbol (e.g., BTC-USD): ").upper()

                if symbol == "EXIT":
                    print("Exiting cryptocurrency lookup.")
                    break

                print(lookup_crypto_price(symbol))
        elif choice == "4":
            # Tool 4: Portfolio Tracker
            portfolio = load_portfolio()
            # Call functions related to portfolio management here
            save_portfolio(portfolio)
            print("Returning to the main menu.")
        elif choice == "5":
            # Tool 5: Calculate Average
            # Example usage for calculating the average
            numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]
            result = calculate_average(numbers)

            if result is not None:
                print(f"The average is: {result}")
            else:
                print("Please enter at least one number.")
        elif choice == "6":
            # Tool 6: Create a QR Code
            website_url = input("Enter the website URL for the QR code (full address only): ")
            qr_code_file_path = "qr_code.png"
            generate_qr_code(website_url, qr_code_file_path)
            print(f"QR code generated and saved to {qr_code_file_path}")
        elif choice == "7":
            # Tool 7: Get Weather
            city = input("Enter the city for weather information: ")
            get_weather(city)
        elif choice == "8":
            # Tool 8: Calculate Wage
            calculate_wage()
        elif choice == "9":
            num_questions = int(input("How many questions would you like to answer (1 - 100)?"))
            my_quiz = Quiz(quiz_questions)
            my_quiz.run_quiz(num_questions)
        elif choice == "10":
            # Tool 10: Unit Converter
            while True:
                print("\nSelect a category:")
                print("1. Length Converter")
                print("2. Weight Converter")
                print("3. Temperature Converter")
                print("EXIT. Back to the main menu")

                unit_converter_choice = input("Enter your choice (1-4): ")

                if unit_converter_choice == "1":
                    length_converter()
                elif unit_converter_choice == "2":
                    weight_converter()
                elif unit_converter_choice == "3":
                    temperature_converter()
                elif unit_converter_choice == "4":
                    print("Returning to the main menu.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        elif choice == "11":
            # Tool 11: Currency Converter
            print("\nSelect a currency conversion option:")
            print("1. USD to Other Currencies")
            print("2. GBP to Other Currencies")
            print("3. Euro to other currencies")
            print("4. exit. Back to the main menu")

            currency_choice = input("Enter your choice (1-4): ")

            if currency_choice == "1":
                usd_to_other_currencies()
            elif currency_choice == "2":
                gbp_to_other_currencies()
            elif currency_choice == "3":
                currency_converter_euro()

            elif currency_choice == "4":
                print("Returning to the main menu.")
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        elif choice == "12":
            # Tool 12: English to Spanish Translator
            user_input = input("Enter English text to translate to Spanish (or 'exit' to quit): ")

            if user_input.lower() == 'exit':
                print("Exiting the translator.")
                break

            translated_text = translate_text(user_input, english_to_spanish_translator)
            print("Translated text:", translated_text)
        elif choice == "13":
            # Tool 13: Exit
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 13.")

if __name__ == "__main__":
    main()
