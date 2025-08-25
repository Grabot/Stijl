import math

from objects.plane import Plane
from util.colours import colours
from util.draw_plane import draw_plane
from util.variables import show_lines


def background_square_clean(_rand, _width, _height, _index):
    # We will draw a larger square on it's side. The points of the square are:
    # [-width/2, -height/2]
    # [width/2, -height/2]
    # [width/2, height/2]
    # [-width/2, height/2]
    # The square behind this square on it side will have the following points:
    side_triangle = _height / math.sqrt(2)
    point_a = math.pow(side_triangle, 2) - math.pow(_height / 2, 2)
    point_a = math.sqrt(point_a)
    point_a = -(_width / 2) - point_a
    left_point = [point_a, 0]
    point_c = point_a * -1
    right_point = [point_c, 0]
    side_triangle_2 = _width / math.sqrt(2)
    point_b = math.pow(side_triangle_2, 2) - math.pow(_width / 2, 2)
    point_b = math.sqrt(point_b)
    point_b = -(_height / 2) - point_b
    bottom_point = [0, point_b]
    point_d = point_b * -1
    top_point = [0, point_d]

    colour_index = _rand.randint(_index, len(colours)-1 + _index)
    colour_index -= _index
    _index += 1

    background_points = [left_point, top_point, right_point, bottom_point]
    background_plane = Plane(background_points, colours[colour_index])

    return background_plane

def background_square(_yertle, _rand, _width, _height, _index):
    # We will draw a larger square on it's side. The points of the square are:
    # [-width/2, -height/2]
    # [width/2, -height/2]
    # [width/2, height/2]
    # [-width/2, height/2]
    # The square behind this square on it side will have the following points:
    side_triangle = _height / math.sqrt(2)
    point_a = math.pow(side_triangle, 2) - math.pow(_height / 2, 2)
    point_a = math.sqrt(point_a)
    point_a = -(_width / 2) - point_a
    left_point = [point_a, 0]
    point_c = point_a * -1
    right_point = [point_c, 0]
    side_triangle_2 = _width / math.sqrt(2)
    point_b = math.pow(side_triangle_2, 2) - math.pow(_width / 2, 2)
    point_b = math.sqrt(point_b)
    point_b = -(_height / 2) - point_b
    bottom_point = [0, point_b]
    point_d = point_b * -1
    top_point = [0, point_d]

    colour_index = _rand.randint(_index, len(colours) + _index)
    colour_index -= _index
    _yertle.fillcolor(colours[colour_index])
    print("colour_index: %s" % colour_index)
    _index += 1

    background_points = [left_point, top_point, right_point, bottom_point]
    background_plane = Plane(background_points, colours[colour_index])
    _yertle.penup()
    _yertle.goto(left_point[0], left_point[1])
    if not show_lines:
        _yertle.color(colours[colour_index])
    _yertle.pendown()

    _yertle.begin_fill()
    _yertle.goto(top_point[0], top_point[1])
    _yertle.goto(right_point[0], right_point[1])
    _yertle.goto(bottom_point[0], bottom_point[1])
    _yertle.goto(left_point[0], left_point[1])
    _yertle.end_fill()

    return background_plane


def hide_canvas_sides(_yertle, _width, _height):
    side_triangle = _height / math.sqrt(2)
    point_a = math.pow(side_triangle, 2) - math.pow(_height / 2, 2)
    point_a = math.sqrt(point_a)
    point_a = -(_width / 2) - point_a
    left_point = [point_a, 0]
    point_c = point_a * -1
    right_point = [point_c, 0]
    side_triangle_2 = _width / math.sqrt(2)
    point_b = math.pow(side_triangle_2, 2) - math.pow(_width / 2, 2)
    point_b = math.sqrt(point_b)
    point_b = -(_height / 2) - point_b
    bottom_point = [0, point_b]
    point_d = point_b * -1
    top_point = [0, point_d]
    _yertle.fillcolor("#FFFFFF")

    canvas_point_bl = [-_width / 2, -_height / 2]
    canvas_point_br = [_width / 2, -_height / 2]
    canvas_point_tl = [-_width / 2, _height / 2]
    canvas_point_tr = [_width / 2, _height / 2]
    left_triangle = [canvas_point_bl, canvas_point_tl, left_point]
    right_triangle = [canvas_point_br, canvas_point_tr, right_point]
    top_triangle = [canvas_point_tl, canvas_point_tr, top_point]
    bottom_triangle = [canvas_point_bl, canvas_point_br, bottom_point]
    draw_plane(_yertle, left_triangle)
    draw_plane(_yertle, right_triangle)
    draw_plane(_yertle, top_triangle)
    draw_plane(_yertle, bottom_triangle)
