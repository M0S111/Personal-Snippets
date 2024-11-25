import random as rand

p = 7919
a = rand.randrange(1,p)
b = rand.randrange(0,p)

def hash_function(key):

    m = 50
    
    return (((a*key + b)% p)% m)

print(hash_function(5))
print(hash_function(5))


    
