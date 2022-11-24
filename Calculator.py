def solve(num_1, num_2, operation):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*" or operation == "x":
        return num_1 * num_2
    elif operation == "/":
        return num_1 / num_2
    else:
        return "Invalid Operator"


print(solve(float(input("Enter a number: ")), float(input("Enter another number: ")), input("Enter an operation: ")))

