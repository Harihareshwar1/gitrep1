from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.penup()
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x,random_y)
    def reposition(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
