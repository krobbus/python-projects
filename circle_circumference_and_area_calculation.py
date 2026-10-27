# Math calculation for circle circumference and area using built-in math module

import math

# circle
radius = int(input("Enter the radius of circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference of the circle is {circumference}")
print(f"The area of the circle is {round(area, 2)}cm^2")