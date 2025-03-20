import random

def main():
    N_NUMBERS = 10
    MIN_VALUE = 1
    MAX_VALUE = 100
    
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(" ".join(map(str, random_numbers)))

if __name__ == '__main__':
    main()

