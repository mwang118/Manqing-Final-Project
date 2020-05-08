#     8. The greatest common divisor (GCD) of two values can be computed using
#        Euclid's algorithm. Starting with the values m and n, we repeatedly apply
#        the formula: n, m = m , n%m until m is 0. At that point, n is the GCD of
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

# I remember I learnt this at elementary school. As always, I asked for input but two whole numbers at this time.
# Then defined y to temporarily represent the input. Loop over m = n%m until m == 0.
