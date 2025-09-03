# Goal
# The program asks the user to input their height (cm) and weight (kg).
# It then calculates the BMI using the formula:
#     BMI = weight (kg) / (height (m))^2
# Finally, it outputs a message based on the BMI result.

# BMI Calculator

# Input height and weight
height = float(input("Enter your height (cm): "))   # Get height in cm
weight = float(input("Enter your weight (kg): "))   # Get weight in kg

# BMI calculation (convert cm → m)
height_m = height / 100           # Convert height to meters
bmi = weight / (height_m ** 2)    # Formula: weight ÷ (height in meters)²

# Print result
print(f"Your BMI is {bmi:.2f}")

# Evaluation
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 23:
    print("Normal weight")
elif 23 <= bmi < 25:
    print("Overweight")
else:
    print("Obese")
