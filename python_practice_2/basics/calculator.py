#Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1/num2
elif operator == "*":
    result = num1 * num2
else:
    print(f"{operator} is not a valid operator")


print(f"the result is {round(result, 2)}")