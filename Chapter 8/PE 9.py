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

# I actually struggled a lot on this one because I am not familiar with the knowledge of such area. I am not quiet sure
# what leg is. But I got something here and definitely not correct because the output is strange.
