# Goal
# Input scores for multiple subjects and calculate the average, highest, and lowest scores
# Use a list to store and process the data
# print, int, for

print("📊 Grade Calculator (with Subject Names)")

scores = {}
n = int(input("Enter the number of subjects: "))

for i in range(n):
    subject = input(f"Enter the name of subject {i+1}: ")
    score = int(input(f"Enter the score for {subject}: "))
    scores[subject] = score

print("\n📌 Results")
for subject, score in scores.items():
    print(f"{subject}: {score} points")

values = list(scores.values())
print(f"\nTotal: {sum(values)}")
print(f"Average: {sum(values) / len(values):.2f}")
print(f"Highest Score: {max(values)}")
print(f"Lowest Score: {min(values)}")
