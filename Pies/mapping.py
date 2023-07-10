nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x/11, nums))

def decrement(arg):
    
    arg = arg - 1
    
    return arg

result = list(map(decrement, result))

print(result)


def factorial(x):

    if x == 1:
        
        return 1
        
    else:
    
        return x * factorial(x-1)

print(factorial(5))


from random import randint

class Rectangle: 
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(randint(0,100),randint(0,100))


print("My Rectangle's width is {0} & height is {1}".format(rect.width, rect.height))