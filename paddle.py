from turtle import Turtle

POSITION = (0, -200)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_speed = 40
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.shape('square')
        self.paddle_width = 6
        self.shapesize(stretch_len=self.paddle_width)
        self.goto(POSITION)

    def move_left(self):
        if self.xcor() <= (-400 + (20 * self.paddle_width/2)):
            pass
        else:
            self.back(self.paddle_speed)

    def move_right(self):
        if self.xcor() >= (400 - (20 * self.paddle_width/2)):
            pass
        else:
            self.forward(self.paddle_speed)
