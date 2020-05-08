#     7. The Goldbach conjecture asserts that every even number is the sum of two
#        prime numbers. Write a program that gets a number from the user, checks
#        to make sure that it is even, and then finds two prime numbers that add
#        up to the number.


import math as m

def prime(n):
    x = m.sqrt(n)
    i = 2
    while i <= x:
        value = n % i
        if value == 0:
            return None
        else:
            i = i + 1
    return n

def main():
    x = eval(input("Type in a postive number: "))
    while True:
        if x == 0:
            x = eval(input("The number must be larger than 0: "))
        elif (x % 1 != 0):
            x = eval(input("The number should be whole: "))
        elif (x < 1):
            x = eval(input("The number should be positive: "))
        elif (x % 2 != 0):
            x = eval(input("The number should be even: "))
        else:
            n = x
            break
    while n > 0:
        prime_num = prime(n)
        if prime_num != None:
            prime_2 = x - prime_num
            test = prime(prime_2)
            if test != None:
                print("{0} + {1} = {2}".format(prime_num, prime_2, x))
        n = n - 1

main()

# Import math first to do the calculation for me. I defined a function to detect what is prime number first, and asked
# some input which is positive whole even number. Then find the two prime number within it using the function.
