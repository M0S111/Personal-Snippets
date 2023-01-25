from math import sqrt as sq

def prime(prime):
    
    prime=int(prime)
    
    rng=range(0,prime)

    prime_pos=[]

    prime_neg=[]

    odd=[]
    
    for n in rng:

        if n%2==0:
            prime_neg.append(n)
            
        elif sq(n) is type(float):
            prime_pos.append(n)

        else:
            odd.append(n)
            

##    prime_pos.insert(1,2)
##    prime_pos.remove(1)
##    prime_neg.remove(2)
##    prime_neg.remove(0)

    print("These numbers aren't prime:",prime_neg)
    print("\nThese numbers are prime:",prime_pos)
    print("\nThese numbers are odd:",odd)




prime(76)



    










    
    
