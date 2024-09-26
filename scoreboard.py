from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-200,250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.update_level()

    def level_up(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}",False,"center",FONT)

    def report_level(self):
        return self.level

    def game_over(self):
        game_over = Scoreboard()
        game_over.goto(0,0)
        game_over.write("Game Over",False,"center",FONT)
        game_over.hideturtle()