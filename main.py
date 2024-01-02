import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Game Race", prompt="Make your bet. Enter a color: ")
colors = ["red", "black", "purple", "green", "blue", "yellow", "orange"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtle = []
for turtle_index in range(0,6):
    tim = Turtle()
    tim.penup()
    tim.color(colors[turtle_index])
    tim.shape("turtle")
    tim.goto(x=-240, y=y_positions[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"you win! The {winning_turtle} wins")
            else:
                print(f"you lost! The {winning_turtle} wins")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()






# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def counter_clockwise():
#     tim.left(10)
#
#
# def clockwise():
#     tim.right(10)
#
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
# screen.listen()
# screen.onkey(key="W", fun=move_forward)
# screen.onkey(key="S", fun=move_backward)
# screen.onkey(key="A", fun=counter_clockwise)
# screen.onkey(key="D", fun=clockwise)
# screen.onkey(key="C", fun=clear_drawing)
