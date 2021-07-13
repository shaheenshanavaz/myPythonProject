import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def funcforward():
    tim.forward(10)


def funcbackward():
    tim.backward(10)

mylist = [30,60,90,150,180,240,270,360]

def funccounterclockwise():
        angle = 0
        angle += 10
        tim.left(angle)
def funcclockwise():
        angle = 0
        angle += 10
        tim.right(angle)

def drawcircle():
        # tim.circle(120, extent= funcclockwise(),steps= 1)
        # else:
        #     tim.circle(129, funcclockwise)
        turtle.degrees(400.0)
        turtle.heading()

def cleardrawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.onkey(fun=funcforward, key="w")
screen.onkey(fun=funcbackward, key="s")
screen.onkeypress(fun=funccounterclockwise, key="a")
screen.onkeypress(fun=funcclockwise, key="d")
# screen.onkeypress(fun=drawcircle, key="g")
screen.onkeypress(fun=cleardrawing, key="c")
screen.listen()
screen.exitonclick()