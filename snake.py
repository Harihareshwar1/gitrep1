import turtle
positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.turtles = []
        self.create()

    def create(self):
        for i in positions:
            self.add_seg(i)
    def add_seg(self,position):
        timmy = turtle.Turtle("square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(position)
        self.turtles.append(timmy)
    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
             self.turtles[i].goto(self.turtles[i-1].position())
        self.turtles[0].forward(20)
    def up(self):
        if self.turtles[0].heading() == 270:
            pass
        else:
          self.turtles[0].setheading(90)
    def down(self):
        if self.turtles[0].heading() == 90:
            pass
        else:
          self.turtles[0].setheading(270)
    def right(self):
        if self.turtles[0].heading() == 180:
            pass
        else:
          self.turtles[0].setheading(0)
    def left(self):
        if self.turtles[0].heading() == 0:
            pass
        else:
           self.turtles[0].setheading(180)