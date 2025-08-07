# Goal
# Show a predefined sentence
# Measure how long the user takes to type the sentence
# Display typing accuracy (typos) and speed (WPM)

# Concepts used
# Measuring time with time module
# Getting user input with input()
# String comparison
# Lists and conditional statements


import time
import random

# ANSI escape codes for coloring

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Load sentences from external file

with open("Lyrics_Riize.txt", "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f if line.strip()]

print("⌨️ Typing Speed Tester (Riize Version)")
input("Press Enter when you're ready...")


# Randomly select sentences

num_tests = 3  # Number of sentences to test
total_wpm = 0
total_accuracy = 0

test_sentences = random.sample(sentences, num_tests)

for i, target in enumerate(test_sentences):
    print(f"\n==========================")
    print(f"📄 Test {i+1} - Start typing!")
    print("=========================")
    print("\nType the following sentence exactly as shown:\n")
    print("📝", target)
    input("\n🔔 Press Enter when you're ready...")


    # Start timer
    start_time = time.time()
    typed = input("\nYour input: ")
    end_time = time.time()

    # Calculate time taken

    elapsed_time = end_time - start_time
    elapsed_seconds = round(elapsed_time, 2)

    # Measure accuracy
    correct_chars = sum(1 for i, c in enumerate(typed) if i < len(target) and c == target[i])
    accuracy = round((correct_chars / len(target)) * 100, 2)

    # Calculate WPM (Words Per Minute)
    word_count = len(typed.split())
    wpm = round((word_count / elapsed_time) * 60)

    # Highlight typos
    highlighted = ""
    for i in range(max(len(target), len(typed))):
        if i < len(typed) and i < len(target):
            if typed[i] == target[i]:
                highlighted += GREEN + typed[i] + RESET
            else:
                highlighted += RED + typed[i] + RESET
        elif i < len(typed):  # 초과 입력 
            highlighted += RED + typed[i] + RESET
        else:
            highlighted += RED + "_" + RESET   # 빠뜨린 글자 

    print("\n📊 Summary of Results")
    print("\n🕒 Time taken:", elapsed_seconds, "seconds")
    print("🎯 Accuracy:", accuracy, "%")
    print("🚀 Typing speed:", wpm, "WPM")
    print("🔍 Typo highlights:\n" + highlighted)

    total_accuracy += accuracy
    total_wpm += wpm 


# Display averages
avg_accuracy = round(total_accuracy / num_tests, 2)
avg_wpm = round(total_wpm / num_tests, 2)

print("\n==========================")
print("✅ All tests completed!")
print("==========================")
print("📌 Average Accuracy:", avg_accuracy, "%")
print("📌 Average Typing Speed:", avg_wpm, "WPM")
