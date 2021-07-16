from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        print(f"new x{new_x}")
        print(f"new y{new_y}")
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        print(f"bounce new y{self.y_move}")

    def bounce_x(self):
        self.x_move *= -1
        print(f"bounce new y{self.x_move}")
        self.move_speed *= 0.9

    def restart(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.bounce_x()