def sum_of_numbers(numbers):
    """Calculate the sum of all numbers in the list."""
    total = sum(numbers)  # Cleaner approach using built-in sum
    return total

def get_user_input():
    """Prompt user to enter numbers separated by commas."""
    try:
        user_input = input("Enter numbers separated by commas (e.g., 10, 20, 30): ")
        numbers = [int(num.strip()) for num in user_input.split(',')]
        return numbers
    except ValueError:
        print("⚠️ Invalid input! Please enter only integers separated by commas.")
        return get_user_input()  # Retry input

def main():
    print("🧮 Welcome to the Number Sum Calculator")
    print("======================================")

    numbers_list = get_user_input()
    result = sum_of_numbers(numbers_list)

    print("\n✅ Numbers Entered:", numbers_list)
    print("🔢 Sum of Numbers:", result)

if __name__ == '__main__':
    main()
