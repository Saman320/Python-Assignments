from colorama import init, Fore, Style
import time

# Initialize colorama
init(autoreset=True)

def main():
    print(Style.BRIGHT + Fore.BLUE + "\n╔════════════════════════════════════════╗")
    print(Fore.CYAN + "     🔢  Welcome to the Square Finder")
    print(Fore.BLUE + "╚════════════════════════════════════════╝\n")
    
    try:
        # Smooth user prompt
        number = float(input(Fore.YELLOW + "🔸 Enter a number to find its square: "))

        # Simulate thinking...
        print(Fore.LIGHTBLACK_EX + "\nCalculating...", end="", flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        print()

        # Calculate the square
        square = number ** 2

        print(Fore.GREEN + f"\n✅ Result: {number}² = {square}")
        print(Fore.MAGENTA + "\n💡 Tip: The square of a number is the number multiplied by itself.")
        print(Fore.BLUE + "\n────────────────────────────────────────────")

    except ValueError:
        print(Fore.RED + "\n❌ Error: Please enter a valid numeric value.")

if __name__ == '__main__':
    main()
