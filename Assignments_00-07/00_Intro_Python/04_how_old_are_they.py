import random
import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def main():

    # Assigning dynamic ages with a random slight variation
    base_age = 21
    Anton = base_age
    Beth = Anton + random.randint(5, 8)  # Beth is 5-8 years older than Anton
    Chen = Beth + random.randint(18, 22)  # Chen is 18-22 years older than Beth
    Drew = Anton + Chen
    Ethan = Chen

    # Getting current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Adding a header with some style
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "Age Calculation Program")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    
    # Printing the current timestamp in a colorful format
    print(Fore.GREEN + f"Date and Time: {current_time}")
    print(Fore.CYAN + "=" * 50)

    # Printing the names and ages with some colorful formatting
    print(Fore.MAGENTA + f"Anton is {Anton} years old")
    print(Fore.RED + f"Beth is {Beth} years old")
    print(Fore.BLUE + f"Chen is {Chen} years old")
    print(Fore.YELLOW + f"Drew is {Drew} years old")
    print(Fore.GREEN + f"Ethan is {Ethan} years old")
    
    print(Fore.CYAN + "=" * 50)

if __name__ == '__main__':
    main()
