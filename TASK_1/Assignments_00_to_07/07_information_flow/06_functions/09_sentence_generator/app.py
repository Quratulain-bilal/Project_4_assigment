

def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"The {word} is essential for our survival.")
    elif part_of_speech == 1:
        print(f"Every morning, I {word} to start my day.")
    elif part_of_speech == 2:
        print(f"The weather today is absolutely {word}.")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    try:
        part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("Invalid input! Please enter 0, 1, or 2.")

if __name__ == '__main__':
    main()
