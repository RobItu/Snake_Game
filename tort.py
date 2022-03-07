from turtle import Turtle, Screen

def up():
    timmy.setheading(90)
def down():
    timmy.setheading(270)
def left():
    timmy.setheading(180)
def right():
    timmy.setheading(0)
def forward():
    timmy.fd(20)
screen = Screen()
timmy = Turtle()
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(forward, "w")
screen.exitonclick()