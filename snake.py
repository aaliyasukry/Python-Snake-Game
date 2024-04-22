from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, color):
        # TODO 1: Create a snake body.
        self.segments = []
        self.color = color
        self.create_snake()
        self.head = self.segments[0]

    # Extend the Tail
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Add new segment
    def add_segment(self, positions):
        tim = Turtle(shape="square")
        tim.color(self.color)
        tim.penup()
        tim.goto(positions)
        self.segments.append(tim)

    # Create the Snake
    def create_snake(self):
        for positions in START_POSITIONS:
            self.add_segment(positions)

    # TODO 2: Move the snake.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    # TODO 3: Control the snake.
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
