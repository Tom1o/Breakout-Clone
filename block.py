from turtle import Turtle


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.blocks = []
        self.red_blocks = []
        self.orange_blocks = []
        self.green_blocks = []
        self.yellow_blocks = []
        self.create_blocks()

    def create_blocks(self):
        for row in range(8):
            for column in range(16):
                block = Turtle(shape='square')
                block.penup()
                block.color('white')
                block.shapesize(stretch_len=2)
                block.goto((-375 + (column * 50)), (200 - (row * 25)))
                if row <= 1:
                    block.color('red')
                    self.red_blocks.append(block)
                elif row <= 3:
                    block.color('orange')
                    self.orange_blocks.append(block)
                elif row <= 5:
                    block.color('green')
                    self.green_blocks.append(block)
                elif row <= 7:
                    block.color('yellow')
                    self.yellow_blocks.append(block)
                self.blocks.append(block)


