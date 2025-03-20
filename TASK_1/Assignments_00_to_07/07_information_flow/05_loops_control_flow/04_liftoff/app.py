import time

def countdown_timer():
    print("🚀 Preparing for launch...")
    
    for i in range(5, 0, -1):  # Countdown from 5 to 1
        print(i)
        time.sleep(1)  # Adding a 1-second delay for a real countdown effect

    print("🔥 Blastoff! The mission has started! 🚀")

# Run the countdown
if __name__ == "__main__":
    countdown_timer()
