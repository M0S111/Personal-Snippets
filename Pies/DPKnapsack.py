def sackRep(C,items,values):

    knap = [0]*(C+1)

    for c in range(C+1):
        for i in items:
            if i <= c:
                val = knap[c - i] + values[items.index(i)]
                knap[c] = max(knap[c],val)

    return knap[C]

print(sackRep(10,[6,3,4,2],[30,14,16,9]))


def sackNoRep(C, items, values):
    n = len(items)
    knap = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, C + 1):
            knap[i][c] = knap[i - 1][c]
            if items[i - 1] <= c:
                val = knap[i - 1][c - items[i - 1]] + values[i - 1]
                knap[i][c] = max(knap[i][c], val)
                

    return knap[n][C]

print(sackNoRep(10,[6,3,4,2],[30,14,16,9]))

def maxW(C, items):
    n = len(items)
    knap = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, C + 1):
            knap[i][c] = knap[i - 1][c]
            if items[i - 1] <= c:
                val = knap[i - 1][c - items[i - 1]] + items[i - 1]
                knap[i][c] = max(knap[i][c], val)
                

    return knap[n][C]

print(maxW(19,[9,1,8]))
