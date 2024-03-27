from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()

    def increment_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", False, align="center", font=('Arial', 12, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=('Courier', 12, "bold"))
