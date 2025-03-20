def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop from 1 to num inclusive
        if num % i == 0:  # Check if i is a divisor of num
            print(i, end=" ")
    print()

def main():
    num = int(input("Enter a number: "))  # Get user input
    print_divisors(num)  # Call function to print divisors

if __name__ == "__main__":
    main()

