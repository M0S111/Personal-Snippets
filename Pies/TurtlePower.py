import turtle
from random import randrange

win = turtle.Screen()

pen = turtle.Turtle()

pen2 = turtle.Turtle()

cols = ['BLUE','BROWN','PURPLE','GREEN','RED']

r = len(cols)

rad = 30

pen.speed(0)
	
pen2.speed(0)

pen.ht()

pen2.ht()

for i in range(30):
	
	rad += 10
	
	pen.color(cols[randrange(r - 1)])
	
	pen2.color(cols[randrange(r - 1)])
	
#	pen2.circle(rad)
	
	pen2.up()

	pen.circle(rad,70)
	
	pen2.goto(pen.position())
	
	pen2.down()
	
pen.write('YAY!', font=("Times New Roman", 16, "italic"))
	
turtle.exitonclick()