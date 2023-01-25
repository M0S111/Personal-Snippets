import turtle            
wn = turtle.Screen()
fella = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:
   fella.color(aColor)
   fella.forward(50)
   fella.left(90)

wn.exitonclick()
