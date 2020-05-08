#     7. In mathematics, Cnk denotes the number of different ways that k things
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


import sys
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
