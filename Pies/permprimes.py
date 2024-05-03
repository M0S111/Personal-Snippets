def prime(prime = input("State your range. ")):
    
    prime=int(prime)
    
    rng=range(0,prime)

    prime_pos=[]

    prime_neg=[]
    
    for n in rng:

        if n == 2:
            prime_pos.append(n)

        elif (n%2==0) or ((n**0.5)%1 == 0):
            prime_neg.append(n)

        else:
            prime_pos.append(n)

    print("These numbers aren't prime:",prime_neg)
    print("\nThese numbers are prime:",prime_pos)

prime()
