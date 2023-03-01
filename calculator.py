"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Enter input:")
    tokens = user_input.split()
    print("---->",tokens)
    if 'q' in tokens:
        print("exit")
        break

    operator = tokens[0]
    num1 = int(tokens[1])
    if len(tokens) < 3:
        num2 =""
    else:
        num2 =int(tokens[2])

    if operator == "+":
        result = add(num1,num2)
        print(result)
    elif operator == "-":
        result = subtract(num1, num2)
        print(result)
    elif operator == "*":
        result = multiply(num1, num2)
        print(result)
    elif operator == "/":
        result = divide(num1, num2)
        print(result)
    elif operator == "square":
        result = square(num1)
        print(result)
    elif operator == "cube":
        result = cube(num1)
        print(result)
    elif operator == "pow":
        result = power(num1, num2)
        print(result)
    elif operator == "mod":
        result = mod(num1, num2)
        print(result)
