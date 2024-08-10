from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backward():
    tim.back(10)
def move_anti_clockwise():
    tim.right(30)
def move_clockwise():
    tim.left(30)
def clear():
    tim.clear()
    tim.reset()
screen.listen()
screen.onkey(key="W", fun = move_forwards)
screen.onkey(key="S", fun = move_backward)
screen.onkey(key="A", fun = move_anti_clockwise)
screen.onkey(key="D", fun = move_clockwise)
screen.onkey(key="C", fun = clear)
screen.exitonclick()
