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

# This one is more close to daily life. I were to provided some base investment and interest rate. Using while loop as
# the prompt indicates, I set up two bases first, and stop the loop when investment doubles.
