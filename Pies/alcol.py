al_cols=['green','yellow','red','blue']

al_cols.insert(1,'orange')
al_cols.pop(3)


for col in al_cols:
    if col=='green':
        print('You got 5 points, yay!')
    elif col=='blue':
        print('\nYou got 10 points, woohoo!')
    elif col=='orange':
        print('\nBonus round, yippee!')
    else:
        print('\nYou got 3 points, wee!')
    

