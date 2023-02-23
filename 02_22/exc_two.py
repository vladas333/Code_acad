# Write a function that moves all elements of one type to the end of the list:
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]

import logging


logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


elem_list = [1, 3, 2, 4, 4, 1]
elem = 3

def move_to_end(elem_list: int, elem):
    elem_list = [x for x in elem if x != elem] + [elem]
    return elem_list
move_to_end()

logging.info(f"First list: {elem_list(elem_list, elem)}, second list:")


# test_list.append(test_list.pop(test_list.index(5)))