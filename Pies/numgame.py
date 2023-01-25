# This is a guess the number game.

from random import randint as ri

secretNumber = ri(1, 20)
print('I am thinking of a number between 1 and 20.')

gu_num = 6

while gu_num > 0:
    
    g_s=str(gu_num)
    
    guess = int(input('You have '+g_s+' guesses left \nTake a guess. '))
    
    gu_num-=1
        
    if guess < secretNumber:
        print('\nYour guess is too low.')
    elif guess > secretNumber:
        print('\nYour guess is too high.')
    else:
        break 

loop_count=6-gu_num

if guess == secretNumber:
    print('\nGood job! You guessed my number in ' + str(loop_count) + ' guess/es!')
else:
    print('\nNope. The number I was thinking of was ' + str(secretNumber))
