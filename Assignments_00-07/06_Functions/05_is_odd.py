def main():
    print("\033[96m=== Even & Odd Numbers from 10 to 19 ===\033[0m")
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"\033[92m{num} is even\033[0m")
        else:
            print(f"\033[91m{num} is odd\033[0m")

if __name__ == '__main__':
    main()
