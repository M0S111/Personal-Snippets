def prime_gap(gap,start,end):

    rng = range(start,end)

    count = 0

    tmp = 0

    diff = 0

    for i in rng:

        if ((i % 2 != 0) or (i**0.5) % 1 != 0) and (i >= 2):

            tmp = i

            diff = tmp - diff

            if gap == (diff-1): count += 1

    return count

print(prime_gap(2,1,11))
