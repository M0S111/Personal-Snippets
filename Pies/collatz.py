def Collatz(number):
    '''Attempts Collatz procedure on integer argument'''
    if number % 2 == 0:
        a = number // 2
    else:
        a = 3 * number + 1
    return a
