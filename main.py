from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle_L = Paddle(direction='left')
paddle_R = Paddle(direction='right')
ball = Ball()
scoreboard = Scoreboard()

start_direction = random.choice(['left', 'right'])

screen.listen()
screen.onkey(paddle_R.up, "Up")
screen.onkey(paddle_R.down, "Down")
screen.onkey(paddle_L.up, "a")
screen.onkey(paddle_L.down, "z")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move(direction=start_direction)

    # Detect collision with the wall (Top and bottom walls)
    if 280 < ball.ycor() or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with both paddles
    if (ball.distance(paddle_R) < 50 and 320 < ball.xcor()) or (ball.distance(paddle_L) < 50 and ball.xcor() < -320):
        print("I hit the paddle")
        ball.bounce_x()

    # Detect if the ball went off the board's edge
    if ball.xcor() < -380 or 380 < ball.xcor():
        if ball.xcor() < -380:
            scoreboard.new_point('RIGHT')
        elif 380 < ball.xcor():
            scoreboard.new_point('LEFT')

        ball.hideturtle()
        ball.home()

        ball.showturtle()
        if start_direction == 'left':
            start_direction = 'right'
        elif start_direction == 'right':
            start_direction = 'left'

screen.exitonclick()

