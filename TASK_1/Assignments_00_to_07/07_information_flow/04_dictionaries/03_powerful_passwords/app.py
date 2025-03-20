from hashlib import sha256

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    """
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    """
    return stored_logins.get(email) == hash_password(password_to_check)

def main():
    """
    Simulates a simple secure login system.
    """
    stored_logins = {
        "user1@example.com": "3a5b2c1f8d6e9f7a2b4c6d1e5f8a9b3c7d2e4f1a6c8b5d9e7f3a2c4b1d6e8f9",
        "hello@secure.com": "b7c3e8f9a2d1b5c6f3e4a7d2c8b1f9e6a3d5c2b4f7e8a9d6c1b3f5e4a7c2d9f8",
        "admin@mysite.com": "9e7f3a2c4b1d6e8f5a7c3b2d1f9e6a4c8b5d2f7a9e3c1b6f4a5d2e8c7b3f9a1"
    }
    
    email = input("📧 Enter your email: ")
    password = input("🔑 Enter your password: ")
    
    if login(email, stored_logins, password):
        print("✅ Login successful! Welcome! 🎉")
    else:
        print("❌ Login failed. Invalid email or password. Please try again. 🔐")

if __name__ == '__main__':
    main()
