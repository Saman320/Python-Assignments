def read_phone_numbers():
    phonebook = {}

    print("\nEnter contacts for your phonebook. Press Enter without a name to stop.")

    while True:
        name = input("Name: ")
        if not name:  # Exit the loop if the name is empty
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    print("\nPhonebook:")
    if phonebook:
        for name, number in phonebook.items():
            print(f"{name} -> {number}")
    else:
        print("No entries in the phonebook.")

def lookup_number(phonebook):
    print("\nSearch for a contact by name. Press Enter without a name to stop.")
    
    while True:
        name = input("Enter name to lookup: ")
        if not name:  # Exit if no input is given
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name}'s number: {phonebook[name]}")

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_number(phonebook)

if __name__ == '__main__':
    main()
