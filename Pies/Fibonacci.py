import decimal
from decimal import Decimal


##def Fibonacci(n): # Fibonacci by recursion (slowest)
##
##    if n <= 2:
##        return 1
##    else:
##        return Fibonacci(n-2) + Fibonacci(n-1)


def Fibonacci(n): # Fibonacci using Binet's formula (fastest)
    decimal.getcontext().prec = n
    sqrt_5 = Decimal(5).sqrt()
    one = Decimal(1)


    return round(((1)/sqrt_5) * ((((one+sqrt_5)/2)**n) - (((one-sqrt_5)/2)**n)))

##def Fibonacci(n): # Fibonacci by iteration (medium)
##    a, b = 0, 1
##    for _ in range(n):
##        a, b = b, a + b
##    return a

print(Fibonacci(239))
