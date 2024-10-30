# weight convertor

weight = float(input("Enter your weight: "))
unit = input("Enter the unit of measurment (K or L): ")

if unit == "K" or unit == 'k':
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} was not valid")

print(f"Your weight is {round(weight, 2)} in {unit}")