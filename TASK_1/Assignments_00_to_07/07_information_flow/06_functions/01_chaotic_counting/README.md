# Chaotic Counting Program

This project is a Python program that simulates chaotic counting. The program attempts to count from 1 to 10 but may stop early based on a random probability.

## How It Works

- The program starts counting from 1 to 10.
- At each step, it checks whether it should stop early using a probability factor (`DONE_LIKELIHOOD`).
- If the condition is met, the counting stops prematurely.
- Otherwise, it continues counting until it reaches 10.
- The program then prints "I'm done" to indicate completion.

## Requirements
- Python 3+

## Running the Project
Run the following command in the terminal:
```sh
python app.py
```

This project demonstrates control flow, randomness, and early function termination in Python.

