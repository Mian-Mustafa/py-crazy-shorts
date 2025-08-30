import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red","orange","yellow","green","blue","purple"]

for i in range(360):
    t.color(colors[i % 6])
    t.forward(i * 2)
    t.right(59)
    
t.hideturtle()
turtle.done()