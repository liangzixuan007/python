import random
import turtle as t
t.speed(0)
t.bgcolor("black")
col=["red","blue","yellow","green","white"]

def liang():
    t.penup()
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    t.setpos(x,y)
    t.pendown()
    c=random.choice(col)
    t.fillcolor(c)
    t.begin_fill()
    s=random.randint(30,50)
    for i in range(5):
       t.forward(s)
       t.left(144)
    t.end_fill()


for i in range(20):
  liang()

t.hideturtle
