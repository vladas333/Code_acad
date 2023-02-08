# x = (input("Enter 3 user inputs: ").split())

# a = int(x[0])
# b = int(x[1])
# c = int(x[2])

# print(f"A: {a}, B: {b}, C: {c}")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)