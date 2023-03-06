class Romanic_to_arabic:
    def romanic_arabic(self, romanic_number):
        self.romanic_number = romanic_number
        convert_to_arabic=0
        try:
            romanic_number=str(romanic_number)
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
for_print_two = Romanic_to_arabic()
number_for_two = "I"
print(f"{for_print_two.romanic_arabic(number_for_two)}")
