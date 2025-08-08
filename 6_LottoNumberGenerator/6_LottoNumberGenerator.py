# Goal
# Randomly select 6 unique numbers between 1 and 45
# Display the numbers in sorted order
# Optionally allow the user to generate multiple sets

# Concepts used
# random.sample() function
# list, sort(), input(), int()
# for and while loops (for advanced usage)

import random

print("🎰 Lotto Number Generator!")

while True:
    try:
        count = int(input("How many sets would you like to generate? (Enter a number, 0 to quit): "))
        if count == 0:
            print("👋 Exiting the generator.")
            break

        for i in range(count):
            numbers = random.sample(range(1, 46), 6)
            numbers.sort()
            print(f"🔹 Set {i+1}: {numbers}")

    except ValueError:
        print("❗ Please enter a valid number.")

