# Goal
# The computer randomly selects a number between 1 and 100
# The user keeps guessing until they get the correct number
# The program gives hints: higher or lower
# It also tells the user how many tries it took

# Concepts used
# Using import random / input() / while loop / if-else statements
# Use of variables

import random

# Randomly select a number between 1 and 100
secret_number = random.randint(1, 100)
tries = 0;  # To keep track of the number of attempts

print("🔢 Guess the number between 1 and 100!")

while True:
    guess = input("Enter your guess : ")

    # Check if the input is a number
    if not guess.isdigit():
        print("❗ Please enter a valid number.")
        continue

    guess = int(guess)
    tries += 1

    if guess < secret_number:
        print("⬆️ Try a higher number!")
    elif guess > secret_number:
        print("⬇️ Try a lower number!")
    else:
        print(f"🎉 Correct! You guessed it in {tries} tries.")
        break
