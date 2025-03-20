# 🤖 AI Number Guessing Game

This project is a simple number guessing game where the AI attempts to guess the user's chosen number between 1 and 10 based on feedback.

## 🕹️ How It Works

1. The user thinks of a number between 1 and 10.
2. The AI generates a random guess.
3. The user provides feedback:
   - **'correct'** if the AI guessed the number correctly.
   - **'higher'** if the user's number is higher than the AI's guess.
   - **'lower'** if the user's number is lower than the AI's guess.
4. The AI continues guessing based on the feedback until it correctly identifies the number.
5. The game ends when the AI correctly guesses the number, and the user can choose to play again.

## 📌 Example Output

```
🤖 Number Guessing Game
=======================
Think of a number between 1 and 10, and I'll try to guess it!

Attempt #1
My guess is: 5
Is my guess correct? (Enter 'correct', 'higher', or 'lower'): lower

Attempt #2
My guess is: 3
Is my guess correct? (Enter 'correct', 'higher', or 'lower'): correct

🎉 Congratulations! I guessed your number in 2 attempts!
The number was 3.

Do you want to play again? (yes/no): no
Thanks for playing! Goodbye! 🎮
```

## 🛠️ Code Breakdown

- **Random Guess Generation:** The AI generates a random number between 1 and 10.
- **User Feedback Processing:** The user provides hints to guide the AI toward the correct number.
- **Loop Until Correct Guess:** The AI continues guessing until the correct number is found.
- **Replay Option:** The user can choose to play again or exit the game.

🎉 A great beginner-friendly project to practice loops, user input handling, and logic flow in Python!

