def main():
    lst = []  # Empty list to store user inputs
    
    print("Welcome! Enter values to add to the list. Press 'Enter' without typing anything to finish.")
    
    while True:
        value = input("Enter a value: ")  # Taking input from user
        
        if value == "":  # If user presses enter without typing anything, exit loop
            break
        
        lst.append(value)  # Adding value to the list

    print(f"\nHere's the list with {len(lst)} item(s):", lst)  # Printing the final list with count

# Required line to run the program
if __name__ == '__main__':
    main()
