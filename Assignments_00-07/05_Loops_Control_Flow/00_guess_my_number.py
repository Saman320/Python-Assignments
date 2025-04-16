import random

def main():
    print("\n🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 99...\n")

    secret_number = random.randint(0, 99)

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            if guess < secret_number:
                print("📉 Too low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"\n🎉 Congrats! You guessed it right. The number was: {secret_number}")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!\n")

if __name__ == '__main__':
    main()
