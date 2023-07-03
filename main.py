from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def start_game():
    difficulty = screen.textinput("Game Difficulty", "Select difficulty (easy, medium, hard): ")

    if difficulty is None:
        screen.bye()

    if difficulty.lower() == 'medium':
        snake.speed = snake.MEDIUM_SPEED
    elif difficulty.lower() == 'hard':
        snake.speed = snake.HARD_SPEED
    else:
        snake.speed = snake.EASY_SPEED

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.up, "W")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.down, "S")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.left, "A")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.right, "D")
    screen.onkey(restart_game, "R")
    screen.onkey(restart_game, "r")

    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(snake.speed)
        snake.move()

        # collision with food
        if snake.head.distance(food) < food.collision_distance:
            score.add_score(food.score)
            food.refresh()
            snake.grow()
            if score.get_score() >= score.milestone:
                snake.increase_speed()
                score.milestone += 10

        # collision with walls
        if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
            score.print_game_over()
            score.print_restart()
            break

        # collision with tail
        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < 10:
                score.print_game_over()
                score.print_restart()
                is_game_on = False


def restart_game():
    food.refresh()
    snake.reset_position()
    score.reset_score()
    start_game()


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

start_game()

screen.exitonclick()
