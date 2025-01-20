import random as r
colours = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink","magenta", "light green", "light blue"]
import turtle
t = turtle.Turtle()
steps =r.randrange(10,70,1)
degrees = r.randrange(10,350,1)
while colours == colours:
    colour = r.choice(colours)
    t.forward(steps)
    t.left(degrees)
    t.pencolor(colour)
    
