def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(f"\033[92m{message}\033[0m")  # Add color to the repeated message

def main():
    try:
        message = input("\033[96mPlease type a message: \033[0m")
        repeats = int(input("\033[96mEnter a number of times to repeat your message: \033[0m"))
        print(f"\033[93mRepeating your message {repeats} times:\033[0m")
        print_multiple(message, repeats)
    except ValueError:
        print("\033[91mInvalid input. Please enter a valid number for repeats.\033[0m")

# Ensures the main function is executed when the script runs
if __name__ == "__main__":
    main()
