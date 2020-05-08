# Chapter 8
## Programming Exercises

#   1. The Fibonacci sequence starts 1, 1, 2, 3, 5, 8, . . .. Each number in the sequence
#     (after the first two) is the sum of the previous two. Write a program
#     that computes and outputs the nth Fibonacci number, where n is a
#     value entered by the user.

import  inflect
p = inflect.engine()

def main():
    n = eval(input("Your choice of the n Fibonacci number is: "))
    count = 0
    x = 1
    y = 0

    while count < n:
        count = count + 1
        z = x + y
        x = y
        y = z
    print("The {0} Fibonacci number is {1}.".format(p.ordinal(n), z))

main()


# For the very first problem, I elected the first question of this chapter as well as a warm-up question for myself.
# I was asked to obtained a user input for a random whole number which represents the nth Fibonacci number.
# Fibonacci sequence starts from 1 and evey number after is the sum of the previous ones. Import inflect.engine first,
# a package that can be convert nums to text, I belive. Then ask for an input of n, set up the base of counter, and x as
# the first number 1, y as the second. If n is equal to or larger than 1, the counter starts to accumulate, and set up z
# which is equal to the sum of previous two numbers. Finally print z which is the result.




