import random

def generate_password(length):
    """
    Generates a random password using a fixed set of characters.
    """
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*.?"
    return "".join(random.choices(chars, k=length))

def main():
    print("🌟 Welcome to the  Password Generator! 🌟")

    # Input: Number of passwords
    amount_password = input("Enter the number of passwords you want to generate: ")
    while not amount_password.isdigit() or int(amount_password) <= 0:
        print("⚠️ Please enter a valid positive number.")
        amount_password = input("Enter the number of passwords you want to generate: ")
    amount_password = int(amount_password)

    # Input: Length of each password
    length_password = input("Enter the length of each password: ")
    while not length_password.isdigit() or int(length_password) <= 0:
        print("⚠️ Please enter a valid positive number.")
        length_password = input("Enter the length of each password: ")
    length_password = int(length_password)

    # Generate and display passwords
    print("\n.Generated Passwords.")
    for i in range(amount_password):
        password = generate_password(length_password)
        print(f"Password {i+1}: {password}")

    print("\nThank you for using the Password Generator! 👋")

# Start the program
if __name__ == "__main__":
    main()