def calc():
    #float can take a whole and decimal just incase 

    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # operation loop
    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "/":
        # Check for division by zero
        if num_2 == 0:
            return "Error! Division by zero."
        result = num_1 / num_2
    else:
        return "Invalid operation. Please enter one of +, -, *, /."

    # Print the result
    print(f"{num_1} {operation} {num_2} = {result}")

print(calc())
