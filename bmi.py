weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bmi = round(weight/(height*height),2)
print(f"Your BMI is {bmi}")
if bmi>=30:
    print(f"You are obese")
elif bmi>=25 and bmi<30:
    print(f"You are overweight")
elif bmi>=18.5 and bmi<25:
    print(f"You are normal")
else:
    print("You are underweight")