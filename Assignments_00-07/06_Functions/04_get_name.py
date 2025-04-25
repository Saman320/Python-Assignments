def get_name():
    """Returns a predefined name."""
    return "Sophia"

def main():
    print("\033[96m=== Friendly Greeter ===\033[0m")
    name = get_name()
    print(f"\033[92mHowdy {name}! 🤠\033[0m")

if __name__ == '__main__':
    main()
