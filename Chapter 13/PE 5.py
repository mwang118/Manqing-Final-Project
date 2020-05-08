#     5. Computer scientists and mathematicians often use numbering systems other
#        than base 10. Write a program that allows a user to enter a number and a
#        base and then prints out the digits of the number in the new base. Use a
#        recursive function baseConversion(num, base) to print the digits.
#           Hint: Consider base 10. To get the rightmost digit of a base 10 number,
#        simply look at the remainder after dividing by 10. For example, 153 % 10
#        is 3. To get the remaining digits, you repeat the process on 15, which is
#        just 153 // 10. This same process works for any base. The only problem
#        is that we get the digits in reverse order (right to left).
#           The base case for the recursion occurs when num is less than base and
#         the output is simply num. In the general case, the function (recursively)
#         prints the digits of num // base and then prints num % base. You should
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

baseConversion(1234, 16)

# This one is similar to Chapter 8 PE 8.
