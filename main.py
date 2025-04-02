# main_script.py

from calculators.calculator import perform_calculation, calculate_average 
from files_based.fileorganizer import organize_files
from Crypto.crypto_lookup import lookup_crypto_price
from miscellaneous.portfolio import load_portfolio, save_portfolio
from miscellaneous.qrcodegenerator import generate_qr_code
from miscellaneous.weather import get_weather
from calculators.wagecalculator import calculate_net_income
from miscellaneous.quiz import Quiz, quiz_questions
from calculators.unitconverter import length_converter, weight_converter, temperature_converter
from calculators.currencyconverter import usd_to_other_currencies, currency_converter, gbp_to_other_currencies, currency_converter_euro
from language.englishtospanish import create_translator_spanish, translate_text
from files_based.renamer import rename_files_in_folders
from miscellaneous.primenumbers import count_primes_between, get_numbers  # Corrected import names
from system.system import get_system_info, system_main
from miscellaneous.deletepycache import removefolders, main, DEFAULT_BASE_DIRECTORY


def calculate_wage():
    try:
        annual_income = float(input("Enter annual income: £"))
        print(f"Net income after tax: £{calculate_net_income(annual_income):.2f}")
    except ValueError:
        print("Invalid input.")

def main():
    english_to_spanish_translator = create_translator_spanish()
    crypto_lookup_done = False

    while True:
        print("\nSelect a tool:")
        menu = [
            "1. Organize Files", "2. Calculator", "3. Crypto Lookup", "4. Portfolio Tracker", 
            "5. Calculate Average", "6. Generate QR Code", "7. Get Weather", "8. Calculate Wage", 
            "9. Quiz", "10. Unit Converter", "11. Currency Converter", "12. Translate to Spanish", 
            "13. Rename Files", "14. Find Prime Numbers", "15. System Info", "16. Install Programs", "17. Exit"
        ]
        for item in menu: print(item)

        choice = input("Enter choice (1-17): ")
        if choice == "1": organize_files(input("Source: "), input("Destination: "))
        elif choice == "2": perform_calculation()
        elif choice == "3" and not crypto_lookup_done: print(lookup_crypto_price(input("Enter crypto symbol: ").upper()))
        elif choice == "4": save_portfolio(load_portfolio())
        elif choice == "5": print(f"The average is: {calculate_average([float(x) for x in input('Enter numbers: ').split()])}")
        elif choice == "6": generate_qr_code(input("Website URL: "), "qr_code.png")
        elif choice == "7": get_weather(input("City: "))
        elif choice == "8": calculate_wage()
        elif choice == "9": Quiz(quiz_questions).run_quiz(int(input("How many questions? ")))
        elif choice == "10":
            while (unit_choice := input("1. Length, 2. Weight, 3. Temperature, 4. Back: ")) in ["1", "2", "3"]:
                { "1": length_converter, "2": weight_converter, "3": temperature_converter}[unit_choice]()
        elif choice == "11":
            currency_choice = input("1. USD, 2. GBP, 3. Euro, 4. Back: ")
            { "1": usd_to_other_currencies, "2": gbp_to_other_currencies, "3": currency_converter_euro }[currency_choice]() if currency_choice in ["1", "2", "3"] else print("Back to menu.")
        elif choice == "12": print("Translated text:", translate_text(input("Text to translate: "), english_to_spanish_translator))
        elif choice == "13": rename_files_in_folders(input("Root folder path: "))
        elif choice == "14": print("Prime numbers:", count_primes_between(*get_numbers()))
        elif choice == "15": get_system_info(); system_main()
        elif choice == "16":
            print("Exiting program..."); removefolders(DEFAULT_BASE_DIRECTORY); break
        else: print("Invalid choice. Please enter a number between 1 and 17.")

if __name__ == "__main__":
    main()
