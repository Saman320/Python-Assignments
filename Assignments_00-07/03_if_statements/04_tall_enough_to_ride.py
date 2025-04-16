def main():
    print("\n🎢 Welcome to RideCheck!")
    print("Check if you're tall enough to ride.\n")

    while True:
        height = input("👉 Enter your height in inches (or press Enter to exit): ")

        if height == "":
            print("\n👋 Done! Thanks for checking. Stay awesome!\n")
            break

        try:
            height = int(height)
        except ValueError:
            print("⚠️  Please enter a valid number.\n")
            continue

        if height >= 50:
            print("✅ You're tall enough. Enjoy the ride! 🎉\n")
        else:
            print("❌ Not tall enough yet — come back stronger next year! 💪\n")

if __name__ == '__main__':
    main()
