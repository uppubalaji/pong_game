from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, po):
        super().__init__()
        self.sc = 0
        self.po = po
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(self.po)
        self.score()

        
    def score(self):
        self.clear()
        self.write(f"{self.sc}", align = "center", font = ("Arial", 25, "normal"))

    def upd(self):
        self.sc+=1
        self.score()
