def main():
    AFFIRMATION = "I am strong, confident, and capable of achieving my goals."
    
    print("Please type the following affirmation: ")
    print(AFFIRMATION)

    user_feedback = input("> ")  # Get user's input
    
    while user_feedback != AFFIRMATION:  # Repeat until the correct affirmation is entered
        print("\nThat was not the affirmation. Try again!")
        print("Please type the following affirmation: ")
        print(AFFIRMATION)
        user_feedback = input("> ")

    print("\nThat's right! Keep believing in yourself! 😊")

# Required to run the main function
if __name__ == "__main__":
    main()
