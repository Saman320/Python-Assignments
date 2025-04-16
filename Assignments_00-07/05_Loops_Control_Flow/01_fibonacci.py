def main():
    MAX_VALUE = 10000
    a, b = 0, 1

    print("\n🔁 Fibonacci Numbers up to 10,000:\n")

    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b

    print("\n\n✅ Sequence Complete.")

if __name__ == '__main__':
    main()
