###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     mytuple = (r, g, b)
#     rgb_colors.append(mytuple)
# print(rgb_colors)
import turtle
import random
from turtle import Turtle, Screen
from webcolors import rgb_to_name
from my_color_coverter import convert_rgb_to_names
my_color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
                 (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
                 (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                 (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# color_name = rgb_to_name((202, 164, 110), spec='css3')
# def func_color():
#     for color in my_color_list:
#         color_name = convert_rgb_to_names(color)
#
#     print(color_name)
#     return color_name

def func_color1():
    color_name1 = convert_rgb_to_names(random.choice(my_color_list))
    return color_name1
tim = Turtle()
screen = Screen()
print(screen.colormode(255))
screen.screensize(400,300)
tim.speed()
turtle.setworldcoordinates(0, 0, 20, 20)
for _ in range(10):
    for j in range(10):
        # tim.dot(20, func_color1())
        tim.dot(20, random.choice(my_color_list))
        tim.penup()
        tim.forward(2)
    tim.backward(10 * 2)
    tim.left(90)
    tim.forward(2)
    tim.right(90)


# screen.setworldcoordinates(-50, -7.5, 50, 7.5)
# for _ in range(72):
#     tim.left(10)






# turtle.setup(width=_CFG["width"], height=_CFG["height"], startx=_CFG["leftright"], starty=_CFG["topbottom"])¶
screen.exitonclick()