def Change(n):

    cents, nickels, dimes = 0,0,0

    rem = 0

    values = {'ones':'','tens':'','hundreds':'','thousands':''}

    for k in values:

        rem = n % 10

        n -= rem

        n //= 10

        values[k] = rem

    print(values)

    if (values['ones'] == 5):
        nickels = 1
    elif (values['ones'] < 5):
        cents = values['ones']
    else:
        cents = values['ones'] % 5
        nickels = 1

    dimes = (values['tens']*1) + (values['hundreds']*10) + (values['thousands']*100)

    print(f"{cents} cents + {nickels} nickels + {dimes} dimes")

Change(3757)
