# 🔢 Number Frequency Counter

def count_frequencies():
    """
    Collects numbers from user input and counts their occurrences.

    Returns:
    - dict: A dictionary with numbers as keys and their frequencies as values.
    """
    print("\n🔢 Welcome to the Number Frequency Counter!")
    print("ℹ️  Enter numbers one by one. Press Enter without input to finish.\n")

    frequency_dict = {}  # Dictionary to store number counts

    while True:
        try:
            user_input = input("Enter a number (or press Enter to finish): ")

            if user_input == "":  # Stop input collection if Enter is pressed
                break

            number = int(user_input)  # Convert input to integer

            # Count occurrences
            frequency_dict[number] = frequency_dict.get(number, 0) + 1  

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    # Display results
    print("\n📊 Number Frequency Results:")
    if frequency_dict:
        for num, count in sorted(frequency_dict.items()):
            print(f"🔹 {num}: {count} time(s)")
    else:
        print("⚠️ No numbers were entered.")

    print("\n✅ Thank you for using the Number Frequency Counter! 🚀")

# Run the script when executed
if __name__ == "__main__":
    count_frequencies()
