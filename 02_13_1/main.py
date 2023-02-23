# squares = []
# for number in range(10):
#     print(number)
#     if number == 5:
#         squares.append(number * number)
# print(f"first: {squares}")


# squares = [number * number for number in range(10)]
# print(f"first: {squares}")

# def add_smth (nr: int):
#     return nr ** nr

#----------------------------------------------
#5 word list and print all name length is more then 5
# name_list = ["Tomas", "Aleksas", "Jonas", "Vytautas", "Algis"]

# names = []

# for name in name_list:
#     if len(names) >= 5:
#         name.append(names)
# print(f"Name list one: {names}")

#------------------------------------------
# create dictionary
# my_smth = {
#     'Alpha': 1,
#     'Beta': 2,
# }

# squares = {i : i * i for i in range(10) if i <= 6}
# print(squares)

#Create a dictionary with 5 kay:value pairs, Keys must be strings, values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)

# my_dict = {
#     "Name1" : 12,
#     "Name2" : 15,
#     "Name3" : 23,
#     "Name4" : 34,
#     "Name5" : 48,
# }

# print(f"OLD dict: {my_dict}")
# # Convert dictionary keys to lowercase
# my_dict2 =  {key.upper(): int(str(val)[::-1]) for key, val in my_dict.items()}
# # my_dict2 =  {
# #     my_dict(keys).upper(): int(str(key)[::-1] for my_dict, key in my_dict.items())}
# # apsukti a = '45'
# # print (a[::-1])
# # Print the result
# print(my_dict2)

#--------------------------------------
# make a dictonary
name_list = {"Tomas", "Aleksas", "Jonas", "Vytautas", "Algis"}
new_list2 = []

for index, index_name in enumerate(name_list, start=1):
    new_list2[index] = index_name
print(f"New2: {new_list2}")

print()
my_new = {index:name for index, name in enumerate(name_list, start=1)}
print(f"New2: {my_new}")

# name_list_a = {for index, index_name in enumerate(name_list, start=1)}
# print(name_list_a)


#-------------------------------------------------
# def even_items(numbers: list):
#     return [v for i, v in enumerate(numbers, start=1) if not i % 2]

# seq = list(range(1,11))

# print(even_items(seq))


