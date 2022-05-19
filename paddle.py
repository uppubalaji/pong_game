from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, po):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 0.5)
        self.penup()
        self.goto(po)

    def movu(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def movd(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
