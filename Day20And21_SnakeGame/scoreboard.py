from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 11, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 1)
    #     self.write(arg="GAME OVER :(", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update()




