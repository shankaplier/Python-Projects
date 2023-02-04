from turtle import Turtle, Screen


# Instantiate the turtle
tim = Turtle()
screen = Screen()


# Functions that moves the turtle in a particular direction
def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def tilt_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)


def tilt_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


# Function to clear drawings and rest the turtle to its normal position
def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

# Functions to listen to key presses and do whatever action is passed
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=tilt_left)
screen.onkey(key="d", fun=tilt_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()