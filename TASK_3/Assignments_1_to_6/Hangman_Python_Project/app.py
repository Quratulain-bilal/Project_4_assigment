import random

def hangman():
    print("Welcome to Hangman! 🎮")
    print("Guess the word before the hangman is complete.")

    words = ["python", "programming", "hangman", "challenge", "developer", "algorithm"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 5
    guessed_letters = []

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word: " + word)
            break

    else:
        print("\nGame over! 😢 The word was: " + word)

hangman()