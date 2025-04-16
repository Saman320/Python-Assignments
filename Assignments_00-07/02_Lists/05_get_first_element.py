from colorama import Fore, Style

def get_first_element(lst):
    """Prints the first element of the list."""
    print(f"\n{Fore.GREEN}🔹 The first element in the list is: {Style.BRIGHT}{lst[0]}{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}📋 Welcome to the Enhanced List Element Finder{Style.RESET_ALL}")
    print("============================================")

    while True:
        try:
            n = int(input(f"{Fore.MAGENTA}🔢 Enter the number of elements in the list: {Style.RESET_ALL}"))
            
            if n <= 0:
                print(f"{Fore.RED}⚠️ List must contain at least one element.{Style.RESET_ALL}")
                continue

            lst = []
            for i in range(n):
                element = input(f"{Fore.CYAN}➡️ Enter element {i + 1}: {Style.RESET_ALL}")
                lst.append(element)

            # Get the first element
            get_first_element(lst)

            retry = input(f"\n{Fore.CYAN}Do you want to try again? (y/n): {Style.RESET_ALL}").lower()
            if retry != 'y':
                break

        except ValueError:
            print(f"{Fore.RED}⚠️ Invalid input! Please enter a valid number.{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}👋 Goodbye!{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
