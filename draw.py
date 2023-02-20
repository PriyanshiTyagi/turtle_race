from turtle import Turtle, Screen

turt = Turtle()
turt.pensize(5)
screen = Screen()


def forward():
    turt.fd(10)


def backward():
    turt.bk(10)


def clockwise():
    turt.right(10)


def counter_clockwise():
    turt.left(10)


def clear():
    turt.reset()
    turt.pensize(5)


screen.listen()
screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(clockwise, "d")
screen.onkeypress(counter_clockwise, "a")
screen.onkeypress(clear, "c")

screen.exitonclick()
