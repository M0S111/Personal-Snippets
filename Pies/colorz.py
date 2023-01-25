import turtle

wn = turtle.Screen()

back_color=input("Enter background color")
wn.bgcolor(back_color)        

jax = turtle.Turtle()

t_color=input("Enter pen color")
jax.color(t_color)

size=input("Enter stroke width")
size_fin=int(size)
jax.pensize(size_fin)                 

jax.right(45)
jax.forward(30)
jax.left(90)
jax.forward(100)

wn.exitonclick()                
