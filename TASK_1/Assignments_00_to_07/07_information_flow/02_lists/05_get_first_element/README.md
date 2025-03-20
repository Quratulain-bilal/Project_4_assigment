🎯 Get First Element from a List
📜 Description
This program prompts the user to enter elements into a list and retrieves the first element. It serves as a simple demonstration of list manipulation and user input handling in Python.

💡 Key Concept: Lists in Python maintain insertion order, and indexing starts from 0.

❓ Problem Statement
Users input elements one at a time to create a list.
The function get_first_element(lst) retrieves and prints the first element.
The list is guaranteed to be non-empty.
python
Copy
Edit
def get_first_element(lst):
    return lst[0]  # Returns the first element
🌟 Features
✅ Accepts user input dynamically
✅ Retrieves and displays the first element
✅ Demonstrates basic list indexing
✅ Interactive CLI-based execution

🚀 Installation & Usage
🔧 Requirements
🐍 Python 3.x installed
📥 How to Run?
1️⃣ Save the script as app.py.
2️⃣ Open your terminal or command prompt.
3️⃣ Run the script with:

sh
Copy
Edit
python app.py
4️⃣ Enter list elements one by one.
5️⃣ Press Enter without typing anything to stop input.

🎮 Example Run
arduino
Copy
Edit
Please enter an element of the list or press Enter to stop: Apple  
Please enter an element of the list or press Enter to stop: Banana  
Please enter an element of the list or press Enter to stop:  
First Element: Apple  
🔹 The first element entered is displayed as output!

🔍 Understanding Lists in Python
📌 Lists are ordered and mutable – meaning:

Ordered: Elements remain in the order they were inserted.
Mutable: You can modify the list after creation.
Indexing starts at 0 (first element is accessed with list[0]).
Example:

python
Copy
Edit
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])  # Output: Apple
📝 Notes
The program assumes the list is non-empty (i.e., at least one element is provided).
If no input is given, an IndexError may occur (this can be handled with additional checks).
This is a basic example of list operations in Python—useful for beginners!
📄 License
This project is open-source. Feel free to use, modify, and share! 🚀

⭐ If you found this useful, give it a star on GitHub! 😃✨

🔥 Happy coding with Python lists! 🐍💡