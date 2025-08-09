# Goal
# Store words and their meanings in a dictionary
# Show the meaning and let the user guess the word
# Calculate score and show correct/incorrect results

# Concepts used
# Dictionary (dict) data type
# random.choice() for selecting a random question
# Loops (while, for)
# String comparison

import random

# Word dictionary
word_dict = {
    "apple": "a fruit that is usually red, green, or yellow",
    "banana": "a long curved fruit with a yellow peel",
    "computer": "an electronic device for storing and processing data",
    "python": "a popular programming language",
    "school": "a place where students learn"
}

print("📚 English Vocabulary Quiz Game!")
score = 0

# Number of rounds
rounds = int(input("How many questions would you like to answer? "))

for i in range(rounds):
    # Randomly select a word
    word, meaning = random.choice(list(word_dict.items()))
    print(f"\nQuestion {i+1}: What is the English word for '{meaning}'?")
    answer = input("Your answer: ").strip().lower()

    if answer == word:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was '{word}'.")

print("\n🎯 Game Over!")
print(f"You got {score} out of {rounds} correct.")

