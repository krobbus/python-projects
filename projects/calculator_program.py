# Calculator program

operator = input("Enter an operator (+ - / *): ")
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

if operator == "+":
    result = first_num + second_num
    print(f"The answer is {result}")
elif operator == "-":
    result = first_num - second_num
    print(f"The answer is {result}")
elif operator == "/":
    result = first_num / second_num
    print(f"The answer is {round(result)}")
elif operator == "*":
    result = first_num * second_num
    print(f"The answer is {round(result)}")
else:
    print("Not valid operator or number. Please try again")