def is_leap_year(year):
    """Determines if a given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    try:
        year = int(input("Please enter a year: "))
        if is_leap_year(year):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    except ValueError:
        print("Invalid input! Please enter a valid year.")

if __name__ == "__main__":
    main()

