from collatz import Collatz as c

active = True

count = 0

while active:

    try:
        num = int(input("\nEnter number."))

        if type(num) == int:
            while num > 1:
                num = c(num)
                print('\n', num)
                active = False
                count += 1

        else:
            continue

    except ValueError:
        print("\nBzzt!\nInvalid argument.")

print("\n It took",count,"attempts to reduce your input.")
