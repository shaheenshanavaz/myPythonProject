from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("brown")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up_paddle(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down_paddle(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

