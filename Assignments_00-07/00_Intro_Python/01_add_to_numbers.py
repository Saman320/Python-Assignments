import sys

# ANSI color codes for styling
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def main():
    print(f"{CYAN}" + "=" * 40)
    print(f"{GREEN}     🧮 Simple CLI Addition Program {RESET}")
    print(f"{CYAN}" + "=" * 40)

    try:
        num1 = int(input(f"{YELLOW}➤ Enter first number: {RESET}"))
        num2 = int(input(f"{YELLOW}➤ Enter second number: {RESET}"))

        total = num1 + num2
        print(f"{GREEN}\n✅ The total sum is: {total}{RESET}\n")

    except ValueError:
        print(f"{RED}\n❌ Invalid input! Please enter valid numbers.{RESET}")
        sys.exit(1)  # Exit the program with an error code

    print(f"{CYAN}" + "=" * 40 + f"{RESET}")

if __name__ == '__main__':
    main()
