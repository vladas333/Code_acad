class Read_from_terminal:
    def __init__(self):
        self.select_conv: str = input("Please select which converting do (Arabic to Romanic write AR Romanic to Arabic write RA): ")
        
    def which_converter_select(self):
        if self.select_conv == "RA":
           return print("Romanic to Arabic")
        elif self.select_conv == "AR":
           return print("Arabic to Romanic")
        return print(f"try")
    
    



print_answer = Read_from_terminal()
print(print_answer.which_converter_select())
