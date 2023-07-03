from turtle import Screen
from snake import Snake
from food import Food
import time

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
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.reposition()

    # collision with walls
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        print("hit the walls")
        break

    if snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        print("hit the walls")
        break


screen.exitonclick()