from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5)
        self.xco = 10
        self.yco = 10
        self.movespeed = 0.1
    def move(self):
        nx = self.xcor() + self.xco
        ny = self.ycor() + self.yco
        self.goto(nx, ny)

    def bounce(self):
        self.yco *= -1

    def bounce1(self):
        self.xco *= -1
        self.movespeed *= 0.9

    def respos(self):
        self.goto(0,0)
        self.movespeed = 0.1
        self.bounce1()