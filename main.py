from turtle import Screen
from snake import Snake
import time
import random

#   3. Enable user to control the snake
#   4. Generate food randomly on the game screen
#   5. Detect collision with the food
#   6. Create a scoreboard
#   7. Detect collision with the wall
#   8. Detect collision with the body
#   9. Allow users to choose difficulty and adjust the snake's speed accordingly

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.colormode(255)
screen.title("Snake Game")
screen.tracer(0)
screen.update()
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()