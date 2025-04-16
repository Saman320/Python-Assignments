MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def main():
    lst = []
    n = int(input("Enter the number of elements you want in the list: "))
    
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("\nOriginal list:", lst)
    shorten(lst)
    print("\nShortened list (if needed):", lst)

if __name__ == '__main__':
    main()
