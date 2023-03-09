from typing import Union

class Read_from_terminal:
    def __init__(self, number_for_change: int) -> Union[str, int]:
        self.select_conv: str = input("Please select which converting do (Arabic to Romanic write AR Romanic to Arabic write RA): ")
        self.number_for_chane = number_for_change
        
    def which_converter_select(self, number_for_change2: int):
        if self.select_conv == "RA":
           return print("Romanic to Arabic")
        elif self.select_conv == "AR":
           return number_for_change2 =  Arabic_to_romanic(input("Yoy select Arabic to change in Romanic. Please enter: "))
           #return print("Arabic to Romanic")
        return print(f"try")

class Arabic_to_romanic:
    def __init__(self):
        self.number_for_change: int = input("Yoy select Arabic to change in Romanic. Please enter: ")
            
    def int_to_roman(self, number_for_change) -> str:
        self.number_for_change = number_for_change
        rules = [
            ("M", 1000),
            ("CM", 900),
            ("D",  500),
            ("CD", 400),
            ("C",  100),
            ("XC",  90),
            ("L",   50),
            ("XL",  40),
            ("XXX", 30),
            ("XX",  20),
            ("X",   10),
            ("IX",   9),
            ("V",    5),
            ("IV",   4),
            ("I",    1),
        ]
        
        answer_ar = ""
        for leter_for_change, number in rules:
            while number_for_change >= number:
                number_for_change -= number
                answer_ar += leter_for_change
                
        return print(f"Your answer is: {answer_ar}")

# for_print = Arabic_to_romanic()
# number_for = 1958
# print(f"You give Arabic: {number_for} and get Romanic: {for_print.int_to_roman(number_for)}")

print_answer = Read_from_terminal()
#print(print_answer.which_converter_select())