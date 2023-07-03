from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align="center", font=FONT)
        self.hideturtle()

    def add_score(self, score):
        self.score += score
        self.print_score()

    def print_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align="center", font=FONT)
        self.hideturtle()

    def get_score(self):
        return self.score
