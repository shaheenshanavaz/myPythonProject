import turtle
from turtle import Turtle,Screen,Shape
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")
tim.pendown()
tim.pencolor("blue")

# TODO Drawing a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# TODO Drawing all different shapes
# tim.speed(1)
turtle.colormode(255)
def random_color():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    mytuple = (r, g, b)
    return mytuple

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.pencolor(R, G, B)

# for sides in range(3, 10):
#     change_color()
#     for t in range(sides):
#         tim.right(360/sides)
#         tim.forward(80)
        # Different shapes in longer version
# tim.pencolor("yellow")
# for t in range(3):
#     tim.right(120)
#     tim.forward(80)
# tim.pencolor("orange")
# for s in range(4):
#     tim.right(90)
#     tim.forward(80)
# tim.pencolor("purple")
# for p in range(5):
#     tim.right(72)
#     tim.forward(80)
# tim.pencolor("red")
# for p in range(6):
#     tim.right(60)
#     tim.forward(80)
# tim.pencolor("blue")
# for p in range(7):
#     tim.right(51.42)
#     tim.forward(80)
# tim.pencolor("maroon")
# for p in range(8):
#     tim.right(45)
#     tim.forward(80)
# tim.pencolor("brown")
# for p in range(9):
#     tim.right(40)
#     tim.forward(80)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# TODO Random Walk
tim.pensize(5)
tim.speed(1)
# print(type(walk))
# is_ended = False
# while not is_ended:
#     num = random.randint(0,2)
#     if num == 0:
#         tim.right(90)
#     else:
#         tim.left(90)
#     tim.forward(10)
#     change_color()

# OR

moves = [0,90,180, 270]
for _ in range(40):
    tim.forward(20)
    tim.setheading(random.choice(moves))
    tim.color(random_color())














screen = Screen()
screen.exitonclick()