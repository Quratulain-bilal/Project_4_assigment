MAX_LENGTH: int = 3

def shorten(lst):
    """Removes elements from the end of lst until its length is MAX_LENGTH."""
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(f"Removed: {last_elem}")

def get_lst():
    """Prompts the user to enter elements one by one and returns the list."""
    lst = []
    while True:
        elem = input("Enter an element (or press Enter to stop): ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    """Main function to get user input and process list shortening."""
    lst = get_lst()
    print("Original List:", lst)
    shorten(lst)
    print("Final List:", lst)

if __name__ == '__main__':
    main()

