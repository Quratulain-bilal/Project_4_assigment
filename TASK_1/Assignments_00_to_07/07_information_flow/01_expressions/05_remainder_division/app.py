def main():
    """ Command-line version of Division Calculator """
    try:
        dividend = int(input("Please enter an integer to be divided: "))  # Get first number
        divisor = int(input("Please enter an integer to divide by: "))  # Get second number

        if divisor == 0:
            print("Division by zero is not allowed.")
            return

        quotient = dividend // divisor  # Integer division
        remainder = dividend % divisor  # Get remainder
        print(f"The result of this division is {quotient} with a remainder of {remainder}")
    except ValueError:
        print("Please enter a valid integer.")

# Required line to run the main function
if __name__ == '__main__':
    main()

