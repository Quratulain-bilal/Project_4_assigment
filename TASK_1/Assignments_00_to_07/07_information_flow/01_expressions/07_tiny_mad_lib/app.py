# 🌠 Space Adventure Story Generator 🚀
# 🎯 This script creates a fun and interactive space-themed story using user input.

# 📜 Sentence starter for the story
STORY_START = "One day, I found a mysterious spaceship. It took me to a "

def create_story():
    """
    📌 Function to generate a space-themed story by taking user input.
    """
    # 🎭 Get words from the user
    adjective = input("🌟 Enter an adjective: ")
    planet = input("🪐 Enter the name of a planet: ")
    creature = input("👽 Enter a type of alien or creature: ")

    # 📝 Generate and print the final story
    print("\n🚀 Your Space Adventure Begins! 🚀")
    print(STORY_START + f"{adjective} planet called {planet}, where I met a {creature}!")

# 🚀 Run the program
if __name__ == "__main__":
    create_story()
