def print_divisors(num):
    print("\033[94mDivisors:\033[0m", end=" ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(f"\033[92m{i}\033[0m", end=' ')
    print()  # Newline

def main():
    try:
        num = int(input("\033[96mEnter a number: \033[0m"))
        print(f"\033[93mHere are the divisors of {num}:\033[0m")
        print_divisors(num)
    except ValueError:
        print("\033[91mInvalid input. Please enter a valid integer.\033[0m")

if __name__ == '__main__':
    main()
