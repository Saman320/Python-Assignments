import pyfiglet
import termcolor

def main():
    title = pyfiglet.figlet_format("Temp Converter", font="starwars")
    print(termcolor.colored(title, "yellow", attrs=["bold"]))
    
    print(termcolor.colored("==============================", "blue", attrs=["bold"]))
    print(termcolor.colored("Temperature Conversion (Fahrenheit to Celsius)", "cyan", attrs=["bold", "underline"]))
    print(termcolor.colored("==============================", "blue", attrs=["bold"]))
    
    print(termcolor.colored("Enter the temperature in Fahrenheit below: ", "green", attrs=["bold"]))
    fahrenheit = float(input(termcolor.colored(">> ", "magenta", attrs=["bold"])))
    
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    print(termcolor.colored("==============================", "blue", attrs=["bold"]))
    print(termcolor.colored(f"Temperature: {fahrenheit}F = {celsius:.2f}C", "magenta", attrs=["bold", "underline"]))
    print(termcolor.colored("==============================", "blue", attrs=["bold"]))

if __name__ == '__main__':
    main()