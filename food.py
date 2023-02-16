from turtle import Turtle
import random

SHAPES = ("circle", "turtle", "triangle", "square")


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.choose_shape()
        self.penup()
        self.refresh()

    def choose_shape(self):
        self.shape(random.choice(SHAPES))
        if self.shape() == "turtle":
            self.turtle_shape()
        elif self.shape() == "circle":
            self.circle_shape()
        elif self.shape() == "triangle":
            self.triangle_shape()
        else:
            self.square_shape()

    def turtle_shape(self):
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("green")
        self.speed("fastest")

    def circle_shape(self):
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")

    def triangle_shape(self):
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

    def square_shape(self):
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.choose_shape()
        self.goto(random_x, random_y)
