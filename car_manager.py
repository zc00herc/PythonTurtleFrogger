from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.make_cars()
        self.move_car(self.level)

    def make_cars(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(340,random.randint(-250,250))
        self.setheading(180)


    def move_car(self,level):
        self.fd(STARTING_MOVE_DISTANCE+(MOVE_INCREMENT*(level-1)))

    def destroy_car(self):
        self.clear()