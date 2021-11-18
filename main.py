from turtle import Turtle, Screen
import time
from paddle import Paddle

screen = Screen()
screen.title("Pong Game")
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()