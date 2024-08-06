import requests

def get_weather(city):
    try:
        # Construct the URL for wttr.in
        url = f'https://wttr.in/{city}?format=%t+%C+%w'

        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the weather information
            print(f"Weather in {city}: {response.text.strip()}")
        else:
            print(f"Failed to retrieve weather information. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get user input for the city
    city = input("Enter the city: ")

    # Call the function to get weather information
    get_weather(city)
