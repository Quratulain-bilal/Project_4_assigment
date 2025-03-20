import random

DONE_LIKELIHOOD = 0.3  # Adjust likelihood of stopping early

def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Ends function execution and returns to main()
        print(curr_num)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()


