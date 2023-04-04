from math import sqrt as sq

def prime(prime = input("State your range. ")):
    
    prime=int(prime)
    
    rng=range(0,prime)

    prime_pos=[]

    prime_neg=[]
    
    for n in rng:

        if (n%2==0) & (sq(n) != type(float)):
            prime_neg.append(n)
            
        else:
            prime_pos.append(n)
            

    prime_pos.insert(1,2)
    prime_neg.remove(2)
    prime_neg.remove(0)

    print("These numbers aren't prime:",prime_neg)
    print("\nThese numbers are prime:",prime_pos)




prime()



    










    
    
