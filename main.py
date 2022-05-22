import turtle
from turtle import Screen
import random
import os
from util.add_square import add_square
from util.background_square import background_square, hide_canvas_sides
from util.draw_canvas import draw_canvas

if __name__ == '__main__':
    # seed = "test7"
    seed = "Sander Kools"
    random.seed(seed)

    yertle = turtle.Turtle(visible=False)
    yertle.hideturtle()

    width = 800
    height = 600
    max_squares = 10
    screen = Screen()
    view_algorithm = True
    start_x = 0
    start_y = 0
    if view_algorithm:
        # screen setup to view algorithm
        if width > height:
            screen.setup(width*2, width*2, startx=start_x, starty=start_y)
            screen.setworldcoordinates(-width, -width, width + 5, width + 5)
        else:
            screen.setup(height * 2, height * 2, startx=start_x, starty=start_y)
            screen.setworldcoordinates(-height, -height, height + 5, height + 5)
    else:
        # Screen setup with only canvas
        screen.setup(width, height, startx=start_x, starty=start_y)
        screen.setworldcoordinates(-width/2, -height/2, width/2 + 5, height/2 + 5)

    yertle.speed(0)
    planes = []
    # Add an index so that we can pick new colours from the same list using the same seed and get a new one every time.
    index = 0
    background_plane = background_square(yertle, random, width, height, index)
    index += 1
    planes.append(background_plane)

    triangle_numbers = random.randint(0, max_squares)

    for x in range(0, triangle_numbers):
        plane_1, plane_2, chosen_plane = add_square(yertle, random, width, height, planes, index)
        del planes[chosen_plane]
        planes.append(plane_1)
        planes.append(plane_2)
    # for t in range(0, triangle_numbers):
    #     add_random_triangle(random, width, height)
    print(triangle_numbers)
    # background_plane = hide_canvas_sides(yertle, width, height)

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('results/%s' % seed):
        os.makedirs('results/%s' % seed)

    # I think now we'll start over and redraw the planes in their final position with the canvas
    # This way we can identify the coordinates
    yertle.speed(10)
    draw_canvas(yertle, width, height, planes, seed)

    turtle.Screen().exitonclick()

