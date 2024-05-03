from random import randint as rr
import re

def Toss(Cash=int(input('How much dough do you have? ')),Stakes=int(input('Pick your stakes. '))):

        count = 0

        c = 3


        if Stakes > Cash:
                print('\nGTFO! You penniless punk!!!')
                quit()

        while Cash > 0:

                urDie = []
                dlDie = []

                for i in range(c):
                        numr = rr(1,6)
                        urDie.append(str(numr))
                        cfin0 = ', '.join(urDie)
                        cfin = ''.join(urDie)


                for i in range(c):
                        numr = rr(1,6)
                        dlDie.append(str(numr))
                        dlRoll0 = ', '.join(dlDie)
                        dlRoll = ''.join(dlDie)



                count+=1

                yi = re.compile(r'[1]')
                er = re.compile(r'[2]')
                san = re.compile(r'[3]')

                se = re.compile(r'[4]')
                wu = re.compile(r'[5]')
                liu = re.compile(r'[6]')

                roll = re.compile(r'[1-6]{2}')

                pat0 = roll.findall(cfin)
                patc = roll.findall(dlRoll)

                pat1 = yi.search(cfin)
                pat2 = er.search(cfin)
                pat3 = san.search(cfin)

                pat4 = se.search(cfin)
                pat5 = wu.search(cfin)
                pat6 = liu.search(cfin)

                if pat1 and pat2 and pat3:
                        print('\nRoll',count,': Your roll:',cfin0," Dealer's roll:",dlRoll0)
                        Cash-=(Stakes * 2)

                elif pat4 and pat5 and pat6:
                        print('\nRoll',count,': Your roll:',cfin0," Dealer's roll:",dlRoll0)
                        Cash+=(Stakes * 2)

                elif not (pat0):
                        print('\nRoll',count,': Your roll:',cfin0," Dealer's roll:",dlRoll0)
                        Cash-=Stakes

                elif (Cash >= 300000000):
                        print('!!! YOU BROKE THE BANK PLAYA !!!')
                        break
                else:
                        Cash+=Stakes

                print('Your bankroll is',str(Cash)+'. The stakes were',str(Stakes)+'.')

                Stakes+=10

        if Cash < 0:
                print('Pay up, bitch!')

Toss()
