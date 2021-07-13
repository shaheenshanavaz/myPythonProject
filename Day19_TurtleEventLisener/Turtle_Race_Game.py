import random
from turtle import Turtle, Screen, color
import random
is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color do you choose your turtle to be?")
turtle_color = ["red", "blue", "purple", "green", "yellow", "orange"]
s = 0
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-150 + s)
    all_turtles.append(new_turtle)
    s += 30

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle.hideturtle()
                turtle.setpos(x=0, y=180)
                # turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
                turtle.write(arg=f"You have won. The winning color is {winning_color}", move=False, align="center",
                             font=("Arial", 11, "bold"))
            else:
                turtle.hideturtle()
                turtle.setpos(x=0, y=180)
                turtle.write(arg=f"You have lost. The winning color is {winning_color}", move=True, align="center",
                             font=("Arial", 11, "bold"))
        rand_dist = random.randint(1, 10)
        turtle.forward(rand_dist)









screen.exitonclick()