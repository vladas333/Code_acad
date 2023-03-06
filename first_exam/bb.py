class Lab1:
    def sumNum():
         n = int(input("Please enter a three digit whole number "))
         tot=0
         while(n>0):
             dig=n%10
             tot=tot+dig
             n=n//10
         print("The total sum of digits is:",tot)

    def reverseNums():
        Number = int(input("Please Enter any Number: "))    
        Reverse = 0    
        while(Number > 0):    
             Reminder = Number %10    
             Reverse = (Reverse *10) + Reminder    
             Number = Number //10 
        print("\n Reverse of entered number is = %d" %Reverse)

    def getlist():
        n = input("Please enter a number ")
        list1 = list(n)
        print(list1)

run1 = Lab1.sumNum()
run2 = Lab1.reverseNums()
run3 = Lab1.getlist()