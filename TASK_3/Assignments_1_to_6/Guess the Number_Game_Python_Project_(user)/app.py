import random

def play_game():
    """Simple number guessing game."""
    print("\n🎮 Welcome to Guess the Number!")
    print("Try to guess the number between 1 and 10.\n")

    secret_number = random.randint(1, 10)  # Random number
    attempts = 0
    hints = []

    while True:
        try:
            guess = int(input("Enter your guess (1-10): "))
            if guess < 1 or guess > 10:
                print("🚨 Please enter a number between 1 and 10!")
                continue
        except ValueError:
            print("🚨 Invalid input! Please enter a number.")
            continue

        attempts += 1  # Count attempts

        if guess == secret_number:
            print(f"🎉 Correct! The number was {secret_number}. You guessed it in {attempts} attempts!\n")
            break
        else:
            hint = "higher" if guess < secret_number else "lower"
            hints.append(f"💡 Hint: The number is {hint}.")
            print(f"💡 Hint: The number is {hint}.")

    print("\n💡 All Hints:")
    for hint in hints:
        print(hint)

    # Play again option
    if input("\nPlay again? (yes/no): ").strip().lower() == "yes":
        play_game()
    else:
        print("Thanks for playing! 🎮")

if __name__ == "__main__":
    play_game()
