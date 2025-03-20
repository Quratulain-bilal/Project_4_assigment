# 🟢 Square Calculator 🟢
# 🎯 This script calculates and displays the square of a given number.

def calculate_square():
    """
    📌 Function to calculate the square of a user-input number.
    """
    try:
        # 🔢 Get the number from the user
        num = float(input("🔢 Type a number to see its square: "))

        # 🧮 Calculate the square
        square = num ** 2

        # 📢 Display the result
        print(f"✅ {num} squared is {square} 🎯")

    except ValueError:
        print("⚠️ Please enter a valid numeric value! 🚫")

# 🚀 Run the program
if __name__ == '__main__':
    calculate_square()
