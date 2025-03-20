import random

def main():
    # Generate a random number between 1 and 55
    secret_number: int = random.randint(1, 55)
    
    # Print the initial message
    print("I am thinking of a number between 1 and 99...")
    
    # Get the user's first guess
    guess = int(input("Enter a guess: "))
    
    # Keep asking for guesses until the user guesses the correct number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Print an empty line for better readability
        print()
        
        # Get a new guess from the user
        guess = int(input("Enter a new guess: "))
    
    # Congratulate the user when they guess the correct number
    print("Congrats! The number was:", secret_number)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()