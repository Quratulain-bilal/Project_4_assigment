def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    print(in_range(n, low, high))

if __name__ == "__main__":
    main()

