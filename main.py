import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

tracker = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
cars = []
player = Player()
screen.onkeypress(player.move_turtle,"Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    if player.reset_turtle():
        scoreboard.level_up()
    if round(tracker % 3) == 0:
        cars.append(CarManager())
    for index in range(0,len(cars)):
        cars[index].move_car(scoreboard.report_level())
        if cars[index].xcor()-20 <= 10  and cars[index].xcor()+20 >= -10 and cars[index].ycor()-10 <= player.ycor()+10 and cars[index].ycor()+10 >= player.ycor()-10:
            game_is_on = False
            scoreboard.game_over()
    time.sleep(0.1)
    tracker+=0.3
    screen.update()
screen.exitonclick()
