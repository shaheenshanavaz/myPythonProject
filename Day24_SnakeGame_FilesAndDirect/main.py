import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)   # Here we stop the animation to make the body of the snake to be formed

snake = Snake()
food = Food()
score = ScoreBoard()


# TODO 3: Control the snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")


game_is_on = True
while game_is_on:
    screen.update()  # Here we are starting the animation once the body of the snake is created
    time.sleep(0.1)    # Here we are delaying the movement of the snake

    snake.move()

    # TODO Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # TODO Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # score.game_over()
        # game_is_on = False
        snake.reset_snake()
        score.reset_scoreboard()

    # TODO Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # score.game_over()
            # game_is_on = False
            snake.reset_snake()
            score.reset_scoreboard()


screen.exitonclick()
