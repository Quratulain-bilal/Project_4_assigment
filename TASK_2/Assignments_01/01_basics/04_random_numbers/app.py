import random

def generate_random_numbers(count=10, start=1, end=100):
    """
    Generates a list of random integers within a specified range.

    Parameters:
    - count (int): Number of random numbers to generate.
    - start (int): Lower bound of the range (inclusive).
    - end (int): Upper bound of the range (inclusive).

    Returns:
    - List[int]: A list containing 'count' random integers between 'start' and 'end'.
    """
    return [random.randint(start, end) for _ in range(count)]

def main():
    random_numbers = generate_random_numbers()
    print("Generated random numbers:")
    print(" ".join(map(str, random_numbers)))

if __name__ == "__main__":
    main()
