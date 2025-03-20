
📥 Enter Values into a List
📜 Description
This Python program allows users to dynamically enter values into a list. Once the user presses Enter without typing anything, the program displays the full list of entered values.

🔹 Key Concept: The program continuously collects input until the user submits an empty value, making it an interactive way to work with lists!

🌟 Features
✅ Continuously collects user input 📌
✅ Stops when an empty input is detected ❌
✅ Displays the final list of entered values 📋
✅ Beginner-friendly & interactive 🏆

🚀 Installation & Usage
🔧 Requirements
🐍 Python 3.x installed
📥 How to Run?
1️⃣ Save the script as app.py.
2️⃣ Open your terminal or command prompt.
3️⃣ Run the script using:

sh
Copy
Edit
python app.py
4️⃣ Enter values one by one.
5️⃣ Press Enter without typing anything to stop input.

🎮 Example Run
yaml
Copy
Edit
Enter a value: Apple  
Enter a value: Banana  
Enter a value:  
Here's the list: ['Apple', 'Banana']  
🔹 The full list is displayed when input is stopped!

🛠 How It Works?
1️⃣ Loop runs indefinitely, collecting user input.
2️⃣ If input is empty, the loop breaks.
3️⃣ Final list is printed with all collected values.

Example Code:

python
Copy
Edit
def collect_values():
    values = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)
    print("Here's the list:", values)

collect_values()
📝 Notes
This program does not handle duplicate entries but allows them.
No error handling for invalid inputs (but can be added).
Works seamlessly in CLI environments for hands-on Python practice.
📄 License
This project is open-source. Modify, use, and share freely! 🚀

⭐ Love Python? Keep coding & exploring! 😃✨

🔥 Enjoy interactive list handling in Python! 🐍💡