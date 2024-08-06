# main_script.py

import os
import time
from calculators.calculator import calculate_average, perform_calculation
from files_based.fileorganizer import organize_files
from Crypto.crypto_lookup import lookup_crypto_price
from miscellaneous.portfolio import load_portfolio, save_portfolio
from miscellaneous.qrcodegenerator import generate_qr_code
from miscellaneous.weather import get_weather
from calculators.wagecalculator import calculate_net_income
from miscellaneous.quiz import Quiz, quiz_questions
from calculators.unitconverter import length_converter, weight_converter, temperature_converter
from calculators.currencyconverter import usd_to_other_currencies, currency_converter_euro, gbp_to_other_currencies
from language.englishtospanish import create_translator_spanish, translate_text
from files_based.renamer import rename_files_in_folders
from miscellaneous.primenumbers import count_primes_between, get_numbers
from system.system import get_system_info, system_main
from miscellaneous.deletepycache import removefolders, DEFAULT_BASE_DIRECTORY

def calculate_wage():
    try:
        annual_income = float(input("Enter annual income: £"))
    except ValueError:
        print("Invalid input. Please enter a valid annual income.")
        return
    net_income = calculate_net_income(annual_income)
    print(f"Net income after tax and NIC: £{net_income:.2f}")

def main():
    english_to_spanish_translator = create_translator_spanish()
    crypto_lookup_done = False

    tools = {
        "1": ("Organize Files by Extension", lambda: organize_files(
            input("Enter the source folder path: "), input("Enter the destination folder path: "))),
        "2": ("Calculator", lambda: print(f"Result: {perform_calculation()}")),
        "3": ("Cryptocurrencies Lookup", lambda: lookup_crypto_price(
            input("Enter the cryptocurrency symbol (e.g., bitcoin): ").upper())),
        "4": ("Portfolio Tracker", lambda: save_portfolio(load_portfolio())),
        "5": ("Calculate Average", lambda: print(f"The average is: {calculate_average([float(x) for x in input('Enter numbers separated by space: ').split()])}")),
        "6": ("Create a QR Code", lambda: generate_qr_code(
            input("Enter the website URL for the QR code (full address only): "), "qr_code.png")),
        "7": ("Get Weather", lambda: get_weather(input("Enter the city for weather information: "))),
        "8": ("Calculate Wage after tax and NIC", calculate_wage),
        "9": ("Quiz", lambda: Quiz(quiz_questions).run_quiz(int(input("How many questions would you like to answer (1 - 100)?")))),
        "10": ("Unit Converter", lambda: {
            "1": length_converter,
            "2": weight_converter,
            "3": temperature_converter
        }[input("\nSelect a category:\n1. Length Converter\n2. Weight Converter\n3. Temperature Converter\nEnter your choice (1-3): ")]()),
        "11": ("Currency Converter", lambda: {
            "1": usd_to_other_currencies,
            "2": gbp_to_other_currencies,
            "3": currency_converter_euro
        }[input("\nSelect a currency conversion option:\n1. USD to Other Currencies\n2. GBP to Other Currencies\n3. Euro to other currencies\nEnter your choice (1-3): ")]()),
        "12": ("English to Spanish Translator", lambda: print("Translated text:", translate_text(
            input("Enter English text to translate to Spanish (or 'exit' to quit): "), english_to_spanish_translator))),
        "13": ("Rename Files in Folders", lambda: rename_files_in_folders(input("Enter the root folder path: "))),
        "14": ("Find Prime Numbers in a Range", lambda: print(f"Number of prime numbers between {start_num} and {end_num} is: {count_primes_between(start_num := get_numbers()[0], end_num := get_numbers()[1])}")),
        "15": ("System Information", lambda: [get_system_info(), system_main()]),
        "16": ("Clean up", lambda: removefolders(base_directory=DEFAULT_BASE_DIRECTORY)),
        "17": ("Exit", exit)
    }

    while True:
        print("\nSelect a tool:")
        for key, (name, _) in tools.items():
            print(f"{key}. {name}")
        choice = input("Enter your choice (1-17): ")
        if choice in tools:
            tools[choice][1]()
        else:
            print("Invalid choice. Please enter a number between 1 and 17.")

if __name__ == "__main__":
    main()
