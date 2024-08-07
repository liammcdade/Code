
    

def perform_calculation():
        try:
            number1 = float(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            number2 = float(input("Enter the second number: "))

            if operation == '+':
                result = number1 + number2
            elif operation == '-':
                result = number1 - number2
            elif operation == '*':
                result = number1 * number2
            elif operation == '/':
                if number2 == 0:
                    return "Error: Division by zero"
                result = number1 / number2
            else:
                return "Error: Invalid operation"

            return str(result)
        except ValueError as ve:
            return f"Error: {ve}"
        except Exception as e:
            return f"Error: {e}"
def calculate_average(numbers):
        if not numbers:
            return None  # Return None for an empty list

        total = sum(numbers)
        average = total / len(numbers)
        return average