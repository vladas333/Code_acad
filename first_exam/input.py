class Read_from_terminal:
    def __init__(self):
        self.select_conv: str = input("Please select which converting do (Arabic to Romanic write AR Romanic to Arabic write RA): ")
        
    def which_converter_select(self):
        if self.select_conv == "RA":
           return print("Romanic to Arabic")
        elif self.select_conv == "AR":
           return print("Arabic to Romanic")
        return print(f"try")
    
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
                
        return answer_ar



print_answer = Read_from_terminal()
print(print_answer.which_converter_select())
