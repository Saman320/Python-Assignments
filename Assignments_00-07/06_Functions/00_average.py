from rich.console import Console
from rich.prompt import Prompt

console = Console()

def find_average(num1, num2):
    return (num1 + num2) / 2

def main():
    console.rule("[bold green]Average Calculator[/bold green]")
    
    try:
        # Taking input using Rich Prompt
        num1 = float(Prompt.ask("Enter the first number"))
        num2 = float(Prompt.ask("Enter the second number"))

        average = find_average(num1, num2)

        # Displaying the result with formatting
        console.print(f"\n[bold cyan]The average of {num1} and {num2} is:[/bold cyan] [bold yellow]{average}[/bold yellow]\n")

    except ValueError:
        console.print("[bold red]Invalid input! Please enter numeric values.[/bold red]")

if __name__ == '__main__':
    main()
