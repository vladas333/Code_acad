# import time

# seconds = 1
# while True:
#     print("Zalgiris")
#     time.sleep(0.5)
#     seconds += 1
#     if seconds == 3:
#         break
# real while example
# apples = 0

# while apples <= 10:
#     print(f"Gathered apples so far: {apples}")
#     apples += 1
#----------------------------------------------------
# import sys
# names = ["Antanas", "Mindaugas"]
# #print("Consumption", sys.getsizeof(names))

# for name in names:
#     print(name)
#     print(type(name))

# for letter in "Antanas":
#     print(letter)

# my_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for _ in range(0, 5):
#     for number in my_number_list:
#         print(number)
#         if number >= 9:
#             break
#     break

# my_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in my_number_list:
#     if number ==  7:
#         continue
#     print(number)


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)