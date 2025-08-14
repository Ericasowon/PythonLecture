# Goal
# Prompt the user to enter the item price and the amount paid, then calculate the change.
# Display the change broken down into denominations of 50,000 won, 10,000 won, 5,000 won,
# 1,000 won, 500 won, and 100 won.


print("💰 Change Calculator")

# User input
price = int(input("Enter the item price: "))
paid = int(input("Enter the amount paid: "))

# Calculate change
change = paid - price

if change < 0:
    print(f"⚠ You are short of {abs(change)} won.")
else:
    print(f"\nChange: {change} won")

    # Bill/Coin denominations
    units = [50000, 10000, 5000, 1000, 500, 100]
    for unit in units:
        count = change // unit   # Number of bills/coins of this denomination
        change %= unit           # Remaining amount
        if count > 0:
            print(f"{unit} won: {count} piece(s)")
