# main_script.py
import time
import tkinter as tk
import os
import shutil
import subprocess
import self 
import requests 

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toolbox Application")
        self.geometry("600x400")

        self.crypto_lookup_done = False

        self.create_widgets()

    def create_widgets(self):
        # Create a label for the main menu
        label = tk.Label(self, text="Select a tool:")
        label.pack(pady=10)

        # Create buttons for each tool
        tools = [
            ("Organize Files by Extension", self.organize_files_tool),
            ("Calculator", self.calculator_tool),
            ("Cryptocurrencies Lookup", self.crypto_lookup_tool),
            ("Calculate Average", self.calculate_average_tool),
            ("Create a QR Code", self.qr_code_tool),
            ("Get Weather", self.weather_tool),
            ("Calculate Wage after tax and NIC", self.calculate_wage_tool),
            ("Quiz", self.quiz_tool),
            ("Unit Converter", self.unit_converter_tool),
            ("Currency Converter", self.currency_converter_tool),
            ("English to Spanish Translator", self.translator_tool),
            ("Rename Files in Folders", self.rename_files_tool),
            ("Find Prime Numbers in a Range", self.prime_numbers_tool),
            ("Exit", self.exit_tool),
        ]

        for text, command in tools:
            btn = tk.Button(self, text=text, command=command)
            btn.pack()

    def organize_files_tool(self):
        source_folder_entry = tk.Entry(self)
        destination_folder_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: self.organize_files(
            source_folder_entry.get(), destination_folder_entry.get()))

        source_folder_entry.grid(row=0, column=0, columnspan=2)
        destination_folder_entry.grid(row=1, column=0, columnspan=2)
        submit_button.grid(row=2, column=0, columnspan=2)

    def organize_files(self, source_folder, destination_folder):
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)

                if os.path.isfile(file_path):
                    _, file_extension = os.path.splitext(file)
                    destination_folder_path = os.path.join(destination_folder, file_extension[1:])

                    if not os.path.exists(destination_folder_path):
                        os.makedirs(destination_folder_path)

                    new_file_path = os.path.join(destination_folder_path, file)
                    shutil.move(file_path, new_file_path)

    def calculator_tool(self):
        calculation_entry = tk.Entry(self)
        result_label = tk.Label(self, text="")
        submit_button = tk.Button(self, text="Submit", command=lambda: self.perform_calculation(calculation_entry.get(), result_label))

        calculation_entry.pack()
        submit_button.pack()
        result_label.pack()

    def perform_calculation(self, user_input, result_label):
        try:
            number1, operation, number2 = map(str.strip, user_input.split())
            number1, number2 = float(number1), float(number2)

            if operation == '+':
                result = number1 + number2
            elif operation == '-':
                result = number1 - number2
            elif operation == '*':
                result = number1 * number2
            elif operation == '/':
                if number2 == 0:
                    result_label.config(text="Error: Division by zero")
                    return
                result = number1 / number2
            else:
                result_label.config(text="Error: Invalid operation")
                return

            result_label.config(text=f"Result: {result}")
        except ValueError as ve:
            result_label.config(text=f"Error: {ve}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    def calculator_tool(self):
        calculation_entry = tk.Entry(self)
        result_label = tk.Label(self, text="")
        submit_button = tk.Button(self, text="Submit", command=lambda: self.perform_calculation(calculation_entry.get(), result_label))

    # Pack the GUI elements into a grid
        submit_button.pack()(row=0, column=0, columnspan=2)
        result_label.pack()(row=1, column=0, columnspan=2)
        calculation_entry.pack()(row=2, column=0, columnspan=2)

    def crypto_lookup_tool(self):
        # Add a text box for the user to enter the cryptocurrency symbol
        symbol_entry = tk.Entry(self)
        result_label = tk.Label(self, text="")  # Add a label to display the result
        submit_button = tk.Button(self, text="Submit", command=lambda: self.perform_crypto_lookup(symbol_entry.get(), result_label))

        # Pack the GUI elements into a grid
        symbol_entry.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)
        result_label.grid(row=2, column=0, columnspan=2)

    def perform_crypto_lookup(self, symbol, result_label):
        result = lookup_crypto_price(symbol)  # Call the lookup_crypto_price function
        result_label.config(text=result)  # Update the result label with the fetched result



    def calculate_average_tool(self):
        # Add a text box for the user to enter the numbers
        numbers_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: calculate_average([float(x) for x in numbers_entry.get().split()]))

        # Pack the GUI elements into a grid
        numbers_entry.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)

    def qr_code_tool(self):
        # Add a text box for the user to enter the website URL
        website_url_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: generate_qr_code(website_url_entry.get(), "qr_code.png"))

        # Pack the GUI elements into a grid
        website_url_entry.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)

    def weather_tool(self):
        # Add a text box for the user to enter the city
        city_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: get_weather(city_entry.get()))

        # Pack the GUI elements into a grid
        city_entry.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)

    def calculate_wage_tool(self):
        # Add a text box for the user to enter the annual income
        income_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: calculate_net_income(float(income_entry.get())))

        # Pack the GUI elements into a grid
        income_entry.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)

    def quiz_tool(self):
        # Add a slider for the user to select the number of questions
        num_questions_slider = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL)
        submit_button = tk.Button(self, text="Submit", command=lambda: Quiz(quiz_questions).run_quiz(num_questions_slider.get()))

        # Pack the GUI elements into a grid
        num_questions_slider.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)

    def unit_converter_tool(self):
        # Add a button for each unit conversion function
        length_entry = tk.Entry(self)
        weight_entry = tk.Entry(self)
        temperature_entry = tk.Entry(self)

        length_button = tk.Button(self, text="Length", command=lambda: length_converter(length_entry.get()))
        weight_button = tk.Button(self, text="Weight", command=lambda: weight_converter(weight_entry.get()))
        temperature_button = tk.Button(self, text="Temperature", command=lambda: temperature_converter(temperature_entry.get()))

        # Pack the GUI elements into a grid
        length_entry.grid(row=0, column=0)
        weight_entry.grid(row=0, column=1)
        temperature_entry.grid(row=0, column=2)

        length_button.grid(row=1, column=0)
        weight_button.grid(row=1, column=1)
        temperature_button.grid(row=1, column=2)

    def currency_converter_tool(self):
        # Add entry boxes for currency conversion
        usd_from_entry = tk.Entry(self)
        usd_to_entry = tk.Entry(self)
        gbp_from_entry = tk.Entry(self)
        gbp_to_entry = tk.Entry(self)
        euro_from_entry = tk.Entry(self)
        euro_to_entry = tk.Entry(self)

        usd_to_other_currencies_button = tk.Button(self, text="USD to Other Currencies", command=lambda: usd_to_other_currencies(usd_from_entry.get(), "USD", usd_to_entry.get()))
        gbp_to_other_currencies_button = tk.Button(self, text="GBP to Other Currencies", command=lambda: gbp_to_other_currencies(gbp_from_entry.get(), "GBP", gbp_to_entry.get()))
        euro_to_other_currencies_button = tk.Button(self, text="EUR to Other Currencies", command=lambda: currency_converter_euro(euro_from_entry.get(), "EUR", euro_to_entry.get()))

        # Pack the GUI elements into a grid
        usd_from_entry.grid(row=0, column=0)
        usd_to_entry.grid(row=0, column=1)
        gbp_from_entry.grid(row=1, column=0)
        gbp_to_entry.grid(row=1, column=1)
        euro_from_entry.grid(row=2, column=0)
        euro_to_entry.grid(row=2, column=1)

        usd_to_other_currencies_button.grid(row=0, column=2)
        gbp_to_other_currencies_button.grid(row=1, column=2)
        euro_to_other_currencies_button.grid(row=2, column=2)

    def translator_tool(self):
        # Add a text box for the user to enter the English text
        english_text_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: translate_text(english_text_entry.get(), self.english_to_spanish_translator))

        # Pack the GUI elements into a grid
        english_text_entry.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)

    def rename_files_tool(self):
        # Add a text box for the user to enter the folder path
        folder_path_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: rename_files_in_folders(folder_path_entry.get()))

        # Pack the GUI elements into a grid
        folder_path_entry.grid(row=0, column=0, columnspan=2)
        submit_button.grid(row=1, column=0, columnspan=2)

    def prime_numbers_tool(self):
        # Add text boxes for the user to enter the range of prime numbers
        start_entry = tk.Entry(self)
        end_entry = tk.Entry(self)
        submit_button = tk.Button(self, text="Submit", command=lambda: count_primes_between(int(start_entry.get()), int(end_entry.get())))

        # Pack the GUI elements into a grid
        start_entry.grid(row=0, column=0)
        end_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=0, columnspan=2)

    def exit_tool(self):
        self.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()