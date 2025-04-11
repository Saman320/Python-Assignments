import time
import os

# Constants
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    header = """
  ╔════════════════════════════════════════════╗
  ║       ⏳ Seconds in a Year Calculator       ║
  ╚════════════════════════════════════════════╝
    """
    print(f"\033[1;35m{header}\033[0m")


def animate_calculation():
    print("Calculating", end="")
    for _ in range(4):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")


def calculate_seconds_in_year():
    return DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN


def display_result(total_seconds):
    message = f"""
    ┌────────────────────────────────────────────┐
    │  ✅ There are \033[1;32m{total_seconds:,}\033[0m seconds in a year!       │
    └────────────────────────────────────────────┘
    """
    print(message)


def main():
    clear_screen()
    print_header()
    input("🧮 Press ENTER to calculate seconds in a year...")
    animate_calculation()
    total_seconds = calculate_seconds_in_year()
    display_result(total_seconds)


if __name__ == '__main__':
    main()
