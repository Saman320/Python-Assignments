import random

SIDES_ON_DIE = 6

def simulate_roll(round_num):
    first_die = random.randint(1, SIDES_ON_DIE)
    second_die = random.randint(1, SIDES_ON_DIE)
    total = first_die + second_die

    print(f"\n🎲 Roll {round_num}")
    print(f"   ➤ First Die:  {first_die}")
    print(f"   ➤ Second Die: {second_die}")
    print(f"   ➤ Total:      {total}")

def run_simulation():
    local_die = 10
    print("🎮 Dice Roll Simulator".center(40, "="))
    print(f"\n🔧 Initial value of local_die in run_simulation(): {local_die}\n")

    for i in range(1, 4):
        simulate_roll(i)

    print(f"\n🧠 Final value of local_die remains: {local_die}")
    print("\n" + "=" * 40)

if __name__ == "__main__":
    run_simulation()
