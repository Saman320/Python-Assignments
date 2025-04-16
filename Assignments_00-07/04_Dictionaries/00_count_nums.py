def main():
    num_counts = {}

    print("\nWelcome to the Number Occurrence Counter.")
    print("Enter numbers to count their occurrences. Press Enter without typing to exit.\n")

    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            print("\nExiting the program. Here's the result:")
            break

        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue
        
        # Update the count for the entered number
        num_counts[number] = num_counts.get(number, 0) + 1

    # Display the counts
    print("\nNumber Occurrences:")
    for num, count in num_counts.items():
        print(f"{num} appears {count} time(s).")

if __name__ == '__main__':
    main()
