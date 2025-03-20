🔄 Mutable List Modification Example
📜 Description
This program demonstrates mutability in Python, showing how changes to mutable data types (like lists) persist even when modified inside a function without returning the modified object.

In contrast, immutable data types (like strings and numbers) do not retain modifications unless explicitly returned.

💡 Key Concept: Lists are mutable, meaning they can be changed in place, while strings and numbers are immutable and require explicit return statements to reflect changes.

❓ Problem Statement
Consider a function that adds multiple copies of a given value to a list.

🟢 Mutable types (lists, dictionaries): Changes persist even without returning.
🔴 Immutable types (strings, tuples, numbers): Changes do not persist unless explicitly returned.
This program defines:

python
Copy
Edit
def add_three_copies(my_list, data):
    my_list.extend([data] * 3)
The function modifies my_list without returning it!

🌟 Features
✅ Demonstrates list mutability in Python
✅ Uses a helper function for modification
✅ Compares list states before and after function execution
✅ Simple and interactive example

🚀 Installation & Usage
🔧 Requirements
🐍 Python 3.x installed
📥 How to Run?
1️⃣ Download the script and save it as mutable_list.py.
2️⃣ Open your terminal or command prompt.
3️⃣ Run the script with:

sh
Copy
Edit
python mutable_list.py
4️⃣ Enter a message when prompted.

🎮 Example Run
pgsql
Copy
Edit
Enter a message to copy: Python Rocks!  
List before: []  
List after: ['Python Rocks!', 'Python Rocks!', 'Python Rocks!']
🛠️ The list is updated without being returned!

🔍 Understanding Mutability in Python
🔹 Mutable Types (modifiable in place)

Lists (list)
Dictionaries (dict)
Sets (set)
🔸 Immutable Types (cannot be changed in place)

Strings (str)
Tuples (tuple)
Numbers (int, float)
💡 Why does this matter?

If you modify a mutable object inside a function, the changes persist globally.
If you modify an immutable object, you need to return the new value to reflect changes.
📝 Notes
Lists in Python are mutable, meaning they retain modifications even if they are not returned from a function.
Be careful when modifying lists inside functions, as changes persist outside the function scope.
Different programming languages have different mutability rules, so always check the behavior!
📄 License
This project is open-source and free to use. Feel free to modify and share! 🎉

If you found this useful, give it a ⭐ on GitHub! 😃✨

🔥 Enjoy experimenting with Python's mutability! 🚀🐍