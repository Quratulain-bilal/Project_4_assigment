import time  # ⏳ Delay effect ke liye
import os    # 🖥️ Screen clear karne ke liye (Windows/Linux)

# 📏 Canvas ka size define karein
CANVAS_WIDTH = 10   # ⚙️ Columns (width)
CANVAS_HEIGHT = 10  # ⚙️ Rows (height)
ERASER_SIZE = 2     # 🔲 Eraser ka size

# 🎨 Pehle pura canvas blue blocks se bhar dete hain
canvas = [['█' for _ in range(CANVAS_WIDTH)] for _ in range(CANVAS_HEIGHT)]

def print_canvas():
    """
    🖼️ Yeh function canvas ko print karega aur instructions dega.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # 🔄 Screen clear karna
    for row in canvas:
        print(" ".join(row))  # 📜 Har row ko print karna
    print("\n🎮 Move the eraser using W/A/S/D. Press Q to quit.")

def erase(x, y):
    """
    ✏️ Yeh function eraser ke position par canvas clean karega.
    """
    for i in range(max(0, y), min(CANVAS_HEIGHT, y + ERASER_SIZE)):
        for j in range(max(0, x), min(CANVAS_WIDTH, x + ERASER_SIZE)):
            canvas[i][j] = ' '  # 🧽 Canvas clean karna

def main():
    """
    🔄 Yeh function game loop run karega, eraser move karayega, aur canvas update karega.
    """
    eraser_x, eraser_y = 0, 0  # 🎯 Eraser start position
    print_canvas()  # 🖥️ Pehli bar canvas dikhana
    
    while True:
        command = input("🔼🔽🔼 Enter move (W/A/S/D to move, Q to quit): ").strip().lower()
        
        if command == 'q':  # ❌ Quit karna
            break
        elif command == 'w' and eraser_y > 0:  # 🔼 Up
            eraser_y -= 1
        elif command == 's' and eraser_y < CANVAS_HEIGHT - ERASER_SIZE:  # 🔽 Down
            eraser_y += 1
        elif command == 'a' and eraser_x > 0:  # ◀️ Left
            eraser_x -= 1
        elif command == 'd' and eraser_x < CANVAS_WIDTH - ERASER_SIZE:  # ▶️ Right
            eraser_x += 1
        
        erase(eraser_x, eraser_y)  # ✏️ Erase karna
        print_canvas()  # 🔄 Update screen
        time.sleep(0.1)  # ⏳ Thoda delay for smooth effect

# 🚀 Program ko run karne ka tareeqa
if __name__ == "__main__":
    main()
