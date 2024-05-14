def FibLargeMod(n,m): # get last digits of very large nth Fibonacci number by calculating modulo with m

    p_a = [0,1] # initialize list/vector with first 2 Fibonacci numbers

    for i in range(2,n+1): # iterate from index 2 up to and including n
        p_a.append(((p_a[i-1] + p_a[i-2]) % m)) # append remainders of all Fibonacci numbers till n

        if p_a[i-1] == 0 and p_a[i-2] == 1: # stop if Pisano period has come to end indicated by sequence beginning with 0,1
            break

    #print(p_a)

    P_per_len = (len(p_a[:-2])) # get the length of Pisano period for this calculation

    fib_n = n % P_per_len # calculate the remainder of nth number and the Pisano period's length

    a, b = 0, 1 # calculate the Fibonacci number up to that remainder
    for _ in range(fib_n):
        a, b = b, a + b
        #print(a)

    if n > m:
        return a % m # if the modulo is smaller than the nth number then return remainder of previously calculated smaller Fibonacci number

    return p_a[-1] # otherwise it's the last entry of Fibonacci list

print(FibLargeMod(2816213588,239))
print(FibLargeMod(239,1000))
