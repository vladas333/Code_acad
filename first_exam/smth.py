class Read_from_terminal:
    def __init__(self):
        self.select_conv: str = input("Please select which converting do (*Arabic to Romanic write AR **Romanic to Arabic write RA): ")
        #self.number_for_change = self.int_to_roman()
        #self.romanic_number = self.romanic_to_arabic
        if self.select_conv == "RA" or self.select_conv == "ra":
           print(self.romanic_to_arabic(input(f"Please enter Romanic number: ")))
        #elif self.select_conv == "AR":
        elif self.select_conv == "AR" :
            self.int_to_roman()
           #return print("Arabic to Romanic")
        return print(f"Program finish!!")
        

    # def which_converter_select(self):
    #     if self.select_conv == "RA" or self.select_conv == "ra":
    #        self.romanic_to_arabic()
    #     #elif self.select_conv == "AR":
    #     else :
    #         return self.int_to_roman()
    #        #return print("Arabic to Romanic")
    #     return print(f"try")
    
    def int_to_roman(self) -> str:
        self.number_for_change: int = int(input(f"Please enter Arabic number: "))
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
            while self.number_for_change >= number:
                self.number_for_change -= number
                answer_ar += leter_for_change
                
        return print(answer_ar)
    
    def romanic_to_arabic(self, romanic_number) -> str:
        self.romanic_number = romanic_number
        convert_to_arabic = 0
        try:
            romanic_number = str(romanic_number)
            for temp_number in range(0, len(romanic_number)):
                if romanic_number[temp_number]=='I' or romanic_number[temp_number]=='i':
                    try:
                        if romanic_number[temp_number+1]=='V' or romanic_number[temp_number+1]=='X' or romanic_number[temp_number+1]=='v' or romanic_number[temp_number+1]=='x': 
                            convert_to_arabic-=1
                        else:
                            convert_to_arabic+=1
                    except:
                        convert_to_arabic+=1
                elif romanic_number[temp_number]=='V' or romanic_number[temp_number]=='v':
                    convert_to_arabic+=5
                elif romanic_number[temp_number]=='X' or romanic_number[temp_number]=='x':
                    try:
                        if romanic_number[temp_number+1]=='C' or romanic_number[temp_number+1]=='L' or romanic_number[temp_number+1]=='c' or romanic_number[temp_number+1]=='l': 
                            convert_to_arabic-=10
                        else:
                            convert_to_arabic+=10
                    except:
                        convert_to_arabic+=10
                elif romanic_number[temp_number]=='L' or romanic_number[temp_number]=='l':
                    convert_to_arabic+=50
                elif romanic_number[temp_number]=='C' or romanic_number[temp_number]=='c':
                    try:
                        if romanic_number[temp_number+1]=='M' or romanic_number[temp_number+1]=='D' or romanic_number[temp_number+1]=='m' or romanic_number[temp_number+1]=='d': 
                            convert_to_arabic-=100
                        else:
                            convert_to_arabic+=100
                    except:
                        convert_to_arabic+=100
                elif romanic_number[temp_number]=='D' or romanic_number[temp_number]=='d':
                    convert_to_arabic+=500
                elif romanic_number[temp_number]=='M' or romanic_number[temp_number]=='m':
                    convert_to_arabic+=1000
                else:
                    print("Invalid number")
        except:
            print("Invalid number")
        return convert_to_arabic



print_answer = Read_from_terminal()
#print(print_answer.which_converter_select())
