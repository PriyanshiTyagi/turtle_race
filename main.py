from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(700, 400)
screen.bgcolor(0, 0, 0)


y_cor = [-130]
for i in range(5):
    y_cor.append(y_cor[i] + 50)

colors = ["violet", "blue", "green", "yellow", "red", "cyan"]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2, 2, 1)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_cor[i])
    new_turtle.write(arg=colors[i], font=('Arial', 12, 'normal'))
    new_turtle.backward(50)
    all_turtles.append(new_turtle)
user_bet = screen.textinput(title="Make a bet ", prompt="Which turtle will win the race ?Enter any color:")
race_on = True

if user_bet:

    while race_on:
        for tuts in all_turtles:
            tuts.forward(random.randint(0, 10))
            if tuts.xcor() > 320:
                race_on = False
                winning_color = tuts.pencolor()
                if winning_color == user_bet:
                    print(f"You won .The {winning_color} turtle won the race")
                else:
                    print(f"You lose .The {winning_color} turtle won the race")

screen.exitonclick()
