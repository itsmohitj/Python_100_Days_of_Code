import art
print(art.logo)


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multitply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {"+": add, "-": subtract, "*": multitply, "/": divide}

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation_symbol = input("Which operation would you like to perform? (+, -, *, /): ")

answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
repeat = input(f"Would you like to continue performing another operation on {answer}? (y/n): ")
while(repeat == "y"):
    num3 = float(input("Enter the next number: "))
    operation_symbol = input("Which operation would you like to perform? (+, -, *, /): ")
    num4 = answer
    answer = operations[operation_symbol](answer, num3)
    print(f"{num4} {operation_symbol} {num3} = {answer}")
    repeat = input(f"Would you like to continue performing another operation on {answer}? (y/n): ")
    if repeat != "y":
        print("Bye!!")