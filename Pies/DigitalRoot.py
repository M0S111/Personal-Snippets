def digitRoot(n = input("Number: ")):

    n = int(n)

    digits = []

    c = 1

    if n < 10:
        return n

    while n > 9:

        r = (n%(10**c))

        digits.append(r/(10**(c-1)))

        n -= r

        c += 1

    return digitRoot(round(sum(digits)))

        

print(digitRoot())

