# ---variables---
string_example = "Alef"
integer_example = 22
float_example = 8.99

print(string_example)
print(f"Hello, I'm {string_example} and I'm {integer_example} years old")

# ---input---
name = input("What is your name?: ")
age = int(input("How old are you?: "))
age += 1

print(f"Hello, {name}\nHappy Birthday!\nYou are {age} years old now")