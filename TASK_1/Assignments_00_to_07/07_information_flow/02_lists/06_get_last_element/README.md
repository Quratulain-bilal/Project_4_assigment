
🔚 Get Last Element from a List
📜 Description
This interactive Python program allows users to input a list of elements and then retrieves the last element efficiently. It demonstrates the power of Python’s negative indexing for list manipulation.

💡 Concept: Python lists are ordered collections where the last element can be accessed using lst[-1].

❓ Problem Statement
The user enters elements to form a dynamic list.
The function get_last_element(lst) extracts and prints the last item.
The list is guaranteed to be non-empty.
python
Copy
Edit
def get_last_element(lst):
    return lst[-1]  # Returns the last element efficiently
🌟 Features
✅ Accepts dynamic user input
✅ Retrieves and displays the last element
✅ Utilizes Python's negative indexing (-1)
✅ Simple and beginner-friendly

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
4️⃣ Enter list elements one by one.
5️⃣ Press Enter without typing anything to stop input.

🎮 Example Run
arduino
Copy
Edit
Please enter an element of the list or press Enter to stop: Apple  
Please enter an element of the list or press Enter to stop: Banana  
Please enter an element of the list or press Enter to stop:  
Last Element: Banana  
🔹 The last element entered is displayed as output!

🔍 Understanding Negative Indexing in Python
📌 Python supports negative indexing – meaning:

lst[-1] retrieves the last element.
lst[-2] retrieves the second last element, and so on.
Example:

python
Copy
Edit
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[-1])  # Output: Cherry
🔹 This approach is more efficient than using len(lst) - 1.

📝 Notes
The program assumes the list is non-empty.
If no input is given, an IndexError may occur (handling can be added for safety).
This example is a great starting point for learning list operations in Python!
📄 License
This project is open-source. Feel free to modify and share! 🚀

⭐ Found this useful? Star it on GitHub! 😃✨

🔥 Happy coding with Python lists! 🐍💡