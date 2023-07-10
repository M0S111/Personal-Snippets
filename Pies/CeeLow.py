from random import randint as rr
import re

def Toss(Cash=int(input('How much dough do you have? ')),Stakes=int(input('Pick your stakes. '))):
	
	count = 0
	
	c = 3

	
	if Stakes > Cash:
		print('\nGTFO! You penniless punk!!!')
		quit()
	
	while Cash > 0:
	
		chin = []
		
		comprc = 0
		comprd = 0
	
		for i in range(c):
			numr = rr(1,6)
			chin.append(str(numr))
			cfin0 = ', '.join(chin)
			cfin = ''.join(chin)
			comprc+=numr
		
		
		for i in range(c):
			numr = rr(1,6)
			comprd+=numr
		
		
		count+=1
		
		yi = re.compile(r'[1]')
		er = re.compile(r'[2]')
		san = re.compile(r'[3]')
		
		se = re.compile(r'[4]')
		wu = re.compile(r'[5]')
		liu = re.compile(r'[6]')
		
		pin = re.compile(r'[1]{3}')
		
		pat3 = pin.findall(cfin)
		
		pat0 = yi.search(cfin)
		pat1 = er.search(cfin)
		pat2 = san.search(cfin)
		
		pat4 = se.search(cfin)
		pat5 = wu.search(cfin)
		pat6 = liu.search(cfin)
		
		if pat0 and pat1 and pat2:
			print('\nRoll',count,':',cfin0,'\nYou just lost double chump!')
			Cash-=(Stakes * 2)
			
		elif pat4 and pat5 and pat6:
			print('\nRoll',count,':',cfin0,'\n!JACKPOT! Jack!')
			Cash*=Stakes
		
		elif pat3:
			print('\nRoll',count,':',cfin0,'\n!JACKPOT! Jack!')
			Cash*=Stakes
		
		elif Cash >= 300000000:
			print('!!! YOU BROKE THE BANK PLAYA !!!')
			break
			
		elif comprc < comprd:
			print('\nRoll',count,':',cfin0)
			Cash-=Stakes
			
		else:
			print('\nRoll',count,':',cfin0)
			Cash+=Stakes
		
		print('Your bankroll is',str(Cash)+'. The stakes were',str(Stakes)+'.')
		
		print('Your total for this roll:',comprc)
		
		print('Dealer\'s total for this roll:',comprd)
		
		del chin
		
		Stakes+=10
		
	if Cash < 0:
		print('Pay up, bitch!')

Toss()
