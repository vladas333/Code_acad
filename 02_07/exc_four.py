#Write a small calculator application, 
# that allows user to enter two numbers and a symbol, 
# given and then do the operation and print an answer.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# oper_symbol = str(input("Enter which operation ( + - / * ) you would like to do: "))

# if oper_symbol == "+":
#     c = a + b
#     print(f"{a} {oper_symbol} {b} = {c}")
# elif oper_symbol == "-":
#     c = a - b
#     print(f"{a} {oper_symbol} {b} = {c}")
# elif oper_symbol == "/":
#     c = a / b
#     print(f"{a} {oper_symbol} {b} = {c}")
# elif oper_symbol == "*":
#     c = a * b
#     print(f"{a} {oper_symbol} {b} = {c}")
# else:
#     print("Too small calculator!")

oper_symbol = input("Please write your equation seperated by space: ").split()

a = int(oper_symbol[0])
x = oper_symbol[1]
b = int(oper_symbol[2])

#Operation check 31 and 33 lines
operation_list = ["+", "-", "*", "/"]

if x in operation_list:
    if x == "+":
       c = a + b
    elif x == "-":
      c = a - b
    elif x == "*":
       c = a * b
    elif x == "/":
       c = a / b
# else:
#     print("Too small calculator!")

    print(f"{a} {x} {b} = {a + b}")
