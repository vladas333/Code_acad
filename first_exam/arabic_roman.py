class Arabic_to_romanic:
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

for_print = Arabic_to_romanic()
number_for = 1958
print(f"You give Arabic: {number_for} and get Romanic: {for_print.int_to_roman(number_for)}")
