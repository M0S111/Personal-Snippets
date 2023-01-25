import re
import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
from random import randint as rr
from copy import copy


class gameToss(App):
	

	def build(self):
		
		self.layout = GridLayout(rows=3, padding=10)
	
		self.layout.add_widget(Label(text="How much dough do you have?"))
		self.Cash = TextInput(multiline=False, cursor_blink=True)
		self.kash = int(self.Cash.text)
		self.layout.add_widget(self.Cash)
	
		self.layout.add_widget(Label(text="Pick your stakes."))
		self.Stakes = TextInput(multiline=False, cursor_blink=True)
		self.steax = int(self.Stakes.text)
		self.layout.add_widget(self.Stakes)
	
		self.button = Button(text="ROLL!")
	
		self.layout.add_widget(self.button)
	
		self.button.bind(on_press=self.onButtonPress)
	
		return self.layout		
	
	def onButtonPress(self, button):

		layout = GridLayout(cols=1, padding=10)

		if self.kash < self.steax:
			expcatch = Label(text="GTFO! You penniless punk!!!")
			layout.add_widget(expcatch)
			
		while self.kash > 0:


			chin = []
	
			comprc = 0
			comprd = 0
	
			for i in range(c):
				numr = rr(1, 6)
				chin.append(str(numr))
				cfin0 = ', '.join(chin)
				cfin = ''.join(chin)
				comprc += numr
	
			for i in range(c):
				numr = rr(1, 6)
				comprd += numr
	
			count += 1
	
			yi = re.compile(r'[1]')
			er = re.compile(r'[2]')
			san = re.compile(r'[3]')
	
			se = re.compile(r'[4]')
			wu = re.compile(r'[5]')
			liu = re.compile(r'[6]')
	
			pin = re.compile(r'[1]{3}')
	
			pat0 = pin.findall(cfin)
	
			pat1 = yi.search(cfin)
			pat2 = er.search(cfin)
			pat3 = san.search(cfin)
	
			pat4 = se.search(cfin)
			pat5 = wu.search(cfin)
			pat6 = liu.search(cfin)
	
			if pat1 and pat2 and pat3:
				scen1 = Label(text='\nRoll', count, text=':', cfin0, text='You just lost double chump!')
				self.kash -= (self.steax * 2)
				layout.add_widget(scen1)
	
			elif pat4 and pat5 and pat6:
				scen2 = Label(text='\nRoll', count, text=':', cfin0, text='!JACKPOT! Jack!')
				self.kash *= self.steax
				layout.add_widget(scen2)
	
			elif pat0:
				scen3 = Label(text='\nRoll', count, text=':', cfin0, text='!JACKPOT! Jack!')
				self.kash *= self.steax
				layout.add_widget(scen3)
	
			elif sel >= 300000000:
				scenfin = Label(text='!!! YOU BROKE THE BANK PLAYA !!!')
				layout.add_widget(scenfin)
				break
	
			elif comprc < comprd:
				scennorm = Label(text='\nRoll', count, text=':', cfin0)
				self.kash -= self.steax
				layout.add_widget(scennorm)
	
			else:
				scenwin = Label(text='\nRoll', count, text=':', cfin0)
				sel += self.steax
				layout.add_widget(scenwin)
	
			info1 = Label(text='Your bankroll is', str(sel) + text='. The stakes were', str(Stakes) + text='.')
			
			layout.add_widget(info1)
	
			info2 = Label(text='Your total for this roll:', comprc)
			
			layout.add_widget(info2)
	
			info3 = Label(text='Dealer\'s total for this roll:', comprd)
			
			layout.add_widget(info3)
	
			del chin
	
			self.steax += 10
	
		if self.kash < 0:
			print('Pay up, bitch!')

		closeButton = Button(text="I get it.")

		layout.add_widget(closeButton)

		# Instantiate the modal popup and display

		popup = Popup(title='Here we go!!!', content=layout)

				# content=(Label(text='This is a demo pop-up')))

		popup.open()

		# Attach close button press with popup.dismiss action

		closeButton.bind(on_press=popup.dismiss)


if __name__ == '__main__':
	gameToss().run()
	
	
		#count = 0
	
		#c = 3
	
		#if Stakes > Cash:
			#print('\nGTFO! You penniless punk!!!')
			#return
	
		#while Cash > 0:
	
			#chin = []
	
			#comprc = 0
			#comprd = 0
	
			#for i in range(c):
				#numr = rr(1, 6)
				#chin.append(str(numr))
				#cfin0 = ', '.join(chin)
				#cfin = ''.join(chin)
				#comprc += numr
	
			#for i in range(c):
				#numr = rr(1, 6)
				#comprd += numr
	
			#count += 1
	
			#yi = re.compile(r'[1]')
			#er = re.compile(r'[2]')
			#san = re.compile(r'[3]')
	
			#se = re.compile(r'[4]')
			#wu = re.compile(r'[5]')
			#liu = re.compile(r'[6]')
	
			#pin = re.compile(r'[1]{3}')
	
			#pat0 = pin.findall(cfin)
	
			#pat1 = yi.search(cfin)
			#pat2 = er.search(cfin)
			#pat3 = san.search(cfin)
	
			#pat4 = se.search(cfin)
			#pat5 = wu.search(cfin)
			#pat6 = liu.search(cfin)
	
			#if pat1 and pat2 and pat3:
				#print('\nRoll', count, ':', cfin0, '\nYou just lost double chump!')
				#Cash -= (Stakes * 2)
	
			#elif pat4 and pat5 and pat6:
				#print('\nRoll', count, ':', cfin0, '\n!JACKPOT! Jack!')
				#Cash *= Stakes
	
			#elif pat0:
				#print('\nRoll', count, ':', cfin0, '\n!JACKPOT! Jack!')
				#Cash *= Stakes
	
			#elif Cash >= 300000000:
				#print('!!! YOU BROKE THE BANK PLAYA !!!')
				#break
	
			#elif comprc < comprd:
				#print('\nRoll', count, ':', cfin0)
				#Cash -= Stakes
	
			#else:
				#print('\nRoll', count, ':', cfin0)
				#Cash += Stakes
	
			#print('Your bankroll is', str(Cash) + '. The stakes were', str(Stakes) + '.')
	
			#print('Your total for this roll:', comprc)
	
			#print('Dealer\'s total for this roll:', comprd)
	
			#del chin
	
			#Stakes += 10
	
		#if Cash < 0:
			#print('Pay up, bitch!')


#Toss()
