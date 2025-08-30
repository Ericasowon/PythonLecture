# Goal
# Write a memo → Save to file
# Load and display saved memos
# Allow managing multiple memos

FILENAME = "memo.txt"

while True:
    print("\n📝 Memo Pad Menu")
    print("1. Write Memo")
    print("2. View Memos")
    print("3. Exit")

    choice = input("Select: ")

    if choice == "1":
        memo = input("Enter memo: ")
        with open(FILENAME, "a", encoding="utf-8") as f:  # Append mode
            f.write(memo + "\n")
        print("✅ Memo has been saved.")

    elif choice == "2":
        print("\n📖 Saved Memos:")
        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                content = f.read()
                print(content if content else "(No memos)")
        except FileNotFoundError:
            print("(No memos yet.)")

    elif choice == "3":
        print("👋 Exiting Memo Pad.")
        break

    else:
        print("⚠ Invalid input.")
