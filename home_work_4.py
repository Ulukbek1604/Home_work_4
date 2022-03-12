import turtle
from turtle import *

cp = Turtle()
s = Screen()
"""
    screensize - это размер экрана
"""
screensize(100, 1400)
"""
    pencolor - это цвет линий
"""
cp.pencolor("#ff4040")
"""
    bgcolor - это цвет экрана
"""
s.bgcolor("black")
"""
    pensize - это размер линий
"""
cp.pensize(1)
Pyton = 0
cpp = 0
cp.speed(0)
cp.penup()
cp.goto(0, 560)
cp.pendown()

while True:
    cp.forward(Pyton)
    cp.right(cpp)
    Pyton += 3
    cpp += 1

    if cpp == 210:
        break
    cp.hideturtle()

turtle.done()
