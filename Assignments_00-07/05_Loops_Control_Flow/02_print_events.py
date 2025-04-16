def main():
    count = 20
    even_numbers = [i * 2 for i in range(count)]

    print("\n" + "=" * 40)
    print("      ✨ First 20 Even Numbers ✨")
    print("=" * 40)

    # Print numbers in a nicely formatted row
    for index, num in enumerate(even_numbers, start=1):
        print(f"{num:4}", end=" ")
        if index % 10 == 0:  # New line after every 10 numbers
            print()

    print("\n" + "=" * 40)
    print("✅  Display complete.")
    print("=" * 40 + "\n")

if __name__ == '__main__':
    main()
