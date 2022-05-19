from turtle import *
from time import sleep
from scoreboard import Scoreboard
from ball import Ball
from layout import Layout
from paddle import Paddle

bgcolor("black")
screen = Screen()
title("pong")
screen.setup(800, 600)
screen.tracer(0)
user_paddle = Paddle((380, 0))
comp_paddle = Paddle((-380, 0))
scoreboard1 = Scoreboard((25, 250))
scoreboard2 = Scoreboard((-25, 250))
layout = Layout()
for i in range(30):
    layout.move()
screen.listen()
screen.onkey(user_paddle.movu, "Up")
screen.onkey(user_paddle.movd, "Down")
screen.onkey(comp_paddle.movu, "w")
screen.onkey(comp_paddle.movd, "s")


ball = Ball()

while 2<3:

    screen.update()
    ball.move()
    sleep(ball.movespeed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(user_paddle) < 50 and ball. xcor() > 360:
        scoreboard1.upd()
        ball.bounce1()
    if ball.distance(comp_paddle) < 50 and ball. xcor() < -360:
        scoreboard2.upd()
        ball.bounce1()
    if ball.xcor()>380:
        scoreboard2.upd()
        ball.respos()
    if ball.xcor() < -380:
        scoreboard1.upd()
        ball.respos()


screen.exitonclick()
