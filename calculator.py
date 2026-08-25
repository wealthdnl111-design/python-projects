def calculator():
    while True:
        num1_input = input("Enter the first number: ")
        try:
            num1 = float(num1_input)
        except ValueError:
            print(f"'{num1_input}' is not a valid number.")
            continue

        operator = input("Enter an operator (+ - * /): ")

        num2_input = input("Enter the second number: ")
        try:
            num2 = float(num2_input)
        except ValueError:
            print(f"'{num2_input}' is not a valid number.")
            continue

        if operator == "+":
            print(num1 + num2)
        if operator == "-":
            print(num1 - num2)
        if operator == "*":
            print(num1 * num2)
        if operator == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(num1 / num2)
        break

calculator()