def calculator(num1, num2, operator):
    if operator == '+':
        print(f"Result: {num1 + num2}")
        return (num1+num2)
    elif operator == '-':
        print(f"Result: {num1 - num2}")
        return (num1-num2)
    elif operator == '*':
        print(f"Result: {num1 * num2}")
        return (num1*num2)
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"Result: {num1 / num2}")
            return (num1 / num2)
    else:
        print("Invalid operator")

if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        calculator(num1, num2, operator)

    except ValueError:
        print("Invalid input: Please enter numerical values.")

# Poop