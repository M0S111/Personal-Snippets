# python3

class HashTable:
    def __init__(self,m):
        self.pointer_array = [[] for _ in range(m)]
        self.p = 1000000007
        self.x = 263
        self.m = m

    def HashFunc(self,string):
        return (sum([ord(l) * (self.x ** i) for i, l in enumerate(string)]) % self.p) % self.m


    def Insert(self,string):
        if string not in self.pointer_array[self.HashFunc(string)]:
            self.pointer_array[self.HashFunc(string)].append(string)

    def Delete(self,string):
        if string in self.pointer_array[self.HashFunc(string)]:
            self.pointer_array[self.HashFunc(string)].remove(string)

    def Search(self,string):
        if string in self.pointer_array[self.HashFunc(string)]:
            return "yes"
        return "no"

    def Print(self,idx):
        #for w in range(len(self.pointer_array[idx])-1,-1,-1):
        #for w in self.pointer_array[idx][::-1]:
            #print(w)
        return " ".join(self.pointer_array[idx][::-1])


class Query:

    def __init__(self,query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.table = HashTable(bucket_count)  # Store the HashTable instance
        self.elems = []

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == 'add':
            self.table.Insert(query.s)
        elif query.type == 'del':
            self.table.Delete(query.s)
        elif query.type == 'find':
            self.elems.append(self.table.Search(query.s))
        elif query.type == 'check':
            self.elems.append(self.table.Print(query.ind))

        return self.elems

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

    def write_chain(self):
        print('\n'.join(self.elems))

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
    proc.write_chain()
