def print_ones_digit(num):
    print(f"\033[92mThe ones digit is: {num % 10}\033[0m")

def main():
    num = int(input("\033[96mEnter a number: \033[0m"))
    print_ones_digit(num)

if __name__ == '__main__':
    main()
