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
        temp = input("What is the average temperature for day {} or type 'quit' to tabula data: ".format(day))
        if temp.lower() != "quit" and temp.lower() != "q":
            temp = eval(temp)
            if temp > 80:
                coolDeg += 1
            elif temp < 60:
                heatDeg += 1
            day += 1
        else:
            done = True

    print("Number of heat degree-day is {0} and number of cool degree-day is {1}."
          .format(heatDeg, coolDeg))

main()

# First, user can put in as many average temperature of each day as wants. Then I used if to filter these temperature
# and if they meet certain condition, they would be counted under certain category.
