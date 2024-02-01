from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 10
        self.create_ball()
        self.sleep_time = 0.05

    def create_ball(self):
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.setheading(-45)

    def restart(self):
        self.clear()
        self.create_ball()
        self.goto(0, 0)
        self.sleep_time = 0.05

    def move(self):
        self.forward(self.ball_speed)

    def bounce_off_wall(self):
        self.setheading(180 - self.heading())

    def bounce_off_top(self):
        self.setheading(360 - self.heading())

    def bounce_off_paddle(self, paddle_xcor, paddle_width):
        if paddle_xcor >= self.xcor():
            difference_ratio = (abs(paddle_xcor) - abs(self.xcor())) / (paddle_width * 20)
            self.setheading(150 - (50 * (1 - abs(difference_ratio))))
        elif paddle_xcor < self.xcor():
            difference_ratio = (abs(self.xcor()) - abs(paddle_xcor)) / (paddle_width * 20)
            self.setheading(30 + (50 * (1 - abs(difference_ratio))))
