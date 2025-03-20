# Constants
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def calculate_seconds_in_year():
    """Calculates the number of seconds in a year."""
    return DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

def main():
    seconds = calculate_seconds_in_year()
    print(f"There are {seconds} seconds in a year!")

if __name__ == "__main__":
    main()


