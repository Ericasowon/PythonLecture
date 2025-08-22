# Input name, phone number, and email, then save them  
# Display the entire address book  
# Save and load data from a file (addressbook.json)  


import json

FILENAME = "addressbook.json"

# Load address book
try:
    with open(FILENAME, "r", encoding="utf-8") as f:
        addressbook = json.load(f)
except FileNotFoundError:
    addressbook = {}

while True:
    print("\n📇 Address Book Menu")
    print("1. Add Contact")
    print("2. View Address Book")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        addressbook[name] = {"Phone": phone, "Email": email}

        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(addressbook, f, ensure_ascii=False, indent=2)

        print(f"✅ Contact for {name} has been saved.")

    elif choice == "2":
        print("\n📌 Full Address Book")
        for name, info in addressbook.items():
            print(f"{name} | Phone: {info['Phone']} | Email: {info['Email']}")

    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in addressbook:
            info = addressbook[search_name]
            print(f"🔍 Contact info for {search_name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
        else:
            print("⚠ That name is not in the address book.")

    elif choice == "4":
        print("📕 Exiting program.")
        break

    else:
        print("⚠ Invalid input.")
