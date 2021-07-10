import random
import turtle
from turtle import Turtle, Screen

import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return tim.color(color)


def draw_spirograh(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(70)
        random_color()
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograh(5)














screen = Screen()
screen.exitonclick()
