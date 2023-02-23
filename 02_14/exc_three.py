#Create a mini python program which would take two numbers as an input 
# and would return their sum, subtraction, division, multiplication

oper_symbol = input("Please write your equation seperated by space: ").split()

a = int(oper_symbol[0])
x = oper_symbol[1]
b = int(oper_symbol[2])


operation_list = ["+", "-", "*", "/"]

def calc(a, x, b):
    if x in operation_list:
        if x == "+":
            c = a + b
        elif x == "-":
            c = a - b
        elif x == "*":
            c = a * b
        elif x == "/":
            c = a / b
    print(f"{a} {x} {b} = {a + b}")

calc(a, x, b)