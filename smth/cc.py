class Lab1:
    def __init__(self):
        self.num = input("Please enter a number: ")

    def sumNum(self):
        return sum(int(digit) for digit in self.num)

    def reverseNums(self):
        return self.num[::-1]

    def getList(self):
        return list(self.num)

mynum = Lab1()
print(mynum.sumNum())
print(mynum.reverseNums())
print(mynum.getList())