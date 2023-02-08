# allow user to enter two numbers, print out which one is higher than the other, or are they equal?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is higher than {b}")
elif a < b:
    print(f"{a} is smaller then {b}")
else:
    print(f"{a} is equal {b}")