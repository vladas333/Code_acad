# a = 2
# b = 5

# def addition(number1, number2):
#     sum = number1 + number2
#     return sum

# #---------
# # print(number1)
# # not works because bumber1 is inside def

# c = addition(a, b)

# print(c)

#-----------------------------------------

# def even_odd(num):

#     '''
#     Returns "even" if num is even, and "odd" if num is odd.    
#     Parameters:
#         num (int): Any integer    Returns:
#         type (string): "even" if num is even; "odd" if num is odd
#     '''

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"

# number = 10

# if even_odd(number) == "even":
#     print(f"My number : {number} is even!")
# else:
#     print(f"My number: {number} is not even")

#-----------------------------------------------------------
# def check_if_exist(a=None):
#   if a:
#     return a

# #a = check_if_exist("A")

# a = check_if_exist()
# print(a)

# def find_subtraction(num1, num2):
#     '''Returns the sum of num1 and num2.'''
#     sum_nums = num1 - num2  # Finds the sum of num1 and num2
#     return sum_nums  # Returns the sum of the numbers

# print(find_subtraction(num2=5, num1=50))

#---------------------------------------------------------

def add_two_int_numbers(a: int, b: int) -> int:
  return a + b

number_1 = add_two_int_numbers(1, 50)

