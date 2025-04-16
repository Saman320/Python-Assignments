def main():
    print("🗳️ Voting Eligibility Checker\n")

    age = int(input("🔹 How old are you? "))

    print("\n🔍 Checking eligibility...\n")

    if age >= 16:
        print("✅ You can vote in Peturksbouipo (Voting age: 16)")
    else:
        print("❌ You cannot vote in Peturksbouipo (Voting age: 16)")

    if age >= 25:
        print("✅ You can vote in Stanlau (Voting age: 25)")
    else:
        print("❌ You cannot vote in Stanlau (Voting age: 25)")

    if age >= 48:
        print("✅ You can vote in Mayengua (Voting age: 48)")
    else:
        print("❌ You cannot vote in Mayengua (Voting age: 48)")

if __name__ == '__main__':
    main()
