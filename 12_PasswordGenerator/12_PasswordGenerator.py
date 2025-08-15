# Goal
# Generate a password by randomly combining uppercase letters, lowercase letters,
# numbers, and special characters.
# Prompt the user to enter the desired password length and create it.

import random
import string

print("🔐 Strong Password Generator")

length = int(input("Enter the password length (minimum 4): "))

if length < 4:
    print("⚠ Minimum length is 4.")
else:
    # Select at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest with random characters from all categories
    characters = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(characters) for _ in range(length - 4)]

    # Shuffle to randomize order
    random.shuffle(password)

    # Join into the final password string
    print("Generated password:", ''.join(password))
