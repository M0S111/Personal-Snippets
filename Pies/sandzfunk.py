def sando(crust, *fillings):
    if crust == True:
        crust = 'on'
    else:
        crust = 'off'
    print('\nYou prefer the crust ' + crust + ' with the following fillings:')
    for i in fillings:
        print('- ' + i)


sando('o', 'ham', 'lettuce', 'mayo')

sando(True, 'tuna', 'celery', 'tomatoes')

sando('l', 'turkey', 'asparagus', 'mustard')
