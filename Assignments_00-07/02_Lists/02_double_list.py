def double_numbers(numbers):
    """Returns a new list with each number doubled."""
    return [num * 2 for num in numbers]

def get_user_input():
    """Prompts the user to input numbers separated by commas."""
    try:
        user_input = input("Enter numbers separated by commas (e.g., 1, 2, 3): ")
        numbers = [int(num.strip()) for num in user_input.split(',')]
        return numbers
    except ValueError:
        print("⚠️ Invalid input! Please enter only integers separated by commas.")
        return get_user_input()  # Retry input

def main():
    print("🔁 Welcome to the Number Doubler")
    print("================================")

    numbers = get_user_input()
    doubled = double_numbers(numbers)

    print("\n📥 Original List:", numbers)
    print("📈 Doubled List:", doubled)

if __name__ == '__main__':
    main()
