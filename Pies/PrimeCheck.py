from random import randint as ri


n = int(input("\nState number. "))

r = ri(1,100)

if n == 2:

    print("\nThis is a prime number.")

elif ((n % 2 == 0) and (n % r != 0)):

    print("\nThis probably isn't a prime number.")

else:

    print("\nThis probably is a prime number.")
