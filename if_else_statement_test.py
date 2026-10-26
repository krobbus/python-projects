# ---if/else statement---

age = int(input("Enter your age: "))

if age >= 18:
    print("You're now signed up!")
elif age <= 0:
    print("Not valid age")
else:
    print("You must be 18+ to sign up")