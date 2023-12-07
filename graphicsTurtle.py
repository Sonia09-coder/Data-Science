# Challenge 1: Draw a square using turtle graphics
from turtle import Turtle, Screen

timmy_the_turtle= Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# timmy_the_turtle.backward(100)       #we can use forward instead of backward and left instead of right
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.backward(100)
# timmy_the_turtle.right(90)
#   OR

for _ in range(4):
    timmy_the_turtle.backward(100)
    timmy_the_turtle.right(90)


screen=Screen()
screen.exitonclick()
