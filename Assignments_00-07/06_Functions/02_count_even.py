def count_even():
    """
    Continuously collects integer input from the user until Enter is pressed.
    Then counts and prints how many even numbers were entered.
    """
    numbers = []  # List to store valid integers

    while True:
        user_input = input("Enter an integer or press Enter to stop: ")
        if user_input == "":
            break  # Stop input on empty string

        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid integer.")

    # Count how many even numbers are in the list
    even_count = sum(1 for number in numbers if number % 2 == 0)

    # Display the result
    print(f"\n✅ Number of even numbers entered: {even_count}")

def main():
    print("🧮 Even Number Counter")
    count_even()

if __name__ == '__main__':
    main()
