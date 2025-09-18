# calculator_extended.py

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /, **, %, //): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print("Result:", num1 / num2)
elif op == "**":   # Exponent (Power)
    print("Result:", num1 ** num2)
elif op == "%":    # Modulus (Remainder)
    print("Result:", num1 % num2)
elif op == "//":   # Floor Division (integer division)
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print("Result:", num1 // num2)
else:
    print("Invalid operator!")
