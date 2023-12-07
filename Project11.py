#Pong Game 
from turtle import Screen,Turtle
from paddle import Paddle
from ballPaddle import Ball
from scorepaddle import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ballPaddle=Ball()
scorepaddle=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ballPaddle.move_speed)
    screen.update()
    ballPaddle.move()

    #detecting the collision with wall
    if ballPaddle.ycor() > 280 or ballPaddle.ycor() < -280 :
        ballPaddle.bounce_y()

    #detect collision with r_paddle
    if ballPaddle.distance(r_paddle) < 50 and ballPaddle.xcor() > 320 or ballPaddle.distance(l_paddle) < 50 and ballPaddle.xcor() < -320:
        ballPaddle.bounce_x()

    #detect R paddle misses
    if ballPaddle.xcor() > 380:
        ballPaddle.reset_position()
        scorepaddle.l_point()
            
    #detect L paddle misses
    if ballPaddle.xcor() < -380:
        ballPaddle.reset_position()
        scorepaddle.r_point()

screen.exitonclick()