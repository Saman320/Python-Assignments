# Inches to Feet Conversion Calculator
# Conversion formula: 1 foot = 12 inches

INCHES_IN_FOOT = 12  # 1 foot = 12 inches

def main():
    print("\n" + "=" * 60)
    print("🔶🔷 Inches to Feet Converter 🔷🔶".center(60))  # Bold heading with symbols
    print("=" * 60)

    print("\n💡 This tool helps you convert feet to inches!\n")
    
    try:
        # User input for feet with a friendly prompt
        feet_input = input("📐 Please enter the number of feet : ")

        feet = float(feet_input)  # Convert input to float

        # Calculate inches
        inches = feet * INCHES_IN_FOOT

        # Creative output with a bit of flair
        print("\n" + "-" * 60)
        print(f"✅ {feet} feet = {inches} inches 🌟")
        print("-" * 60)

    except ValueError:
        # Error handling with a friendly message
        print("\n❌ Invalid input! Please enter a valid number for feet.")

    # End message with a clean closing line
    print("\n" + "=" * 60)
    print("✨ Thank you for using the converter! ✨".center(60))
    print("=" * 60)

if __name__ == '__main__':
    main()
