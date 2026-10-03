from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.paddle_up,key="Up")
screen.onkeypress(r_paddle.paddle_down,key="Down")

screen.onkeypress(l_paddle.paddle_up,key="w")
screen.onkeypress(l_paddle.paddle_down,key="s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect collision with r wall
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    #Detect collision with l wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
