def gcd(a,b):
    
    while b != 0:
        remainder = a%b
        a = b
        b = remainder

    return round(a)

#print(gcd(6,8))

def lcm(a,b):

    d = 0
    d = gcd(a,b)
    return round((a*b)//d)

print(lcm(226553150,1023473145))
