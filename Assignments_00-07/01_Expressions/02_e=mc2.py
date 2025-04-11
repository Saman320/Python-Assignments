# Mass-Energy Equivalence Calculator
# Using Einstein's famous equation: E = mc²

C = 299_792_458  # Speed of light in m/s

def main():
    print("=" * 60)
    print("💡 Einstein's Mass-Energy Calculator".center(60))
    print("=" * 60)

    try:
        # Taking input from the user
        mass_input = input("\n🔢 Enter mass in kilograms: ")
        mass_in_kg = float(mass_input)

        # Calculate energy using E = mc²
        energy_in_joules = mass_in_kg * (C ** 2)

        # Display results
        print("\n🧠 Using the formula: E = m × c²")
        print(f"📦 Mass (m):        {mass_in_kg} kg")
        print(f"⚡ Speed of Light:  {C} m/s")
        print(f"🔥 Energy (E):      {energy_in_joules:.2e} joules")

    except ValueError:
        print("\n❌ Invalid input! Please enter a numeric value.")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
