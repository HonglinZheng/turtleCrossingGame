from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def go_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def go_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def success(self):
        return self.ycor() >= FINISH_LINE_Y

    def upgrade(self):
        self.goto(STARTING_POSITION)
