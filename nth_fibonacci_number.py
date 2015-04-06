#O(n) solution
def fibo(n):
    fib0 = 0
    fib1 = 1
    fib = 0
    for i in xrange(2, n):
        fib = fib0 + fib1
        fib0 = fib1
        fib1 = fib
        print fib
    return fib

print fibo(10)
#There is a O(logn) solution using matrix multiplication.
