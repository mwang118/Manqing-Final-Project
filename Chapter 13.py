# Chapter 13
## Programming Exercises

#     1. Modify the recursive Fibonacci program given in this chapter so that it
#        prints tracing information. Specifically, have the function print a message
#        when it is called and when it returns. For example, the output should
#        contain lines like these:
#
#        Computing fib(4)
#        ...
#        Leaving fib(4) returning 3
#
#        Use your modified version of fib to compute fib(10) and count how
#        many times fib(3) is computed in the process.


def recFib(n):
    if n < 3:
        return 1
    else:
        print("Leaving fib({0}), returning {1}".format(n, recFib(n-1) + recFib(n - 2)))
        return  recFib(n - 1) + recFib(n - 2)

recFib(5)


#    3. A palindrome is a sentence that contains the same sequence of letters reading
#       it either forwards or backwards. A classic example is '1\.ble was I, ere
#       I saw Elba." Write a recursive function that detects whether a string is a
#       palindrome. The basic idea is to check that the first and last letters of the
#       string are the same letter; if they are, then the entire string is a palindrome
#       if everything between those letters is a palindrome.
#         There are a couple of special cases to check for. If either the first or
#        last character of the string is not a letter, you can check to see if the rest
#        of the string is a palindrome with that character removed. Also, when you
#        compare letters, make sure that you do it in a case-insensitive way.
#          Use your function in a program that prompts a user for a phrase and
#        then tells whether or not it is a palindrome. Here's another classic for
#        testing: "A man, a plan, a canal, Panama!"


def palindrome(xStr, firstRun = True):
    if firstRun == True:
        for ch in '<}{ ][>.?/:;\|+=-_),(*&^%$#@!~`':
            xStr.replace(ch, "")
        xStr = xStr.lower()

    if len(xStr) < 2:
        return  True
    elif xStr[0] == xStr[-1]:
        xStr = xStr[1: -1]
        palindrome(xStr, firstRun = False)
        return True
    else:
        return False

def main():
    xSrt = input("Type a phrase to check for palindrome status here: ")
    if palindrome(xSrt) is True:
        print("The phrase is a palindrome.")
    else:
        print("The phrase is not a palindrome.")

main()


#     4. Write and test a recursive function max to find the largest number in a list.
#        The max is the larger of the first item and the max of all the other items.


from random import  randrange

def mergeMax(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)
    while i1 < n1 and i2 < n2:
        if lst1[i1] > lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 = i1 +1
        else:
            lst3[i3] = lst2[i2]
            i2 = i2 + 1
        i3 = i3 + 1

    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 = i1 + 1
        i3 = i3 + 1

    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 = i2 + 1
        i3 = i3 + 1

def mergeSort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        mergeSort(nums1)
        mergeSort(nums2)
        mergeMax(nums1, nums2, nums)

list = []
for i in range(10000):
    list.append(randrange(1, 13085))
mergeSort(list)
print(list)


#     5. Computer scientists and mathematicians often use numbering systems other
#        than base 10. Write a program that allows a user to enter a number and a
#        base and then prints out the digits of the number in the new base. Use a
#        recursive function baseConversion(num, base) to print the digits.
#           Hint: Consider base 10. To get the rightmost digit of a base 10 number,
#        simply look at the remainder after dividing by 10. For example, 153 % 10
#        is 3. To get the remaining digits, you repeat the process on 15, which is
#        just 153 I I 10. This same process works for any base. The only problem
#        is that we get the digits in reverse order (right to left).
#           The base case for the recursion occurs when num is less than base and
#         the output is simply num. In the general case, the function (recursively)
#         prints the digits of num I I base and then prints num % base. You should
#         put a space between successive outputs, since bases greater than 10 will
#         print out with multi-character "digits." For example, baseConversion (1234,
#         16) should print 4 13 2.


def baseConversion(num, base):
    digit = num % base
    print(num, digit)
    num = num // base

    if num == 0:
        return 1
    elif num < base:
        digit = num
        num = 0
        print(num, digit)
    else:
        baseConversion(num, base)

baseConversion(153, 10)


#     6. Write a recursive function to print out the digits of a number in English.
#        For example, if the number is 153, the output should be "One Five Three."
#        See the hint from the previous problem for help on how this might be
#        done.


def init(self, num, base):
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
    return  str1

list = BaseException(153, 10)
newList = list.getDigits()

print(newList)


#     7. In mathematics, e;: denotes the number of different ways that k things
#        can be selected from among n different choices. For example, if you are
#        choosing among six desserts and are allowed to take two, the number
#        of different combinations you could choose is e􀀮. Here's one formula to
#        compute this value:
#                               en n! k =
#                                        k! (n- k) !
#         This value also gives rise to an interesting recursion:
#                          ekn -- ekn--11 + ekn -1
#         Write both an iterative and a recursive function to compute combinations
#         and compare the efficiency of your two solutions. Hints: When k = 1,
#         e;: = n and when n < k, e;: = 0.


import  sys
sys.setrecursionlimit(1000)
def factorial(n):
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    return  fact

def iterative_options(n, k):
    x = factorial(n)
    y = factorial(k) * factorial(n - k)
    return  x / y

def recursice_options(n, k):
    if k == 1:
        options = n
    elif n < k:
        options = 0
    else:
        options = recursice_options(n - 1, k - 1) + recursice_options(n - 1, k)
    return options

def main():
    print(iterative_options(72, 5))
    print(recursice_options(72, 5))

main()
