def cal():
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
    op = input("Please insert the operation you want to perform (+,-,/,*): ")

    if op == '+':
        print("Result: ",num1+num2)
    elif op == '-':
        print("Result: ", num1 - num2)
    elif op == '*':
        print("Result: ", num1 * num2)
    elif op == '/':
        print("Result: ", num1 / num2)
    else:
        print("Invalid operator, pls try again.")
