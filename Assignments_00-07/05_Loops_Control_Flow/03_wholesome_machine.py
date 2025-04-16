def main():
    affirmation = "I am capable of doing anything I put my mind to."

    print("\n🧘‍♀️  Daily Affirmation Practice\n")
    print(f"👉  Type this affirmation exactly as shown:\n\n    \"{affirmation}\"\n")

    while True:
        user_input = input("\033[36m✨ Your input: \033[0m")

        if user_input.strip() == affirmation:
            print("\n🌟 That's right! You did it. Keep believing in yourself!\n")
            break
        else:
            print("\n😕 Oops! That wasn't quite right. Try again.\n")

if __name__ == '__main__':
    main()
