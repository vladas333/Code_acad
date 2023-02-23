# Create 5 list of  5 words and generate 5 random diferent words for 5 different leters. 
# (A word must the size between 5 and 15 letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.

# gyveno karta nykstukas su kepure
# mazas mazas medis auga miske
# zalia zole kuri yra pjaunama
# varztas medvarstis sraigtas ir namas
# baltas popieriaus lapas suristas virvele

import random

list_one = str("gyveno karta nykstukas su kepure").split()
list_two = str("mazas mazas medis auga miske").split()
list_three = str("zalia zole kuri yra pjaunama").split()
list_four = str("varztas medvarstis sraigtas ir namas").split()
list_five = str("baltas popieriaus lapas suristas virvele").split()

tmp_list = list_one + list_two + list_three +  list_four + list_five
print(tmp_list)
x = 0

