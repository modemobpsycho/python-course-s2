import turtle
from random import sample, randint, choice
from time import sleep

BITMAPS = (
    ((0, 0),),
    ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)),
    ((0, -1), (0, 1), (0, -2), (0, 2),
     (1, 1), (1, -1), (1, 0), (2, 0),
     (-1, 1), (-1, 0), (-1, -1), (-2, 0))
)


class Star:
    def __init__(self, size, pos, color):
        self.pen = turtle.Turtle(shape='square', visible=False)
        self.pen.speed(0)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.shapesize(.5)
        self.pen.fillcolor(color)
        self.size = size
        self.x = pos[0] * 10
        self.y = pos[1] * 10
        self.key_frame = 0
        self.draw()

    def draw(self):
        self.pen.clear()
        for x, y in BITMAPS[self.key_frame]:
            x, y = x * 10, y * 10
            self.pen.goto(self.x + x, self.y + y)
            self.pen.stamp()
        self.pen.goto(-600, -600)
        turtle.update()

    def animation(self):
        self.key_frame = (self.key_frame + 1) % (self.size + 1)
        self.draw()

    def __str__(self):
        return f"{self.size=}, {self.x=}, {self.y=}"


turtle.tracer(0, 0)
turtle.goto(-600, -600)
turtle.hideturtle()
turtle.bgcolor('black')
stars = [
    Star(sample((0, 1, 2), counts=(10, 5, 2), k=1)[0],
         (randint(-50, 50), randint(-50, 50)),
         choice(('white', 'red', 'purple', 'cyan', 'green', 'yellow')))
    for _ in range(35)
]

while True:
    sleep(.1)
    for star in stars:
        star.animation()