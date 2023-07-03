from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            self.snake[seg_num].goto(self.snake[seg_num - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for i in range(3):
            segment = Turtle()
            segment.penup()
            segment.color("white")
            segment.shape("square")
            segment.goto(STARTING_POSITIONS[i])
            self.snake.append(segment)

    def up(self):
        print("up")
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        print("down")
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        print("right")

        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        print("left")
        if self.head.heading() != 0:
            self.head.setheading(180)