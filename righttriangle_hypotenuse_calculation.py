# Math calculation of right triangle hypotenuse using built-in math module
import math

# triangle
a = int(input("Enter the side A: "))
b = int(input("Enter the side B: "))

c = math.sqrt((pow(a, 2) + pow(b,2)))

print(f"The side C of the triangle is {c}")