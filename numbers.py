# Program for a simple calculator

# Input two numbers and the operation from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

# Display the result
print(f"The result of {num1} {operator} {num2} is: {result}")
