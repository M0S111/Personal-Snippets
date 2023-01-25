active = True

while active:

    try:
        a = int(input("\nEnter value of variable a. "))
        b = int(input("\nEnter value of variable b. "))
        break

    except ValueError:
        print("\nIncorrect input. Try again.")


x = a + b

print('\nYour result:', x)
