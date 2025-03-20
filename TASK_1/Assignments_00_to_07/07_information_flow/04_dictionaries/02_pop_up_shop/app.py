def main():
    """Calculates the total cost of fruits based on user input."""
    
    # Dictionary storing fruit names and their prices per unit ($)
    fruits = {
        'banana': 0.5,
        'pineapple': 3.0,
        'grapes': 2.5,
        'strawberry': 4.0,
        'watermelon': 7.0,
        'blueberry': 6.5
    }
    
    total_cost = 0  # Variable to store total cost

    # Loop through each fruit and ask the user for quantity
    for fruit_name, price in fruits.items():
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
        total_cost += price * amount_bought
    
    # Display total amount
    print(f"\n🛒 Your total is **${total_cost:.2f}**. Thank you for shopping! 🍉")

if __name__ == '__main__':
    main()
