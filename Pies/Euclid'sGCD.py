def gcd(a,b): # apply Euclid's algo for Greatest Common Divisor of 2 integers where a > b
    
    while b != 0: # repeat till b reduces to 0
        remainder = a%b # get a modulo b (remainder)
        a = b # set smaller divisor as larger dividend
        b = remainder # set new divisor as remainder of a%b

    return round(a) # return GCD

#print(gcd(6,8))

def lcm(a,b): # algo for Least Common Multiple utilizing Eucllid's gcd algo

    d = 0 # initialize divisor
    d = gcd(a,b) # set divisor as value of GCD of inputs
    return round((a*b)//d) # return quotient of product of inputs integer divided by divisor

print(lcm(226553150,1023473145))
