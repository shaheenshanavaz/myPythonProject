import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

tim = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
# TODO Moving the right paddle
screen.onkey(r_paddle.up_paddle, key="Up")
screen.onkey(r_paddle.down_paddle, key="Down")

# TODO Moving the left paddle
screen.onkey(l_paddle.up_paddle, key="w")
screen.onkey(l_paddle.down_paddle, key="s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    # TODO Detect collision with the up and down wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        # bounce the ball
        ball.bounce_y()

    # TODO Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # TODO Detect when right paddle missed
    if ball.xcor() > 390:
        ball.restart()
        score.l_point()

    # TODO Detect when left paddle missed
    if ball.xcor() < -390:
        ball.restart()
        score.r_point()


screen.exitonclick()