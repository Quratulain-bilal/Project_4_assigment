import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled: {die1} and {die2}, Total: {total}")

def main():
    die1 = 10  # Variable scope demonstration
    print(f"die1 in main() starts as: {die1}")
    
    # Roll the dice three times
    for _ in range(3):
        roll_dice()
    
    print(f"die1 in main() is: {die1}")

if __name__ == '__main__':
    main()


