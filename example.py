def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    numbers = range(1, 20)
    primes = [number for number in numbers if is_prime(number)]
    print("Prime numbers between 1 and 20:", primes)

if __name__ == "__main__":
    main()
