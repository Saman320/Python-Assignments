def main():
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.0
    }

    total_cost = 0  # Initialize total cost

    print("\nWelcome to the Fruit Price Calculator!")
    print("Here are the available fruits and their prices per unit:\n")
    
    # Display fruit prices
    for fruit, price in fruit_prices.items():
        print(f"{fruit.capitalize()} - ${price:.2f} per unit")

    print("\nPlease enter the quantity you would like to purchase for each fruit.\n")

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit}s would you like? "))
                if quantity < 0:
                    print("Please enter a non-negative number.\n")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")

        total_cost += quantity * price  # Multiply quantity with price

    # Print total cost
    print(f"\nYour total cost is: ${total_cost:.2f}")  # Display in 2 decimal places

if __name__ == '__main__':
    main()
