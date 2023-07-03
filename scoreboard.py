from turtle import Turtle
import random


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.write("Score: ", True, align="center")