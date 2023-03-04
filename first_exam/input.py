# input_roman_number = int(input("Please, enter a Romanic number: "))

# if input_roman_number == 1:
#     arab_number = "I"


# output_arabic_number = arab_number


# print(f"You enter {input_roman_number}")
# print(f"Arabic number would be: {output_arabic_number}")

from typing import Union

ARABIC_TO_ROMANIC = {
    1 : "I",
    5 : "V",
    10 : "X",
    50 : "L",
    100 : "C",
    500 : "D",
    1000 : "M"
    }

# ara_to_rom = [(1000 : "M"), (500 : "D"), (100 : "C"), (50 : "L"), (10 : "X"), (5 : "V"), (1 : "I")]
# class select_which_conv_make:
#     def __init__(self):
#         self.conv_select_input = input("Please select which converting do:")

# def arabic_to_roman(slct_number: Union[int, float]):
#     romanic = ""
#     print(slct_number)
#     print(type(slct_number))
   
#     while slct_number > 0:
#         for i, r in ara_to_rom:
#             while slct_number >= i:
#                 romanic = romanic + r
#                 slct_number = slct_number - i
#     return romanic


class Read_from_terminal:
    def __init__(self, select_conv: str):
        self.select_conv: str = select_conv
        

    def Which_converter_select(self, select_conv):
        self.select_conv = input("Please select which converting do (Arabic to Romanic write AR Romanic to Arabic write RA): ")
        if select_conv == "RA":
           print("Romanic to Arabic")
        elif select_conv == "AR":
           print("Arabic to Romanic")
        return select_conv

selected = Read_from_terminal()

    
      
        






#select_conv = input("Please select which converting do (Arabic to Romanic write AR Romanic to Arabic write RA): ")
print_answer = Read_from_terminal()
print(print_answer)
# if select_conv == "RA":
#     print("Romanic to Arabic")
# elif select_conv == "AR":
#     print("Arabic to Romanic")
#     select_arabic: int = input("Enter arabic number: ")
#     print(arabic_to_roman(select_arabic))
