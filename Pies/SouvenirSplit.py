#def partition3(a):

##    grid = [0 for _ in range(len(a))]
##
##    for i in range(len(a)):
##        if grid[i] % 3 == 0:
##            grid[i] = (grid[i-1] + a[i])

import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] == sums[2]:
            return 1

    return 0

##Loop Using itertools.product:
##The outer loop iterates over all possible combinations of three values (0, 1, and 2) for each element in the input list A.
##The itertools.product(range(3), repeat=len(A)) generates all possible tuples of length len(A) where each element can be 0, 1, or 2.
##For example, if len(A) is 4, the loop will iterate through tuples like (0, 0, 0, 0), (0, 0, 0, 1), …, (2, 2, 2, 2).
##Calculating Sums:
##Inside the loop, a list called sums is initialized with three None values.
##The inner loop runs three times (for i in range(3)`):
##For each i, it calculates the sum of elements in A where the corresponding value in the tuple c is equal to i.
##The condition if c[k] == i checks whether the k-th element of c is equal to i.
##The sum is stored in the sums[i] position.

print(partition3([1,2,3,4,5,5,7,7,8,10,12,19,25]))
print(partition3([3,3,3,3]))
print(partition3([30]))
