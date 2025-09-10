x = float(input("Enter First Number: "))
operator = input("Enter Operator(+, -, /, or *): ")
if operator not in ('+', '-', '/', '*'):
    print("Invalid Operator")
y = float(input("Enter Second Number: "))
if operator == "+":
    result = x + y
    print(f"{x} + {y} = {result}")
elif operator == "-":
    result = x - y
    print(f"{x} - {y} = {result}")
elif operator == "*":
    result = x * y
    print(f"{x} * {y} = {result}")
elif operator == "/":
    if y != 0:
        result = x / y
        print(f"{x} / {y} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
#Create a simple calculator program and prompts for 2 operands and an operator, then calculates the result.
#Prompt for the first operand (either integer or floating point)
#Prompt for a operator, where:If a valid operator is entered, display the first number, the operand, the second number, an equals sign, and the result of the calculation
# If an invalid operator is entered, then display "Invalid Operator" (Do not display an invalid calculation)