✂️ List Shortener Project
📜 Description
This interactive Python program allows users to enter a list of values, but automatically shortens the list to a maximum of 3 elements. If extra elements are entered, the program removes them and displays the final shortened list.

🔹 Key Concept: Ensures list size remains manageable and concise while allowing user interaction!

🌟 Features
✅ Collects user input dynamically 📥
✅ Restricts list size to a maximum of 3 elements 🚫
✅ Displays removed elements and the final list 📋
✅ Fully interactive CLI-based program 💻

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
5️⃣ Press Enter without typing anything to finalize the list.

🎮 Example Run
pgsql
Copy
Edit
Enter an element: Apple  
Enter an element: Banana  
Enter an element: Cherry  
Enter an element: Date  
Removed: Date  
Here's the final list: ['Apple', 'Banana', 'Cherry']
🔹 Only the first three elements are retained!

🛠 How It Works?
1️⃣ Loop collects user input, appending values to the list.
2️⃣ If the list exceeds 3 elements, extra values are removed.
3️⃣ Final list is displayed, along with removed items.

Example Code
python
Copy
Edit
def shorten_list():
    my_list = []
    
    while True:
        item = input("Enter an element: ")
        if item == "":
            break
        my_list.append(item)

        if len(my_list) > 3:
            removed = my_list.pop()
            print(f"Removed: {removed}")

    print("Here's the final list:", my_list)

shorten_list()
📝 Notes
The default max list length is 3, but you can modify it in the code.
This program automatically removes excess elements instead of preventing input.
Easy to extend for different list-length requirements.
📄 License
This project is open-source. Modify, use, and share freely! 🚀

⭐ Keep coding & exploring! 😃✨

🔥 Enjoy building smart Python applications! 🐍💡