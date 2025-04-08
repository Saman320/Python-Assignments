from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "🔺 Triangle Perimeter Calculator")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)

    try:
        # Prompt the user to enter the lengths of each side of the triangle
        side1 = float(input(Fore.GREEN + "👉 Enter the length of side 1: "))
        side2 = float(input(Fore.GREEN + "👉 Enter the length of side 2: "))
        side3 = float(input(Fore.GREEN + "👉 Enter the length of side 3: "))

        # Calculate the perimeter
        perimeter = side1 + side2 + side3

        print(Fore.CYAN + "-" * 50)
        # Display result
        print(Fore.MAGENTA + f"✅ The perimeter of the triangle is: {perimeter}")
        print(Fore.CYAN + "-" * 50)

    except ValueError:
        print(Fore.RED + "❌ Invalid input! Please enter numeric values only.")

if __name__ == '__main__':
    main()
