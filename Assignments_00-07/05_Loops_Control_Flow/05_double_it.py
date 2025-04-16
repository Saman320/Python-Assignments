def main():
    print("\n🔢 Let's double your number until it reaches 100 or more!\n")
    
    try:
        curr_value = int(input("👉 Enter a number to begin: "))
        print("\n🧮 Doubling in progress...\n")

        while curr_value < 100:
            curr_value *= 2
            print(f"➡️ {curr_value}", end=" ")

        print("\n\n✅ Done! Reached 100 or more.\n")

    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == '__main__':
    main()
