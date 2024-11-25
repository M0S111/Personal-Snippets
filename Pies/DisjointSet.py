class DisjointSet:
    def __init__(self, n):
        self.parents = [-1] * n  # Initialize each node to be its own parent with size -1

    def Find(self, i):
        if self.parents[i] < 0:
            return i
        self.parents[i] = self.Find(self.parents[i])
        return self.parents[i]

    def Union(self, i, j):
        i_id = self.Find(i)
        j_id = self.Find(j)

        if i_id == j_id:
            return

        # Union by size
        if self.parents[i_id] < self.parents[j_id]:  # i_id has more members
            self.parents[i_id] += self.parents[j_id]  # Update size
            self.parents[j_id] = i_id  # Make j_id a child of i_id
        else:
            self.parents[j_id] += self.parents[i_id]  # Update size
            self.parents[i_id] = j_id  # Make i_id a child of j_id

# Example usage
mySet = DisjointSet(6)
mySet.Union(1, 2)
mySet.Union(2, 3)
mySet.Union(4, 5)
mySet.Union(2, 5)

print(mySet.parents)
print(mySet.Find(4))
