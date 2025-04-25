import random

# Probability that the function 'done' returns True
DONE_LIKELIHOOD = 0.2

def done():
    """
    Returns True with a probability defined by DONE_LIKELIHOOD.
    Used to randomly decide whether to stop counting.
    """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """
    Prints numbers from 1 to 10 but may stop early if done() returns True.
    """
    for i in range(1, 11):
        if done():
            return  # Randomly stop the function
        print(i, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

if __name__ == '__main__':
    main()
