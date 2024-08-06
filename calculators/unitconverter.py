def length_converter():
    print("Length Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet} feet")
    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters} meters")
    else:
        print("Invalid choice")


def weight_converter():
    print("Weight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms is equal to {pounds} pounds")
    elif choice == 2:
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kilograms} kilograms")
    else:
        print("Invalid choice")


def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius")
    else:
        print("Invalid choice")


def main():
    print("Welcome to the Unit Converter")
    print("1. Length Converter")
    print("2. Weight Converter")
    print("3. Temperature Converter")

    category_choice = int(input("Enter the category (1/2/3): "))

    if category_choice == 1:
        length_converter()
    elif category_choice == 2:
        weight_converter()
    elif category_choice == 3:
        temperature_converter()
    else:
        print("Invalid category choice")


if __name__ == "__main__":
    main()
