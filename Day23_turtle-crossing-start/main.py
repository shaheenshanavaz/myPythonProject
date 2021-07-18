import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
# TODO Moving the player up
screen.listen()
screen.onkey(player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    # TODO Turtle collide with the car
    for mycar in car.all_cars:
        if mycar.distance(player) < 20:
            # print("hit")
            player.goto(0, 0)
            player.write("GAME OVER", move=False, align="center", font=("Arial", 20, "bold"))
            game_is_on = False

    # TODO Detect if the player reached the other side and speed up the cars in the next level
    if player.is_finish_line():
        player.start_position()
        car.level_up()
        score.increase_score()

screen.exitonclick()
