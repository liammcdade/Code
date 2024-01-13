from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import os
import shutil
import requests

class ToolScreen(Screen):
    def __init__(self, tool_name, **kwargs):
        super(ToolScreen, self).__init__(**kwargs)
        self.tool_name = tool_name
        self.source_folder_entry = None
        self.destination_folder_entry = None
        self.calculation_entry = None
        self.symbol_entry = None
        self.result_label = None
        self.back_button = Button(text="Back", on_press=self.go_back)
        
        # Create a vertical box layout to hold the widgets
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

    def on_enter(self):
        self.layout.clear_widgets()
        if  self.tool_name == "Organize Files by Extension":
            self.layout.add_widget(Label(text="Source Folder:"))
            self.source_folder_entry = TextInput()
            self.layout.add_widget(self.source_folder_entry)

            self.layout.add_widget(Label(text="Destination Folder:"))
            self.destination_folder_entry = TextInput()
            self.layout.add_widget(self.destination_folder_entry)

            self.result_label = Label(text="")
            self.layout.add_widget(self.result_label)

            submit_button = Button(text="Submit", on_press=self.organize_files)
            self.layout.add_widget(submit_button)

            self.layout.add_widget(self.back_button)

        elif self.tool_name == "Calculator":
            self.calculation_entry = TextInput()
            self.layout.add_widget(self.calculation_entry)

            self.result_label = Label(text="")
            self.layout.add_widget(self.result_label)

            submit_button = Button(text="Submit", on_press=self.perform_calculation)
            self.layout.add_widget(submit_button)

            self.layout.add_widget(self.back_button)

        elif self.tool_name == "Cryptocurrencies Lookup":
            self.symbol_entry = TextInput()
            self.layout.add_widget(self.symbol_entry)

            self.result_label = Label(text="")
            self.layout.add_widget(self.result_label)

            submit_button = Button(text="Submit", on_press=self.perform_crypto_lookup)
            self.layout.add_widget(submit_button)
            self.layout.add_widget(self.back_button)

    def on_leave(self):
        self.layout.clear_widgets()

    def go_back(self, instance):
        self.manager.current = "main_menu"

    def organize_files(self, instance):
        source_folder = self.source_folder_entry.text
        destination_folder = self.destination_folder_entry.text

        if not source_folder or not destination_folder:
            self.result_label.text = "Please provide both source and destination folders."
            return

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

        self.result_label.text = "Files organized successfully."

    def perform_calculation(self, instance):
        try:
            user_input = self.calculation_entry.text
            result = eval(user_input)  # Use eval to evaluate the expression
            self.result_label.text = f"Result: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"


    def perform_crypto_lookup(self, instance):
        symbol = self.symbol_entry.text
        result = self.lookup_crypto_price(symbol)
        self.result_label.text = result


    def lookup_crypto_price(self, symbol):
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
class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        main_menu = Screen(name="main_menu")
        main_menu.add_widget(self.create_main_menu_widgets())
        self.screen_manager.add_widget(main_menu)

        tools = [
            ("Organize Files by Extension", ToolScreen(tool_name="Organize Files by Extension", name="organize_files")),
            ("Calculator", ToolScreen(tool_name="Calculator", name="calculator")),
            ("Cryptocurrencies Lookup", ToolScreen(tool_name="Cryptocurrencies Lookup", name="crypto_lookup")),
        ]

        for text, tool_screen in tools:
            self.screen_manager.add_widget(tool_screen)

        return self.screen_manager

    def create_main_menu_widgets(self):
        main_menu_layout = BoxLayout(orientation="vertical")
        label = Label(text="Select a tool:")
        main_menu_layout.add_widget(label)

        tools = [
            ("Organize Files by Extension", "organize_files"),
            ("Calculator", "calculator"),
            ("Cryptocurrencies Lookup", "crypto_lookup"),
        ]

        for text, tool_name in tools:
            btn = Button(text=text, on_press=lambda instance, tn=tool_name: self.show_tool(tn))
            main_menu_layout.add_widget(btn)

        return main_menu_layout

    def show_tool(self, tool_name):
        self.screen_manager.current = tool_name


if __name__ == "__main__":
    MainApp().run()
