# Goal
# Get two numbers and an operator (+, -, *, /) from the user
# Print the result of the calculation
# Handle invalid inputs gracefully

# Concepts used
# input() / if-elif-else / float()
# Function (def) to separate calculation logic


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "❗ You can't divide by zero."
        return num1 / num2
    else:
        return "❗ Unsupported operator."

print("🔢 Simple Calculator.")
print("Available operators: +, -, *, /")

while True:
    first = input("Enter the first number (or type 'q' to quit): ")
    if first.lower() == 'q':
        print("Calculator exited. 👋")
        break
    second = input("Enter the second number: ")
    operator = input("Enter an operator (+, -, *, /): ")

    # Check if the inputs are valid numbers

    try:
        num1 = float(first)
        num2 = float(second)
    except ValueError:
        print("❗ Please enter valid numbers.")
        continue

    result = calculate(num1, num2, operator)
    print("Result : ", result)
    print("-" *60)    