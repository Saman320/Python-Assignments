def add_three_copies(my_list, data):
    """Adds three copies of data to the given list."""
    my_list.extend([data] * 3)  # Cleaner and shorter

def print_list(title, lst):
    """Nicely formatted print of a list with a title."""
    print(f"\n{title}: [{', '.join(map(str, lst))}]")

def main():
    print("📋 Welcome to the Triple Copy App")
    print("===================================")

    # User input
    message = input("🔤 Enter a message to copy three times: ")

    # Original list
    my_list = []
    print_list("📝 List before", my_list)

    # Modify list
    add_three_copies(my_list, message)

    # Result
    print_list("✅ List after", my_list)

if __name__ == '__main__':
    main()
