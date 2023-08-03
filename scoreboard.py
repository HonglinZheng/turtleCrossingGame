from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"LEVEL: {self.level}", align = "left", font = FONT)

    def upgrade(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", align = "left", font = FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f"game over", align="center", font=FONT)

    def complete(self):
        self.goto(0,0)
        self.write(f"You succeed!", align="center", font=FONT)
