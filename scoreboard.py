from turtle import Turtle
import random


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.print_score()


    def print_score(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 12, "normal"))
        self.hideturtle()

    def add_score(self):
        self.score += 1