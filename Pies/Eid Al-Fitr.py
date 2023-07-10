import turtle
from random import randrange


class Cres():
	
	def __init__(self,pos,ang,size):
		
		self.pos = pos
		
		self.ang = ang
		
		self.size = size

	def make(self):
		
		marker = turtle.Turtle()
		
		marker.shape('circle')

		marker.up()
		
		#marker.ht()

		marker.color('light yellow')

		marker.width(1)

		marker.speed(0)
		
		pen = turtle.Turtle()
		
		screen = turtle.Screen()
		
		sc_size = screen.screensize()
		
		screen.bgcolor('BLACK')

		cols = ['LIGHT YELLOW','WHITE']

		n = len(cols)

		pen.speed(0)

		pen.width(5)

		pen.ht()

		pen.up()

		pen.goto(self.pos)
		
		init_pos = pen.xcor()

		pen.down()
		
		pen.begin_fill()


		angl = self.ang

		red_ratio = 3

		for i in range(25):
	
			if i == 24:
		
				pen.fd(self.size)
		
				break
	
			pen.color(cols[randrange(n)])

	
			angl += -15/red_ratio
	
			red_ratio -= 0.03
	
			pen.seth(angl)

			pen.fd(self.size)
			
		self.pos = pen.pos()

		pen.up()

		pen.goto(self.pos)

		pen.down()

		angl = self.ang - 300

		red_ratio = 4

		for i in range(22):
	
			if pen.xcor() == init_pos:
		
				break
	
			pen.color(cols[randrange(n - 1)])

			angl += 15/red_ratio
	
			red_ratio -= 0.07
	
			pen.seth(angl)

			pen.fd(self.size)
	
		pen.end_fill()
		
		pen.up()
			
		pen.home()
		
		pen.down()
				
		pen.write('Eid Mubarak', font=("Arial", 10, "italic"))
		
		count = 100
		
		while count > 0:
		
			#marker.goto(randrange(screen.window_width()),randrange(screen.window_height()))
			
			marker.goto(randrange(-700,700),randrange(-700,700))
			
			marker.down()
			
			marker.stamp()
			
			marker.up()
			
			count -= 1


ang_h = 200
	
p = (250,-500)

crescent = Cres(p,ang_h,50)

crescent.make()
	
turtle.exitonclick()













#	pen2.goto(pen.position())
	
#	pen2.down()

#	pen2.color(cols[randrange(n - 1)])
	
#	pen2.circle(7)
	
#	pen2.up()