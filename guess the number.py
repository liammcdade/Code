import random

def number_guess_game():
    secret_number = random.randint(1, 100)
    tries = 0
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        tries += 1
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {tries} tries.")
            break

if __name__ == "__main__":
    number_guess_game()