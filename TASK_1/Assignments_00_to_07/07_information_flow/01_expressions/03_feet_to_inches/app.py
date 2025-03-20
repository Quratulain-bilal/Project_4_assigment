INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches in 1 foot.

def main():
    """ Command-line version of Feet to Inches Converter """
    try:
        feet = float(input("Enter number of feet: "))  # Get the number of feet
        inches = feet * INCHES_IN_FOOT  # Convert to inches
        print(f"That is {inches} inches!")
    except ValueError:
        print("Please enter a valid number.")

# Required line to run the main function
if __name__ == '__main__':
    main()


