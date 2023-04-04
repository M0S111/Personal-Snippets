def sumSeries(n = int(input("Write number to sum from.\n"))):
    s = n #add first number to sum
    while n > 1:
        z = n-1 #z is 1 less than current value of n
        s += z #add z(n-1) to sum
        n -= 1 #decrement n
    return print(s)

sumSeries()


def sumSeriesRe(n = int(input("Write number to sum from recursively.\n"))):
    s = n #add first number to sum
    if n == 1: #base case
        return 1
    else:
        return s + sumSeriesRe(n-1)
    '''recursive case where series sum of 1 less than input n is
        added (summarized and assigned) to sum variable'''

x = sumSeriesRe()
print(x)
