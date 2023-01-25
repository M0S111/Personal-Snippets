ordz = list(range(0, 14))

for n in ordz:
    if n == 0:
        print(str(n))
    elif n == 1:
        print(str(n) + "st")
    elif n == 2:
        print(str(n) + "nd")
    elif n == 3:
        print(str(n) + "rd")
    else:
        print(str(n) + "th")
