#     6. Write a recursive function to print out the digits of a number in English.
#        For example, if the number is 153, the output should be "One Five Three."
#        See the hint from the previous problem for help on how this might be
#        done.

class BaseConversion:
    def __init__(self, num, base):
        self.list = []
        self.num = num
        self.base = base
        self.makeList()

    def makeList(self):
        digit = self.num % self.base
        self.list.append(digit)
        self.num = self.num // self.base

        if self.num < self.base:
            digit = self.num
            self.num = 0
            self.list.append(digit)
        else:
            self.makeList()

    def getDigits(self):
        self.list.reverse()
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        newList = []
        for num in self.list:
            num = digits[num]
            newList.append(num)
        str1 = ' '.join(newList)
        return str1

list = BaseConversion(153,10)
newList = list.getDigits()

print(newList)

