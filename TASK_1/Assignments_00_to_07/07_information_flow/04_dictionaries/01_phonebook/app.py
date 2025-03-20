def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup (or press Enter to exit): ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name} -> {phonebook[name]}")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()

