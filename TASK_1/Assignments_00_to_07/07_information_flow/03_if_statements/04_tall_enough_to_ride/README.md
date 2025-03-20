# 🎢 Height Checker for Rides 🎡  

## 📜 Description  
This Python program determines whether a user is **tall enough** to ride a rollercoaster 🎢 based on a **pre-set height requirement**.

### 📍 How It Works  
✅ Enter your **height (in cm)** when prompted.  
✅ The program will check if you meet the ride's height requirement.  
✅ Keep checking different heights or press **Enter** to exit.  

---

## 🚀 Features  
✔️ **Interactive CLI-based input system**  
✔️ **Continuous checking until the user exits**  
✔️ **Graceful error handling for invalid inputs**  
✔️ **User-friendly messages with emojis for better engagement**  

---

## 💻 Installation & Usage  

### 🔧 Requirements  
- 🐍 **Python 3.x** installed  

### 📥 How to Run?  
1️⃣ **Save the script** as `height_checker.py`.  
2️⃣ **Open your terminal or command prompt**.  
3️⃣ **Run the script** using:  
   ```sh
   python height_checker.py
   ```  
4️⃣ **Enter your height** when prompted.  

---

## 🎮 Example Runs  

```
🎡 Welcome to the Ride Height Checker! 🎡
👉 Minimum height required: 90 cm

📏 How tall are you? 100
✅ You're tall enough to ride! 🎢 Enjoy!
```
```
🎡 Welcome to the Ride Height Checker! 🎡
👉 Minimum height required: 90 cm

📏 How tall are you? 70
❌ Sorry, you're not tall enough yet. But maybe next year! 🌱
```
```
🎡 Welcome to the Ride Height Checker! 🎡
👉 Minimum height required: 90 cm

📏 How tall are you? abc
⚠️ Invalid input! Please enter a valid height in cm.
```
```
🎡 Welcome to the Ride Height Checker! 🎡
👉 Minimum height required: 90 cm

📏 How tall are you? 
👋 Exiting... Have a great day! 🚀
```

---

## 📝 Notes  
- This program **continuously accepts inputs** until the user decides to exit.  
- If the input is **not a number**, the program will handle the error and prompt the user again.  
- A **minimum height requirement** is set, but you can modify `MIN_HEIGHT` in the script.  

---

## 📄 License  
This project is **open-source**. Feel free to modify and use! 🚀  

💡 **Happy Coding!** 🎢🎡 