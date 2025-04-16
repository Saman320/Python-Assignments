import random

def main():
    print("\n🎲 Random Number Generator")
    print("Generating 10 random numbers between 1 and 100...\n")

    numbers = [random.randint(1, 100) for _ in range(10)]
    print("🔢 Numbers:", *numbers, "\n")

if __name__ == '__main__':
    main()
