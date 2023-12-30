# main_script.py
from calculator import calculate_average, perform_calculation
from fileorganizer import organize_files
from crypto_lookup import lookup_crypto_price
from portfolio import load_portfolio, save_portfolio
from qrcodegenerator import generate_qr_code

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
        print("7. Exit")

        # Get user input for the selected tool
        choice = input("Enter your choice (1-7): ")

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
            # Tool 7: Exit
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
