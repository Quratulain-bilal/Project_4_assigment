import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 200)  # Now the range is 1 to 200
    
    print("I am thinking of a number between 1 and 200... 🤔")
    
    # Get user's guess
    guess = int(input("🔢 Enter a guess: "))
    
    # Loop until the user guesses correctly
    while guess != secret_number:
        if guess < secret_number:
            print("⬆️ Your guess is too low!")
        else:
            print("⬇️ Your guess is too high!")
            
        print()  # Print an empty line for better readability
        guess = int(input("🔄 Enter a new guess: "))  # Get a new guess
        
    print(f"🎉 Congrats! The number was: {secret_number} 🎯")
    
if __name__ == '__main__':
    main()
