def is_prime(num = input("Enter number to check primality. ")):

    num = int(num)
    
    if num == 2:
        return True
    
    elif num < 2:
        return False
    
    r = range(2,num)
    
    for i in r:
        
        if ((num % i == 0) or (num**0.5) % 1 == 0):
            return False
    return True

print(is_prime())
