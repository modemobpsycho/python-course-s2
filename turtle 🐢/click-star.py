from turtle import *
from random import *
speed(0)
def stars(size, count, colo, x,y):
  for i in range(count):
    h = tuple(randint(0, 255) for _ in '123')
    size = randint(3,33)
    fillcolor(h)
    color(h)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
      forward(size)
      left(144)
    end_fill()
size = randint(10,20)
count = randint(50,80)
h = tuple(randint(0, 255) for _ in '123')

def left_mouse_click(x, y):
    stars(1,1,h,x, y)
hideturtle()
Screen().bgcolor('black')
Screen().onclick(left_mouse_click)
Screen().listen()