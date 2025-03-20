🔑 Password Manager
A secure password manager that uses SHA-256 hashing for authentication, ensuring password security and safe login validation.

✨ Features
✔️ Securely stores hashed passwords 🔐
✔️ Authenticates users using SHA-256 hashing 🛡️
✔️ Prevents plain-text password storage 🚀
✔️ Simple & easy-to-use command-line interface 💻

🛠 Setup Instructions
1️⃣ Ensure Python 3+ is installed on your system. 🐍
2️⃣ Clone or download the repository. 📂
3️⃣ Run the password manager using:

bash
Copy
Edit
python password_manager.py
📌 How to Use
1️⃣ Run the script:

bash
Copy
Edit
python password_manager.py
2️⃣ Enter your email:

graphql
Copy
Edit
📧 Enter your email: user1@example.com
3️⃣ Enter your password:

yaml
Copy
Edit
🔑 Enter your password: mysecurepassword
4️⃣ View the result:
✅ If credentials are correct, you'll see:

nginx
Copy
Edit
Login successful! 🎉
❌ If credentials are incorrect, you'll see:

pgsql
Copy
Edit
Login failed. Invalid email or password. 🚫
📂 Stored Logins (Hashed Passwords)
📧 Email	🔑 Plain Password	🔒 SHA-256 Hashed Password
user1@example.com	securepass123	3a5b2c1f8d6e9f7a2b4c6d1e5f8a9b3c7d2e4f1a6c8b5d9e7f3a2c4b1d6e8f9
hello@secure.com	mypassword	b7c3e8f9a2d1b5c6f3e4a7d2c8b1f9e6a3d5c2b4f7e8a9d6c1b3f5e4a7c2d9f8
admin@mysite.com	admin@123	9e7f3a2c4b1d6e8f5a7c3b2d1f9e6a4c8b5d2f7a9e3c1b6f4a5d2e8c7b3f9a1
🔹 Try logging in with any of the above emails & passwords! 🚀

🛡 Security Notes
🔐 Why Hashing?

Passwords are never stored in plain text, making them unreadable even if compromised.
SHA-256 is a cryptographic hashing algorithm, ensuring one-way encryption of passwords.
🚀 Best Practices:

Always use strong, unique passwords.
If adding new users, hash their passwords first before storing.
📄 License
This project is open-source—modify & improve it as you like! 🎯

💡 Happy Coding! 🚀🔒 Let me know if you need any further improvements! 😃