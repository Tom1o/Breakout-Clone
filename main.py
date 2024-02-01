from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Blocks
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")


paddle = Paddle()
ball = Ball()
blocks = Blocks()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=paddle.move_left, key='a')
screen.onkeypress(fun=paddle.move_right, key='d')


game_is_on = True
touched_orange = False
touched_red = False
hits = 0
four_hits = False
twelve_hits = False

while game_is_on:
    time.sleep(ball.sleep_time)
    if (ball.xcor() >= 385 and (ball.heading() < 90 or ball.heading() > 270)) or\
            (ball.xcor() <= -385 and (90 < ball.heading() < 270)):
        ball.bounce_off_wall()

    if ball.ycor() >= 285:
        ball.bounce_off_top()
        paddle.paddle_width = 3
        paddle.shapesize(stretch_len=paddle.paddle_width)

    if ball.distance(paddle) <= (paddle.paddle_width / 2) * 20 and\
            -200 < ball.ycor() <= -180 and 180 < ball.heading() < 360:
        ball.bounce_off_paddle(paddle.xcor(), paddle.paddle_width)
        hits += 1
        if hits >= 4 and not four_hits:
            four_hits = True
            ball.sleep_time *= 0.8
        elif hits >= 12 and not twelve_hits:
            twelve_hits = True
            ball.sleep_time *= 0.8

    if ball.ycor() < -240:
        ball.restart()
        paddle.paddle_width = 6
        paddle.shapesize(stretch_len=paddle.paddle_width)
        touched_orange = False
        touched_red = False
        hits = 0
        four_hits = False
        twelve_hits = False
        scoreboard.decrease_lives()
        if scoreboard.lives == 0:
            game_is_on = False
            scoreboard.final_score()

    for block in blocks.blocks:
        if ball.distance(block) <= 30:

            if block in blocks.red_blocks:
                scoreboard.increase_score(points=7)
                if not touched_red:
                    ball.sleep_time *= 0.8
                    touched_red = True
            elif block in blocks.orange_blocks:
                scoreboard.increase_score(points=5)
                if not touched_orange:
                    ball.sleep_time *= 0.8
                    touched_orange = True
            elif block in blocks.green_blocks:
                scoreboard.increase_score(points=3)
            elif block in blocks.yellow_blocks:
                scoreboard.increase_score(points=1)

            if block.xcor() - 25 < ball.xcor() < block.xcor() + 25 and\
                    (block.ycor() - 7 >= ball.ycor() or block.ycor() + 7 <= ball.ycor()):
                blocks.blocks.remove(block)
                ball.bounce_off_top()
                block.hideturtle()
            elif block.ycor() - 10 < ball.ycor() < block.ycor() + 10 and\
                    (block.xcor() - 10 >= ball.xcor() or block.xcor() + 10 <= ball.xcor()):
                blocks.blocks.remove(block)
                ball.bounce_off_wall()
                block.hideturtle()
        if len(blocks.blocks) == 0:
            ball.restart()
            paddle.paddle_width = 6
            paddle.shapesize(stretch_len=paddle.paddle_width)
            touched_orange = False
            touched_red = False
            hits = 0
            four_hits = False
            twelve_hits = False
            blocks.create_blocks()

    ball.move()
    screen.update()


screen.exitonclick()
