import turtle
from turtle import Screen
import random

from util.background_square import background_square


if __name__ == '__main__':
    random.seed("test")
    
    width = 800
    height = 600
    screen = Screen()
    if width > height:
        screen.setup(width*2, width*2, startx=200, starty=200)
        screen.setworldcoordinates(-width, -width, width + 5, width + 5)
    else:
        screen.setup(height * 2, height * 2, startx=200, starty=200)
        screen.setworldcoordinates(-height, -height, height + 5, height + 5)
    # screen.tracer(False)

    turtle.hideturtle()
    yertle = turtle.Turtle(visible=True)
    yertle.speed(10)

    # Add an index so that we can pick new colours from the same list using the same seed and get a new one every time.
    index = 0
    background_square(yertle, random, width, height, index)
    index += 1

    triangle_numbers = random.randint(0, 20)

    # add_random_plane(yertle, random, width, height, index)
    # for t in range(0, triangle_numbers):
    #     add_random_triangle(random, width, height)
    index += triangle_numbers
    print(triangle_numbers)

    turtle.Screen().exitonclick()

