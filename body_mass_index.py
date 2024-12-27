height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2, 1)

if bmi < 18.5:
    print(f"{bmi} - underweight")
elif bmi < 25:
    print(f"{bmi} - normal weight")
elif bmi < 30:
    print(f"{bmi} - overweight")
elif bmi < 35:
    print(f"{bmi} - obese")
else:
    print(f"{bmi} - clinically obese")