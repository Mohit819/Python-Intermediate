import turtle
s = turtle.Turtle()
import random as r
def draw_rectangle(y):
    for i in range(2):
        s.forward(size)
        s.left(90)
        s.forward(size)
        s.left(90)
def draw_colour_triangle(x):
    s.pencolor(colour)
    for i in range(0,3,1):
        s.forward(100)
        s.left(120)
def draw_circle():
    s.circle(100)
def get_random_colour():
    colours=["red","blue","yellow","green","orange","purple"]
    a=r.choice(colours)
    return a
def get_random_size():
    b = r.randrange(1,100,1)
    return b
while "hi"=="hi":
    s.speed(100)
    colour = get_random_colour()
    size = get_random_size()
    draw_colour_triangle(colour)
    s.left(5)
    draw_rectangle(size)
    draw_circle()
