# Goal
# Roll dice when Enter is pressed and display a number between 1 and 6
# Allow rolling two or more dice at once

# Concepts used
# random, while, if, for, except ValueError

import random

print("🎲 Dice Rolling Simulator")

while True:
    try:
        count = int(input("Enter the number of dice to roll (0 to quit): "))
        if count == 0:
            print("Exiting the game. 🎯")
            break

        results = []
        for _ in range(count):
            results.append(random.randint(1, 6))

        print(f"Result: {results} (Total: {sum(results)})")
        print("-" * 30)

    except ValueError:
        print("⚠ Please enter a valid number!")


