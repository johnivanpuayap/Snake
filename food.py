from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.collision_distance = 0
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        chance = random.randint(1, 10)
        if chance <= 1:
            self.big_circle()
        elif chance <= 3:
            self.medium_circle()
        else:
            self.small_circle()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def small_circle(self):
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.collision_distance = 15
        self.score = 1

    def medium_circle(self):
        self.collision_distance = 20
        self.score = 3

    def big_circle(self):
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.collision_distance = 25
        self.score = 5
