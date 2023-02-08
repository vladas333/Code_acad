# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

first_name = str(input("Enter your name: "))
surname = str(input(" Enter your surname: "))
age = int(input("Enter your age: "))

if age >= 21:
    print("You are ALLOWED in Online casino")
else:
    print("You are NOT ALLOWED in Online Casino!")