import turtle
from turtle import Screen
import random

from util.add_square import add_square
from util.background_square import background_square, hide_canvas_sides

if __name__ == '__main__':
    random.seed("Sander Kools")
    
    width = 800
    height = 600
    screen = Screen()
    if width > height:
        screen.setup(width*2, width*2, startx=0, starty=0)
        screen.setworldcoordinates(-width, -width, width + 5, width + 5)
    else:
        screen.setup(height * 2, height * 2, startx=0, starty=0)
        screen.setworldcoordinates(-height, -height, height + 5, height + 5)
    # screen.tracer(False)

    turtle.hideturtle()
    yertle = turtle.Turtle(visible=True)
    yertle.speed(10)

    planes = []
    # Add an index so that we can pick new colours from the same list using the same seed and get a new one every time.
    index = 0
    background_plane = background_square(yertle, random, width, height, index)
    index += 1
    planes.append(background_plane)

    triangle_numbers = random.randint(0, 40)

    for x in range(0, triangle_numbers):
        plane_1, plane_2, chosen_plane = add_square(yertle, random, width, height, planes, index)
        del planes[chosen_plane]
        planes.append(plane_1)
        planes.append(plane_2)
    # for t in range(0, triangle_numbers):
    #     add_random_triangle(random, width, height)
    print(triangle_numbers)
    background_plane = hide_canvas_sides(yertle, width, height)

    turtle.Screen().exitonclick()

