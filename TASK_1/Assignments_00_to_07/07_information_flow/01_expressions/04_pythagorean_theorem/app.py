import math  # Import math module for square root calculation

def main():
    """ Command-line version of the Pythagorean Theorem Calculator """
    try:
        ab = float(input("Enter the length of AB: "))  # Get side AB
        ac = float(input("Enter the length of AC: "))  # Get side AC
        bc = math.sqrt(ab**2 + ac**2)  # Compute hypotenuse using Pythagorean theorem
        print(f"The length of BC (the hypotenuse) is: {bc}")
    except ValueError:
        print("Please enter a valid number.")

# Required line to run the main function
if __name__ == '__main__':
    main()

