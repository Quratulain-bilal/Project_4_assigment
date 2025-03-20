import time

def generate_story_logic(noun, adjective, verb):
    """Generates a fun story using user-provided words."""
    return f"One fine morning, a {adjective} {noun} decided to {verb} through the bustling city, marveling at the sights and sounds."

def main():
    print("\n📜 Welcome to the **Mad Libs Story Generator!** 🎭")
    print("========================================")
    print("🖊️ Fill in the blanks with creative words to generate a unique story!\n")
    
    # Input fields with fun prompts
    noun = input("🟠 Enter a **Noun** (e.g., dragon): ").strip()
    adjective = input("🔵 Enter an **Adjective** (e.g., sparkly): ").strip()
    verb = input("🟢 Enter a **Verb** (e.g., dances): ").strip()
    
    # Validate input
    if not noun or not adjective or not verb:
        print("🚨 **Oops!** Please enter **all required words** to create your story.")
        return
    
    if any(" " in word or "," in word for word in [noun, adjective, verb]):
        print("🚨 **No spaces or commas!** Enter **one word per field.**")
        return
    
    print("\n⏳ **Generating your unique story...**")
    time.sleep(2)  # Small delay for fun effect
    
    # Generate and display the story
    story = generate_story_logic(noun, adjective, verb)
    
    print("\n🎉 **Your Fun Story is Ready!**")
    print("-------------------------------------------------")
    print(f"📖 {story}")
    print("-------------------------------------------------\n")

    # Ask for replay
    play_again = input("🔄 **Want to create another story?** (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("\n✨ **Thanks for playing! Keep being creative!** ✨")

if __name__ == "__main__":
    main()
