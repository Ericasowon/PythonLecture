# Program Description
# random.randint() → Randomly selects the table number (a) and the multiplier (b).
# If the user enters 0, the program will exit.
# Checks if the input is a number; if it's not, the program asks again.
# If the answer is correct, the score increases; if it's wrong, the correct answer is shown.
# At the end, the program prints the total number of correct answers.


import random

print("📚 Multiplication Table Quiz")
print("Enter 0 to quit.\n")

score = 0
total_questions = 0

while True:
    a = random.randint(2, 9)  # Multiplication table (2–9)
    b = random.randint(1, 9)  # Multiplier (1–9)
    answer = a * b

    user_input = input(f"{a} x {b} = ")

    # Exit condition
    if user_input == "0":
        break

    # Check if input is a number
    if not user_input.isdigit():
        print("⚠ Please enter numbers only.\n")
        continue

    total_questions += 1
    if int(user_input) == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong. The correct answer is {answer}.\n")

print(f"🎯 You answered {score} out of {total_questions} questions correctly!")
