from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0,280)
        self.score = 0
        self.hideturtle()
        self.write(arg=f"SCORE = {self.score}",align="center",font=("Arial",14,"bold"))
    def show(self):
        self.write(arg=f"SCORE = {self.score}", align="center", font=("Arial", 14, "bold"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAMEOVER",align="center",font=("Arial",17,"bold"))