import time
import turtle
import math
from snake import Snake
from Food import Food
from scoreboard import Score
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
scoreboard = Score()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.tracer(0)
def collide():
    return snake.turtles[0].distance(food)


game = True
while game:
    if collide() < 15:
        food.reposition()
        snake.add_seg(snake.turtles[-1].position())
        scoreboard.score+=1
        scoreboard.clear()
        scoreboard.show()
    if (math.fabs(snake.turtles[0].xcor())) > 285 or math.fabs(snake.turtles[0].ycor()) > 285:
        scoreboard.gameover()
        game = False
    for i in snake.turtles[1:]:
        if i.distance(snake.turtles[0]) < 10:
            scoreboard.gameover()
            game = False
    screen.update()
    time.sleep(0.09)
    snake.move()

screen.exitonclick()
