import random
import os
import time

# Sentence templates with placeholders
TEMPLATES = [
    "Panaversity taught me to make a [adjective] [noun] that can [verb].",
    "One day, my [adjective] [noun] decided to [verb] on Mars.",
    "I built a [adjective] [noun] which can even [verb] during exams!",
    "Every coder dreams of a [adjective] [noun] that can [verb].",
    "My friend owns a [adjective] [noun] that always loves to [verb]."
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = """
  ╔═════════════════════════════════════════════╗
  ║       🎭 Random Sentence Generator          ║
  ╚═════════════════════════════════════════════╝
    """
    print(f"\033[1;36m{header}\033[0m")

def animate(text):
    print(text, end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

def get_input(prompt, emoji):
    return input(f"\033[1;33m{emoji} {prompt}: \033[0m")

def fill_template(template, adjective, noun, verb):
    return template.replace("[adjective]", adjective).replace("[noun]", noun).replace("[verb]", verb)

def main():
    clear_screen()
    print_header()

    animate("Let's create your random sentence")

    adjective = get_input("Type an adjective", "🎨")
    noun = get_input("Type a noun", "📦")
    verb = get_input("Type a verb", "🏃")

    chosen_template = random.choice(TEMPLATES)
    final_sentence = fill_template(chosen_template, adjective, noun, verb)

    animate("Generating your awesome sentence")
    
    print("\n📜 ➤ \033[1;32m" + final_sentence + "\033[0m\n")

if __name__ == "__main__":
    main()
