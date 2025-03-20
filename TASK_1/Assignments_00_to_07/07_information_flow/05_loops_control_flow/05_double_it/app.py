def double_until_threshold():
    print("Number Doubling Program")
    
    number = int(input("Enter a number: "))
    
    curr_value = number
    result = []
    
    while curr_value < 100:
        curr_value *= 2
        result.append(curr_value)
    
    print("Doubled Values:")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    double_until_threshold()

