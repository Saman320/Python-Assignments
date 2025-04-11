import math
import time
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Function to calculate hypotenuse
def calculate_hypotenuse(ab, ac):
    return math.sqrt(ab**2 + ac**2)

def print_with_delay(text, delay=0.5):
    """ Print text with a delay to create an animation effect """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # New line after text

def main():
    # Stylish Title Section
    print(Fore.CYAN + Style.BRIGHT + "\n🌟 Welcome to the Hypotenuse Calculator 🌟")
    print("=" * 60 + "\n")
    
    # Interactive Section with animated text
    print_with_delay("Let's calculate the hypotenuse using the Pythagorean theorem!", 0.1)
    print_with_delay("Please enter the lengths of the two sides of the right triangle:", 0.1)
    
    try:
        # Input Section: Asking for side lengths
        ab = float(input(Fore.GREEN + Style.BRIGHT + "Enter the length of side AB (in units): "))
        ac = float(input(Fore.GREEN + Style.BRIGHT + "Enter the length of side AC (in units): "))
        
        # Perform Calculation
        bc = calculate_hypotenuse(ab, ac)

        # Output Result in a unique style
        print(Fore.YELLOW + Style.BRIGHT + "\n**************************************")
        print(f"🔺 The Hypotenuse (BC) is {bc:.2f} units 🔺")
        print("**************************************")

    except ValueError:
        print(Fore.RED + "🚨 Error: Please enter valid numeric values for the lengths!")

    # Closing Remarks
    print_with_delay("\nThank you for using the Hypotenuse Calculator!", 0.2)
    print("=" * 60 + "\n")

if __name__ == '__main__':
    main()
