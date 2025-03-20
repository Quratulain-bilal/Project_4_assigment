def count_even(lst):
    """
    Returns number of even numbers in the list.
    """
    count = sum(1 for num in lst if num % 2 == 0)
    print(f"Number of even numbers: {count}")

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()


