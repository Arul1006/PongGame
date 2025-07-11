from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(random.randint(10, 60))

    def move(self):
          self.fd(0.9)

    def reset(self):
        self.goto(0, 0)
        self.setheading(random.randint(10, 60))

    def rebound_standing_side(self):
        self.setheading(180 - self.heading())

    def rebound_sleeping_side(self):
        self.setheading(0 - self.heading())
