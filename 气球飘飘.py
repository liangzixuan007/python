import turtle as t
import random

t.colormode(255)
t.speed(0)

for i in range(30):
    red=random.randint(1,255)
    green=random.randint(1,255)
    blue=random.randint(1,255)
    t.color(red,green,blue)

    x=random.randint(-300,200)
    y=random.randint(-100,200)

    t.penup()
    t.goto(x,y)
    t.pendown()

    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.color('black')

    t.right(90)
    t.forward(30)
    t.left(90)

    t.hideturtle()

    
