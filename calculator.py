"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def validation():
    user_input = input("Enter input:")
    tokens = user_input.split()
    
    while True: 
        if tokens[0] != '+' and tokens[0] != '-' and tokens[0] != '*' and tokens[0] != '/' and tokens[0] != 'square' and tokens[0] != 'cube' and tokens[0] != 'pow' and tokens[0] != 'mod' and tokens[0] != 'q':
            print("Please enter proper command (+, -, *, /, square, cube, pow, mod )")
            user_input = input("Re-Enter input:")
            tokens = user_input.split()
        else:
            break

    
    if len(tokens)<3:
        while True:
                if tokens[0] != '+' and tokens[0] != '-' and tokens[0] != '*' and tokens[0] != '/' and tokens[0] != 'square' and tokens[0] != 'cube' and tokens[0] != 'pow' and tokens[0] != 'mod' and tokens[0] != 'q':
                    print("Please enter proper command (+, -, *, /, square, cube, pow, mod )")
                    user_input = input("Re-Enter input:")
                    tokens = user_input.split()
                if tokens[0] == 'q':
                        return tokens
                if not tokens[1].isdigit():
                    print("Please use a number")
                    user_input = input("Re-enter input:")
                    tokens = user_input.split()
                    
                else:
                    break

    if len(tokens)>2:
        while True:
            if tokens[0] != '+' and tokens[0] != '-' and tokens[0] != '*' and tokens[0] != '/' and tokens[0] != 'square' and tokens[0] != 'cube' and tokens[0] != 'pow' and tokens[0] != 'mod' and tokens[0] != 'q':
                    print("Please enter proper command (+, -, *, /, square, cube, pow, mod )")
                    user_input = input("Re-Enter input:")
                    tokens = user_input.split()
            if tokens[0] == 'q':
                        return tokens      
            if not tokens[1].isdigit() or not tokens[2].isdigit():
                print("Please use a number")
                user_input = input("Re-enter input:")
                tokens = user_input.split()
            else:
                break
    
    return tokens


while True:

    tokens= validation()
    # user_input = input("Enter input:")
    # tokens = user_input.split()
    
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


