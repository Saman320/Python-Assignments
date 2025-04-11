import os
import time


def print_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    title = """
  ╔══════════════════════════════════════╗
  ║         🔢 Smart Divider App         ║
  ╚══════════════════════════════════════╝
    """
    print(f"\033[1;36m{title}\033[0m")


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(f"\033[1;3m{prompt}\033[0m "))
        except ValueError:
            print("\033[1;31m❌ Invalid input. Please enter a valid integer.\033[0m")


def calculate_division(num1: int, num2: int):
    if num2 == 0:
        return None, None
    return num1 // num2, num1 % num2


def show_result(quotient: int, remainder: int):
    result_box = f"""
    ┌──────────────────────────────────────┐
    │   ✅ Quotient : {quotient:<23}│
    │   🔁 Remainder: {remainder:<23}│
    └──────────────────────────────────────┘
    """
    print(f"\033[1;32m{result_box}\033[0m")


def main():
    print_title()
    print("Welcome to the Smart Divider App!\n")

    num1 = get_integer("Enter the number to be divided:")
    num2 = get_integer("Enter the number to divide by:")

    quotient, remainder = calculate_division(num1, num2)

    print("\nCalculating", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")

    if quotient is None:
        print("\033[1;31m❌ Error: Cannot divide by zero.\033[0m")
    else:
        show_result(quotient, remainder)


if __name__ == "__main__":
    main()
