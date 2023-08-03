from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
FREQUENCY = 6

class CarManager(Turtle):
    def __init__(self):
        self.carlist = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        psblt = random.randint(1, FREQUENCY)
        if (psblt != 1):
            return
        car = Turtle("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.color(random.choice(COLORS))
        y = random.randint(-5, 5)
        car.goto(280, y*50)
        car.setheading(180)
        self.carlist.append(car)

    def move(self):
        for car in self.carlist:
            if (car.xcor() == -320):
                self.carlist.remove(car)
            else:
                car.forward(self.speed)

    def upgrade(self):
        self.speed += MOVE_INCREMENT
        global FREQUENCY
        FREQUENCY -= 1

