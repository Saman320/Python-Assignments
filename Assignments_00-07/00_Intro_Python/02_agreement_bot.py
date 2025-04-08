import pyfiglet
import termcolor

def main():
    title = pyfiglet.figlet_format("Favorite Animal", font="slant")
    print(termcolor.colored(title, "cyan"))
    
    print(termcolor.colored("What's your favorite animal?", "yellow", attrs=["bold", "blink"]))
    animal = input(termcolor.colored(">> ", "green", attrs=["bold"]))
    
    print(termcolor.colored(f"Wow! My favorite animal is also {animal}! 🐾", "magenta", attrs=["bold"]))

if __name__ == '__main__':
    main()
