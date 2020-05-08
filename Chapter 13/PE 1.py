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
        print("Computing fib({0}) \n... \nLeaving fib({1}), returning {2} \n".format(n, n, recFib(n-1) + recFib(n - 2)))
        return  recFib(n - 1) + recFib(n - 2)

print(recFib(10))

# All I needed to do was to add a print line in the original program. But I am not sure how to count the appearances
# of fib(3) here.






