def lcs2(a, b):
    grid = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])

    return grid[-1][-1]

#print(lcs2(list("editing"),list("distance")))

def lcs3(a,b,c):
    grid = [[[0 for _ in range(len(c)+1)] for _ in range(len(b)+1)] for _ in range(len(a)+1)]

    for i in range(1,len(a) + 1):
        for j in range(1,len(b) + 1):
            for k in range(1,len(c) + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    grid[i][j][k] = grid[i - 1][j - 1][k - 1] + 1
                else:
                    grid[i][j][k] = max(grid[i - 1][j][k], grid[i][j - 1][k], grid[i][j][k - 1])

    return grid[-1][-1][-1]

#print(lcs3(list("sin"),list("sine"),list("slope")))

def editDistance(a, b):
    grid = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    if a == b:
        return 0

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])


    return

print(editDistance(list("editing"),list("distance")))
