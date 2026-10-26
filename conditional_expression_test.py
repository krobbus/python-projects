# X if condition else Y

num = int(input("Enter your number: "))

result1 = ("POSITIVE" if num > 0 else "NEGATIVE")
result2 = ("EVEN" if num % 2 == 0 else "ODD")

print(f"Your {num} number is {result1}, {result2}")