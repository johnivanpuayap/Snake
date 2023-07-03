from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

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
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.grow()
        if score.get_score() % 10 == 0:
            snake.increase_speed()

    # collision with walls
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        score.print_game_over()
        break

    if snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        score.print_game_over()
        break

    # collision with tails
    for segment in snake.snake:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.print_game_over()
            break

screen.exitonclick()