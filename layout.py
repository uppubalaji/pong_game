from turtle import Turtle

class Layout(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(2)
        self.pencolor("white")
        self.setheading(90)
        self.penup()
        self.goto(0,-300)
        self.pendown()
    def move(self):
        self.penup()
        self.forward(10)
        self.pendown()
        self.forward(10)
