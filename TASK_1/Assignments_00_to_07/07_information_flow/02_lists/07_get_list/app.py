def main():
    lst = []  # Initialize an empty list

    while True:
        val = input("Enter a value: ")  # Prompt user for input
        if val == "":  # Stop when input is empty
            break
        lst.append(val)  # Add input to the list
    
    print("Here's the list:", lst)

if __name__ == '__main__':
    main()

