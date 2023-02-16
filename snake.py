import random
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
W = 90
S = 270
A = 180
D = 0
COLORS = ["#FF1493", "#C1FFC1", "#BF3EFF", "#BCEE68", "#DC143C", "#FF7F50", "#FFD39B", "#8B0A50", "#FFC125", "#ADD8E6"]


class Snake:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, starting_positions):
        self.color_head = ""
        self.segments = []
        self.create_snake(starting_positions)
        self.head = self.segments[0]
        self.has_lives = False

    def create_snake(self, starting_positions):
        index = 0
        for position in starting_positions:
            self.add_segment(position, index)
            index += 1

    def add_segment(self, position, index):
        new_segment = Turtle("square")
        if index == 0:
            self.color_head = str(random.choice(COLORS))
            new_segment.color(self.color_head)
        else:
            new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position(), 5)

    def remove(self):
        self.segments[-1].goto(1000, 1000)
        del self.segments[-1]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def w(self):
        if self.head.heading() != S:
            self.head.setheading(W)

    def s(self):
        if self.head.heading() != W:
            self.head.setheading(S)

    def a(self):
        if self.head.heading() != D:
            self.head.setheading(A)

    def d(self):
        if self.head.heading() != A:
            self.head.setheading(D)
