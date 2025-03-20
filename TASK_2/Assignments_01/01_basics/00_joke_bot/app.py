# Constants
PROMPT: str = "What do you want? "
JOKE: str = "Here's a joke for you! Why do programmers prefer dark mode? Because light attracts bugs! 🐛😆"
SORRY: str = "Sorry, I only tell jokes."

def main():
    # Ask the user what they want
    user_input = input(PROMPT)
    
    # Normalize the input by stripping whitespace and converting to lowercase
    user_input = user_input.strip().lower()
    
    # Check if the user input is "joke"
    if user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == "__main__":
    main()
