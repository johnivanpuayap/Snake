from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.milestone = 10
        self.color("white")
        self.penup()
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align="center", font=FONT)
        self.hideturtle()

    def add_score(self, add_score):
        self.score += add_score
        self.print_score()

    def print_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align="center", font=FONT)
        self.hideturtle()

    def print_restart(self):
        self.goto(0, -20)
        self.write("Press 'r' or 'R' to Restart the Game", True, align="center", font=("Courier", 12, "normal"))
        self.hideturtle()

    def get_score(self):
        return self.score

    def reset_score(self):
        self.clear()
        self.score = 0
        self.milestone = 10
        self.print_score()
