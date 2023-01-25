import turtle

wn = turtle.Screen()
b_color=input("Enter screen color")
wn.bgcolor(b_color)

jax=turtle.Turtle()
t_color=input("Enter pen color")
jax.color(t_color)

f_color=input("Enter fill color")
jax.fillcolor(f_color)

assign_len=input("Enter length of sides")
len_fin=int(assign_len)

user_range=input("Enter sides of polygon")
range_real=int(user_range)
for i in range(range_real):
    jax.forward(len_fin)
    if range_real<7:
        jax.left(45)
    else:
        jax.left(70)
        
wn.exitonclick()
