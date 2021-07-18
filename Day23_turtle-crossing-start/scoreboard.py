from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Level :{self.score}", move=False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()



