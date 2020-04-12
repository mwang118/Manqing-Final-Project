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
    print("The " + p.ordinal(n) + " Fibonacci number is " + str(z) + ".")

main()


#    3. Write a program that uses a while loop to determine how long it takes
#       for an investment to double at a given interest rate. The input will be an
#       annualized interest rate, and the output is the number of years it takes an
#       investment to double. Note: The amount of the initial investment does not
#       matter; you can use $ 1 .

def main():
    ir = eval(input("The annualized interest rate is (in %): "))
    ir = 0.01 * ir
    investment = eval(input("The initial investment is: $"))

    i = investment
    interest = 0
    years = 0

    while investment > 0.5 * i:
        years = years + 1
        interest = i * ir
        i = i + interest

    print("It takes your investment {0} years to double,"
          " and total profit (including original investment) is ${1}."
          .format(years, round(i,2)))

main()


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


#     8. The greatest common divisor (GCD) of two values can be computed using
#        Euclid's algorithm. Starting with the values m and n, we repeatedly apply
#        the formula: n, m = m , ni'.m until m is 0. At that point, n is the GCD of
#        the original m and n. Write a program that finds the GCD of two numbers
#        using this algorithm.


def main():
    m, n = eval(input("Enter 2 numbers here spearated by a comma: "))

    try:
        if m < n:
            y = n
            n = m
            m = y

        while m != 0:
            y = m
            m = n % m
            n = y
        print("The GCD is", n)

    except TypeError:
        print("The input must be numerical.")

main()


#    9. Write a program that computes the fuel efficiency of a multi-leg journey.
#       The program will first prompt for the starting odometer reading and then
#       get information about a series of legs. For each leg, the user enters the
#       current odometer reading and the amount of gas used (separated by a
#       space) . The user signals the end of the trip with a blank line. The program
#       should print out the miles per gallon achieved on each leg and the total
#       MPG for the trip.


def MPG(odom):
    count = 0
    leg = 0
    totalgas = 0
    while leg != "\n":

        leg = input(("Read the current odometer and the amount of gas (separated by space): "))
        try:
            newodom, gas = leg.split(" ")
            newodom = eval(newodom)
            gas = eval(gas)

            count = count + 1

            distance = newodom - odom
            legMPG = distance/gas
            odom = newodom
            print("You got {0}/gal on leg {1}.". format(round(legMPG,2), count))

            totalgas = totalgas/gas
        except ValueError:
            break
        return  totalgas, distance

def main():
    odom = int(input("Read the current odometer: "))
    totalgas, distance = MPG(odom)
    totalMPG = distance + totalgas
    print("The total MPG for the trip is {0}.".format(round(totalMPG,2)))
main()


#     11. Heating and cooling degree days are measures used by utility companies
#         to estimate energy requirements. If the average temperature for a day is
#         below 60, then the number of degrees below 60 is added to the heating
#         degree days. If the temperature is above 80, the amount over 80 is added
#         to the cooling degree days. Write a program that accepts a sequence of
#         average daily temperatures and computes the running total of cooling and
#         heating degree days. The program should print these two totals after all
#         the data has been processed.


def main():
    day = 1
    coolDeg = 0
    heatDeg = 0
    done = False
    while not done:
        temp = input("What is the average temperature for day" + str(day) +
                     "or quit to tabula data: ")
        if temp.lower() != "quit" and temp.lower() != "q":
            temp = eval(temp)
            if temp > 80:
                coolDeg += temp - 80
            elif temp < 60:
                heatDeg += 60 - temp
            day += 1
        else:
            done = True

    print("Number of heat degree-day {0} and number of cool degree-day {1}."
          .format(heatDeg, coolDeg))

main()
