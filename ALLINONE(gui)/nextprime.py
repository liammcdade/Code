def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_next_prime(current_prime):
    """Find the next prime number."""
    next_num = current_prime + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num

if __name__ == "__main__":
    try:
        current_prime = int(input("Enter the current prime number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        next_prime = find_next_prime(current_prime)
        print(f"The next prime number after {current_prime} is: {next_prime}")