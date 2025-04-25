def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:
        print(f"\033[94mI am excited to add this {word} to my vast collection of them!\033[0m")
    elif part_of_speech == 1:
        print(f"\033[92mIt's so nice outside today it makes me want to {word}!\033[0m")
    elif part_of_speech == 2:
        print(f"\033[93mLooking out my window, the sky is big and {word}!\033[0m")
    else:
        print("\033[91mInvalid choice! Please enter 0 for noun, 1 for verb, or 2 for adjective.\033[0m")

def main():
    try:
        word = input("\033[96mPlease type a noun, verb, or adjective: \033[0m")
        part_of_speech = int(input("\033[96mIs this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: \033[0m"))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("\033[91mInvalid input. Please enter a valid number for part of speech.\033[0m")

# Ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()
