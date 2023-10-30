# Main functions (input)
def main():
    user_input = input("Enter your operation: ")

    # Split the values(3)
    values = user_input.split()

    # Naming the variables
    if len(values) >= 3:
        num1 = values[0]
        op = values[1]
        num2 = values[2]

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
    else:
        print("SYNTAX ERROR")
        return main()


# Calling the main function
main()
