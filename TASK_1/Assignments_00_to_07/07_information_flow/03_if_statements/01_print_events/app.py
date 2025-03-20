def main():
    """
    Prints the first 20 even numbers in a single line.
    """
    for i in range(20):  # Loop 20 times
        print(i * 2, end=" ")  # Multiply each number by 2 to get even numbers
    print()  # Prints a new line after the loop ends

# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
