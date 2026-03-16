def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator")
    except ValueError:
        print("Invalid input: Please enter numerical values.")

calculator()
