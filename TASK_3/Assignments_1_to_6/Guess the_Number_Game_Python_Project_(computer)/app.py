import random

def ai_guess():
    """Generate a random guess between 1 and 10."""
    return random.randint(1, 10)

def main():
    print("🤖 Number Guessing Game")
    print("=======================")
    print("Think of a number between 1 and 10, and I'll try to guess it!")
    
    # Initialize game state
    attempts = 1
    game_over = False
    ai_guess_number = ai_guess()
    
    while not game_over:
        print(f"\nAttempt #{attempts}")
        print(f"My guess is: {ai_guess_number}")
        
        # Ask the user for feedback
        user_feedback = input("Is my guess correct? (Enter 'correct', 'higher', or 'lower'): ").strip().lower()
        
        if user_feedback == "correct":
            print(f"\n🎉 Congratulations! I guessed your number in {attempts} attempts!")
            print(f"The number was {ai_guess_number}.")
            game_over = True
        elif user_feedback == "higher":
            ai_guess_number = random.randint(ai_guess_number + 1, 10)
            attempts += 1
        elif user_feedback == "lower":
            ai_guess_number = random.randint(1, ai_guess_number - 1)
            attempts += 1
        else:
            print("🚨 Invalid input! Please enter 'correct', 'higher', or 'lower'.")
    
    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing! Goodbye! 🎮")

if __name__ == "__main__":
    main()