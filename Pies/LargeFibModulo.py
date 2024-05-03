def FibLargeMod(n,m):

    p_a = [0,1]

    for i in range(2,n+1):
        p_a.append(((p_a[i-1] + p_a[i-2]) % m))

        if p_a[i-1] == 0 and p_a[i-2] == 1:
            break

    #print(p_a)

    P_per_len = (len(p_a[:-2]))

    fib_n = n % P_per_len

    a, b = 0, 1
    for _ in range(fib_n):
        a, b = b, a + b
        #print(a)

    if n > m:
        return a % m

    return p_a[-1]

print(FibLargeMod(2816213588,239))
print(FibLargeMod(239,1000))
