from turtle import Turtle, Screen
import random

colors = ["red", "blue", "green", "orange"]
timmy = Turtle()
timmy.color("red")

x = 0
while(x < 360):
    random_color = random.choice(colors)
    timmy.color(random_color)
    timmy.left(x)
    timmy.circle(50)
    timmy.speed(100)
    x +=   1
screen = Screen()
screen.exitonclick()