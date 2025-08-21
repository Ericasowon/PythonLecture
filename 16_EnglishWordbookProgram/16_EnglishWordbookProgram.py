# Goal
# Input English words and their meanings, then store them
# Load the saved wordbook / Add new words
# A simple word quiz feature can also be added


print("📖 English Wordbook Program")

# Wordbook dictionary
wordbook = {}

while True:
    print("\nMenu:")
    print("1. Add a word")
    print("2. View wordbook")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        eng = input("Enter English word: ")
        kor = input("Enter meaning: ")
        wordbook[eng] = kor
        print("✅ Word has been added.")

    elif choice == "2":
        print("\n📌 Wordbook")
        for eng, kor in wordbook.items():
            print(f"{eng} : {kor}")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("⚠ Invalid input.")
