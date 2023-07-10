import turtle
from random import randrange

win = turtle.Screen()

class Hertz():
	
	def __init__(self,pos,ang,size):
		
		self.pos = pos
		
		self.ang = ang
		
		self.size = size

	def make(self):
		
		pen = turtle.Turtle()

		cols = ['INDIGO','PINK','PURPLE','VIOLET','RED']

		n = len(cols)

		pen.speed(0)

		pen.width(5)

		pen.ht()

		pen.up()

		pen.goto(self.pos)

		pen.down()

		pen2 = pen.clone()

		angl = self.ang

		angl2 = angl - 180

		red_ratio = 2

		for i in range(18):
	
			if i == 17:
		
				pen.fd(self.size)
		
				pen2.fd(self.size)
		
				break
	
			pen.color(cols[randrange(n - 1)])
	
			pen2.color(pen.pencolor())
	
			angl += 15/red_ratio
	
			angl2 -= 15/red_ratio
	
			red_ratio -= .09
	
			pen.seth(angl)

			pen.fd(self.size)
	
			pen2.seth(angl2)

			pen2.fd(self.size)
				
		#pen.write('YAY!', font=("Times New Roman", 10, "italic"))
		
ang_h = 270

rad = 5

s = 1

marker = turtle.Turtle()

marker.ht()

marker.up()

marker.speed(0)
	
for n in range(80):
	
	marker.circle(rad,30,1)
	
	s += 1
	
	rad += 10
	
	p = marker.pos()

	h1 = Hertz(p,ang_h,s)
	
	ang_h += 30

	h1.make()
	
turtle.exitonclick()













#	pen2.goto(pen.position())
	
#	pen2.down()

#	pen2.color(cols[randrange(n - 1)])
	
#	pen2.circle(7)
	
#	pen2.up()