def digit_product(x):
    
    if x < 10:
        return x
    
    else:
        return x%10 * digit_product(x//10)


def persistence(n):
    
    count = 0
    
    if n < 10:
        return 0
    
    else:
        count += 1
        return count + persistence(digit_product(n))


print(persistence(223))
