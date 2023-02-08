#deeper list print

countrys_and_capitals = {
    'Lithuania' : 'Vilnius',
    'Poland' : 'Warsaw',
    'Latvia' :{
        'capital' : 'Riga',
        'population' : 2000000,
        'rich': 'very'
    }
}
# print(f"population:  {countrys_and_capitals['Latvia']['population']}")
# print(f"capital:  {countrys_and_capitals['Latvia']['capital']}")
#--------------------------------------------------------------------------

# print(list(countrys_and_capitals.items()))
# #prints al items in lists

#  print(list(countrys_and_capitals.keys()))
#  #show keys (surnames)of lists

#my_list = list(countrys_and_capitals.values())
#list for use

# print(list(countrys_and_capitals.values()))


# Delete lists element 
# print(countrys_and_capitals)
# countrys_and_capitals.pop('Latvia')
# print(countrys_and_capitals)
# Delete lists element

# #add element
# print(countrys_and_capitals)
# new_country = {'Spain': 'Madrid', 'France': 'Paris'}
# # countrys_and_capitals {'Spaint' : 'Madris'}
# countrys_and_capitals.update(new_country)
# print(countrys_and_capitals)
# #-----------------------------------

# my_set = {1, 2, 3, 4, 5}
# print(my_set)