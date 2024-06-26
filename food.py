from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed(0)
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-270, 270)
        ran_y = random.randint(-270, 250)
        self.goto(ran_x, ran_y)