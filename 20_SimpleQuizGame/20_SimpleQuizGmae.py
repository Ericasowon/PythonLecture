# Goal
# Store questions and answers in a dictionary
# Ask the user each question in order
# If correct, add +1 to score; if wrong, mark as incorrect
# Display the final score at the end


print("❓ Simple Quiz Game Start!")

# Questions and Answers
quiz = {
    "What function is used to print a string in Python?": "print",
    "What function is used to get the length of a list in Python?": "len",
    "What symbol is used for comments in Python?": "#",
    "What data type is used to store 3.14?": "float"
}

score = 0

for question, answer in quiz.items():
    print("\nQuestion: " + question)
    user_answer = input("Answer: ")

    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is '{answer}'.")

print(f"\n🎉 Game Over! Final Score: {score} / {len(quiz)}")
