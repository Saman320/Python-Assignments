import time

def main():
    print("\n🌟 Get Ready for Launch Sequence!\n")
    
    for i in range(10, 0, -1):
        print(f"  ⏳ T-{i}...", end="\r")
        time.sleep(1)  # Thoda delay for dramatic effect

    print("🚀 Liftoff! The rocket has launched!\n")

if __name__ == '__main__':
    main()
