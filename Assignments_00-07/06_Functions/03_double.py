def double(num):
    """Returns double the input number."""
    return num * 2

def main():
    print("\033[96m=== Double Number Calculator ===\033[0m")
    
    try:
        num = int(input("\033[94mEnter a number: \033[0m"))
        result = double(num)
        print(f"\033[92mDouble of {num} is {result}\033[0m")
    except ValueError:
        print("\033[91m❌ Invalid input. Please enter a valid integer.\033[0m")

if __name__ == '__main__':
    main()
