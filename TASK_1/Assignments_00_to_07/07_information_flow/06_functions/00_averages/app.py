def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b
    """
    return (a + b) / 2

def main():
    print("Average Calculation Program")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    avg_result = average(num1, num2)
    print(f"The average of {num1} and {num2} is: {avg_result}")
    
if __name__ == "__main__":
    main()



