# Program to calculate BMI
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100)**2

print("You BMI  is :: ",bmi)

if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi <= 34.9:
    print("You are severely over weight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")