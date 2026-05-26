# Simple CLI Calculator

print("Simple Calculator")
print("Operations: +  -  *  /")

try:
    # Take user input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid operator!")

    # Display result for other operations
    if operator in ["+", "-", "*"]:
        print("Result:", result)

# Handle invalid number input
except ValueError:
    print("Invalid input! Please enter numeric values.")