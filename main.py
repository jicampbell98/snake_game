from turtle import Screen
import time
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard

# Create Screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()  # Create the snake object from created Snake class
food = Food()  # Create the food object from created Food class
scoreboard = Scoreboard()  # Create the scoreboard object from created Scoreboard class

# Start listening to keystrokes
screen.listen()
# Movements
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Keep the snake moving
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.count_score()
        snake.extend()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segments in snake.segments[1:]:  # Here we exclude the head from the following loop (comparison)
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
