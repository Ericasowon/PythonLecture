# using dictionary + loops + conditional statements together

# Goal
# Allow the user to enter desired products and quantities
# Add them to the shopping cart and calculate the final payment amount


print("🛒 Shopping Cart Simulator")

# Product list (dictionary: {item: price})
store = {
    "Apple": 1000,
    "Banana": 2000,
    "Milk": 2500,
    "Bread": 3000
}

cart = {}  # Shopping cart

while True:
    print("\n📦 Available Products:")
    for item, price in store.items():
        print(f"- {item}: {price} won")

    choice = input("\nEnter the product name to purchase (type 'end' to finish): ")

    if choice.lower() == "end":
        break

    if choice not in store:
        print("⚠ This product is not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("⚠ Please enter a valid number for quantity.")
        continue

    # Add to cart
    if choice in cart:
        cart[choice] += quantity
    else:
        cart[choice] = quantity

print("\n🛒 Final Shopping Cart:")
total = 0
for item, quantity in cart.items():
    price = store[item] * quantity
    total += price
    print(f"{item} x {quantity} = {price} won")

print(f"\n💰 Total Payment: {total} won")
