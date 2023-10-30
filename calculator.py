# Main function (input)
def main():
    user_input = input(
        "Enter your operation ('+' for Addition, '-' for Subtraction, '*' for Multiplication,\n'/' for Division, '%' for Modulus, '**' for Exponentiation and '//' for Floor division): "
    )

    # Split the values(3)
    values = user_input.split()

    # Check if there are exactly 3 values
    if len(values) != 3:
        print("SYNTAX ERROR")
        return main()

    # Naming the variables
    num1 = values[0]
    op = values[1]
    num2 = values[2]

    # Check if num1 and num2 are valid numbers
    if not num1.isdigit() or not num2.isdigit():
        print("ERROR. Both number 1 and number 2 should be numbers.")
        return main()

    # Convert the variables to int(num1 and num2)
    num1 = int(num1)
    num2 = int(num2)

    # The math
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        if num2 == 0:
            print("ERROR (Division by zero not allowed)")
            return main()
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "%":
        print(num1 % num2)
    elif op == "**":
        print(num1**num2)
    else:
        print("SYNTAX ERROR")
        return main()


# Calling the main function
main()
