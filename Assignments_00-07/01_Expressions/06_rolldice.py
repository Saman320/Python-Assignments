import random
import time
import os

NUM_SIDES = 6


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    header = """
  ╔═══════════════════════════════════╗
  ║         🎲 Dice Roller Game        ║
  ╚═══════════════════════════════════╝
    """
    print(f"\033[1;34m{header}\033[0m")


def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    return die1, die2, die1 + die2


def animate_rolling():
    print("Rolling the dice", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")


def show_result(die1, die2, total):
    result = f"""
    ┌──────────── Dice Result ────────────┐
    │   🎯 Die 1 : {die1:<28}│
    │   🎯 Die 2 : {die2:<28}│
    │   🧮 Total : {total:<27}│
    └─────────────────────────────────────┘
    """
    print(f"\033[1;32m{result}\033[0m")


def main():
    clear_screen()
    print_header()
    input("🎮 Press ENTER to roll the dice...")
    animate_rolling()
    die1, die2, total = roll_dice()
    show_result(die1, die2, total)


if __name__ == '__main__':
    main()
