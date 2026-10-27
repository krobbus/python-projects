# Weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or P): ")

if weight <= 0:
    print(f"{round(weight)} is not valid weight")
else:
    if unit == "K" or "k":
        weight = weight * 2.205
        unit = "Lbs."
        print(f"Your weight is {round(weight, 1)}{unit}")
    elif unit == "P" or "p":
        weight = weight * 2.205
        unit = "Kgs."
        print(f"Your weight is {round(weight, 1)}{unit}")
    else:
        print(f"{unit} is not valid unit")