from turtle import Turtle

FONT = ('Courier', 24, 'normal')
SCOREBOARD_POSITION = (0, 270)
COLOUR = "white"
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(COLOUR)
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}        Lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def final_score(self):
        self.goto(0, -100)
        self.write(arg=f"  GAME OVER!\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT)