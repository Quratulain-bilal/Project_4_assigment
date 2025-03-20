import random

# Function to determine the winner
def is_win(player, opponent):
    """
    Return True if the player wins against the opponent.
    Rules: Rock (r) beats Scissors (s), Scissors (s) beats Paper (p), Paper (p) beats Rock (r)
    """
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

# Function to display rules and choices
def display_rules():
    print("\nWelcome to Rock-Paper-Scissors!")
    print("Rules:")
    print("- Rock (r) beats Scissors (s)")
    print("- Scissors (s) beats Paper (p)")
    print("- Paper (p) beats Rock (r)\n")

# Function to get valid user input
def get_user_choice():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower().strip()
        if user in choices:
            return user
        print("Invalid choice! Please choose 'r', 'p', or 's'.")

# Function to play one round of the game
def play_round():
    # Mapping shorthand to full names for display
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    # Get user and computer choices
    user = get_user_choice()
    computer = random.choice(list(choices.keys()))
    print(f"\nYou chose {choices[user]}.")
    print(f"Computer chose {choices[computer]}.")

    # Determine the result
    if user == computer:
        return "It's a tie!", 0
    elif is_win(user, computer):
        return "You won!", 1
    else:
        return "You lost!", -1

# Main function to manage the game loop
def main():
    display_rules()
    user_score = 0
    computer_score = 0

    while True:
        result, score = play_round()
        print(result)

        # Update scores
        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1

        # Display current scores
        print(f"\nCurrent Scores: You - {user_score}, Computer - {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("\nFinal Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break

# Entry point of the program
if __name__ == '__main__':
    main()
