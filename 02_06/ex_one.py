# We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# Create one final dictionary from all those 3.

dic_one={1:10, 2:20}
dic_two={3:30, 4:40}
dic_three={5:50,6:60}

print(dic_one)
print(dic_two)
print(dic_three)

dic_one.update(dic_two)

print()
dic_one.update(dic_three)
print(f'Final list  {dic_one}')