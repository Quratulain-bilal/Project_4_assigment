MAX_TERM_VALUE = 10000

def fibonacci_sequence():
    curr_term, next_term = 0, 1
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")
        curr_term, next_term = next_term, curr_term + next_term

def main():
    print("Fibonacci Sequence up to", MAX_TERM_VALUE, ":")
    fibonacci_sequence()

if __name__ == '__main__':
    main()


