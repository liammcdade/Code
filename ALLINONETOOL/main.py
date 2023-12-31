# main_script.py
from tools.calculations.calculator import calculate_average, perform_calculation
from tools.general.fileorganizer import organize_files
from tools.money.crypto_lookup import lookup_crypto_price
from tools.money.portfolio import load_portfolio, save_portfolio
from tools.general.qrcodegenerator import generate_qr_code
from tools.general.weather import get_weather 
from tools.money.wagecalculator import calculate_income_tax, calculate_nic, calculate_total_deductions, calculate_net_income
from games.quiz import Quiz, quiz_questions


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
        print("8. Calculate Wage")
        print("9. Quiz")
        print("10. Exit")

        # Get user input for the selected tool
        choice = input("Enter your choice (1-10): ")

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
            # Tool 10: Exit
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()
