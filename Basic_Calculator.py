x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

arithmetic_operation = input("Choose the math operation: (+, -, *, /)")

if arithmetic_operation == "+":
    print(x+y)
elif arithmetic_operation == "-":
    print(x-y)
elif arithmetic_operation == "*":
    print(x*y)
elif arithmetic_operation == "/":
    print(x/y)
else:
    print("This is not arithmetic_operation")
