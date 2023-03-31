import random
from PIL import Image, ImageDraw
import os
from util.add_square import add_square_clean
from util.background_square import background_square_clean
from util.variables import (
    width,
    height,
    min_squares,
    max_squares,
    seed,
    show_lines
)


def stijl_instant():
    random.seed(seed)
    planes = []
    # Add an index so that we can pick new colours from the same list
    # using the same seed and get a new one every time.
    index = 0
    background_plane = background_square_clean(random, width, height, index)
    index += 1
    planes.append(background_plane)

    points = []
    for line in background_plane.get_all_lines():
        points.append((line.start[0] + width, line.start[1] + height))

    square_numbers = random.randint(min_squares, max_squares)

    for x in range(0, square_numbers):
        plane_1, plane_2, chosen_plane = add_square_clean(
            random, width, height, planes, index
        )
        del planes[chosen_plane]
        planes.append(plane_1)
        planes.append(plane_2)

    im = Image.new("RGBA", (width*2, height*2))
    draw = ImageDraw.Draw(im, "RGBA")
    for plane in planes:
        points = []
        for line in plane.get_all_lines():
            points.append((line.start[0] + width, line.start[1] + height))
        plane_colour = tuple(int(plane.colour.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
        if show_lines:
            draw.polygon(points, plane_colour, outline='black', width=2)
        else:
            draw.polygon(points, plane_colour)

    del draw

    bound_x = width/2
    bound_y = height/2
    box = (bound_x, bound_y, bound_x + width, bound_y + height)
    im2 = im.crop(box)

    if not os.path.exists("results"):
        os.makedirs("results")

    if not os.path.exists("results/%s" % seed):
        os.makedirs("results/%s" % seed)

    file = "results/%s/%s" % (seed, "%s.png" % seed)
    im2.save(file)


if __name__ == "__main__":
    stijl_instant()

