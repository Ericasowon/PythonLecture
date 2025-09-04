# Goal
# Create a program that converts a temperature entered by the user
# in either Fahrenheit or Celsius into the other unit.

# 🌡️ Fahrenheit ↔ Celsius Converter

# Choose conversion direction
print("1: Celsius → Fahrenheit")
print("2: Fahrenheit → Celsius")
choice = input("Select an option (1 or 2): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.1f}℃ is equal to {fahrenheit:.1f}℉ 🔥")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.1f}℉ is equal to {celsius:.1f}℃ ❄️")

else:
    print("Invalid input 🚫")
