def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far = sum(numbers)
    return total_so_far


def main():
    """Command-line interface for summing numbers."""
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        sum_of_numbers = add_many_numbers(numbers)
        print(f"The sum of the entered numbers is: {sum_of_numbers}")
    except ValueError:
        print("Invalid input! Please enter valid numbers separated by spaces.")


if __name__ == "__main__":
    main()

