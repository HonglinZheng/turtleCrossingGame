import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
manager = CarManager()
board = Scoreboard()
level = 1

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.create_car()
    manager.move()

    #game over when car collision
    for car in manager.carlist:
        if car.distance(player) < 20:
            board.gameover()
            game_is_on = False


    #go to next level
    if player.success():
        if level == 5:
            board.complete()
            game_is_on = False
            break
        level += 1
        player.upgrade()
        manager.upgrade()
        board.upgrade()

screen.exitonclick()
