# Goal
# Calculate how many days are left until (or have passed since) a user-input date
# Compare it with today's date and display in D-5, D+10 format

# Concepts used
# datetime module
# Get user input using input()
# Convert string to date (strptime)
# Calculate difference between dates (timedelta)

from datetime import datetime

print("📅 Welcome to the D-Day Calculator!")

while True:
    date_str = input("Enter a target date (YYYY-MM-DD), or type 'q' to quit: ")
    if date_str.lower() == 'q':
        print("👋 Exiting the program.")
        break

    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()

        delta = (target_date - today).days

        if delta > 0:
            print(f"✅ {delta} days remaining. (D-{delta})")
        elif delta < 0:
            print(f"📌 {abs(delta)} days have passed. (D+{abs(delta)})")
        else:
            print("🎉 Today is the D-Day!")

    except ValueError:
        print("❗ Please check the date format. (Example: 2025-12-25)")
