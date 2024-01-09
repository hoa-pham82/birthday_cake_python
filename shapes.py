import turtle
import math


def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.getscreen().update()


def draw_rectangle(turtle, color, x, y, width, height):
    turtle.hideturtle()
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    
    turtle.end_fill()
    turtle.setheading(0)
    turtle.getscreen().update()


def draw_icing(turtle, color, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(-125, y + 10)
    turtle.pendown()
    turtle.begin_fill()

    for x in range(-125, 125):
        turtle.goto(x, y-10-10*math.cos((x/100) * 2 * math.pi))
    
    turtle.goto(125, y+10)
    turtle.goto(-125, y+10)
    turtle.end_fill()
    turtle.getscreen().update()

def draw_stick(turtle, color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.pensize(3)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.forward(-100)
    turtle.end_fill()
    turtle.getscreen().update()

def draw_circle_on_stick(turtle, color, border_color, x, y, radius):
    turtle.penup()
    turtle.pensize(3)
    turtle.color(color)
    turtle.fillcolor(border_color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.getscreen().update()

def write_text(turtle, text, color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.write(text, font=("sans-serif", 26, "bold"))
    turtle.getscreen().update()



