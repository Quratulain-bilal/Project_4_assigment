# 🔐 Password Generator

This project is a simple yet powerful password generator that allows users to create random passwords of customizable length.

## 🕹️ How It Works

1. The user specifies the number of passwords to generate.
2. The user enters the desired length for each password.
3. The program generates random passwords using uppercase, lowercase, digits, and special characters.
4. The generated passwords are displayed to the user.
5. The user is given the option to generate more passwords or exit the program.

## 📌 Example Output

```
🔐 Password Generator
=====================
Enter the number of passwords to generate: 3
Enter the length of each password: 12

Generated Passwords:
Password 1: G#2vSd!8pXqA
Password 2: m4@Lt5Bn*ZpK
Password 3: qY!6wF3#RjTp

Do you want to generate more passwords? (yes/no): no
Thanks for using the Password Generator! Goodbye! 🔐
```

## 🛠️ Code Breakdown

- **User Input Handling:** Ensures the user enters a valid positive number for both password count and length.
- **Random Password Generation:** Uses `random.choice()` to select characters from a mix of letters, digits, and symbols.
- **Formatted Output:** Clearly displays each generated password in a structured manner.
- **Replay Option:** Allows users to generate more passwords if desired.

🎉 A great project to practice working with strings, loops, and randomness in Python!

