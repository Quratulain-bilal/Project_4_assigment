import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and prints their results."""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2

    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

def main():
    roll_dice()

if __name__ == "__main__":
    main()


