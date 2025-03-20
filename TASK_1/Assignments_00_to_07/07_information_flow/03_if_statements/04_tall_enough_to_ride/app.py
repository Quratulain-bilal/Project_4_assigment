MINIMUM_HEIGHT = 50  # Minimum height required to ride

def main():
    while True:
        height = input("How tall are you? (Press enter to exit) ")
        if height == "":
            break
        
        try:
            height = float(height)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()

