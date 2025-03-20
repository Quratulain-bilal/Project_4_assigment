def greet(name: str) -> str:
    return "Greetings " + name + "!"

def main():
    name = input("What's your name? ")
    print(greet(name))

if __name__ == "__main__":
    main()

