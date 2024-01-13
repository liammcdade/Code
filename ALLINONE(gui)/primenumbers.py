import time

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_between(start, end):
    primes_count = sum(1 for num in range(start, end + 1) if is_prime(num))
    return primes_count

def get_numbers():
    while True:
        try:
            start_num = int(input("Enter the starting number: "))
            end_num = int(input("Enter the ending number: "))
            return start_num, end_num
        except ValueError:
            print("Invalid input. Please enter valid integer values.")

def main():
    start_num, end_num = get_numbers()

    start_time = time.time()
    result = count_primes_between(start_num, end_num)
    end_time = time.time()

    print("Number of prime numbers between", start_num, "and", end_num, "is:", result)
    print("Time taken:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()