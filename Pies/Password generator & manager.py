from random import randint as rr

#import json

from passgenpart import *

from kryptor import pasNcrypt

count = 0

fn = r'C:\Users\Abid Sheri\Desktop\Pies\pword.txt'

with open(fn, 'r') as f:

    see = input("\nWould you like to view stored passwords?(y/n) ")

    if see.lower() == 'y':

        for line in f:

            print(line)

            count += 1

go = input("\nDo you want to assign some passwords?(y/n) ")

if go.lower() == 'y':
    entry = True
else:
    entry = False


passlock = {}

while entry:

    site = input("\nEnter new site name. ")

    if site.startswith('www.') or site.startswith('http://') or site.startswith('https://'):

        ask = input("\nWould you like to assign your own password?(y/n) ")

    else:
        print("Invalid site name. Try again. ")
        continue

    if ask.lower() == 'y':

        p = ''

        while len(p) < 8:

            p = input("\nEnter new password for site account. Should be 8 characters long. ")

            aid = input("\nDo you need help?(y/n) ")

            if aid.lower() == 'y':
                p = passgen_p(p)
                break

        passlock[site] = p

        prompt = input("\nDo you want to assign another password?(y/n) ")

        if prompt.lower() == 'n':
            entry = False
    else:
        pas = passgen()
        passlock[site] = pas
        prompt = input("\nDo you want to assign another password?(y/n) ")

        if prompt.lower() == 'n':
            entry = False

if len(passlock) != 0:

    with open(fn,'a') as f:

        for s, p in passlock.items():

            count += 1
            p = pasNcrypt(p)
            pastr = '\n'+ str(count) + '. ' + p + ' for the site ' + s
            f.write(pastr)
        


print('\nYour passwords are:')
for s, p in passlock.items():
    print('\n', p, 'for the site', s)

if go.lower() == 'n':
    print("\nYou didn't assign any new passwords.")
