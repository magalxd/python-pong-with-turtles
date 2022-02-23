from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import ScoreBoard
from dashedline import DashedLine
import time


screen = Screen()

screen.setup(width=800, height=600)
screen.title("Ponggers")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
field = DashedLine()


r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
ball = Ball()
ball.move()

score = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # collision with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:

        ball.bounce()
        ball.move()
    else:
        ball.move()

    # collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.paddle_bounce()
        ball.move()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.paddle_bounce()
        ball.move()

    # scoring points right paddle
    if ball.xcor() >= 390:
        ball.reset_position()
        score.l_point()
    # scoring points left paddle
    if ball.xcor() <= -390:
        ball.reset_position()
        score.r_point()

    if score.r_score >= 7 or score.l_score >= 7:
        score.end_game()
        game_is_on = False









screen.exitonclick()

