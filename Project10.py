#Building the snake game
from turtle import Screen
from game_snake import Snake
from food import Food
from snakeScoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(game_snake.up,"Up")
screen.onkeypress(game_snake.down,"Down")
screen.onkeypress(game_snake.left,"Left")
screen.onkeypress(game_snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    game_snake.move()

    #detection of food
    if game_snake.head.distance(food) < 15:
        food.refresh()
        game_snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if game_snake.head.xcor()> 280 or game_snake.head.xcor()<-280 or game_snake.head.ycor()>280 or game_snake.head.ycor()<-280:
        scoreboard.reset()
        game_snake.reset()
        
    #detect collision with tail
    for segment in game_snake.segments[1:]:
       if segment==game_snake.head:
            pass
       elif game_snake.head.distance(segment) < 10:
            scoreboard.reset()
            game_snake.reset()
screen.exitonclick()
