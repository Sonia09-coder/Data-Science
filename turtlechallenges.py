import turtle as t
import random
tim=t.Turtle()

#Challenge 1: Drawing a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

tim.shape("turtle")
# colors=["pink","green","red","blue","wheat","coral","SeaGreen"]
#Challenge 2: Drawing the shapes


# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

#Challenge 3: Draw a random walk
directions=[0,90,180,270]
t.colormode(255)
tim.pensize(10)
tim.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# screen=Screen()
# screen.exitonclick()