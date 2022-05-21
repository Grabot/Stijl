import math

from objects.line import Line
from util.draw_plane import draw_plane


def line_intersection(line_1, line_2):
    # https://gist.github.com/kylemcdonald/6132fc1c29fd3767691442ba4bc84018
    x1, y1 = line_1.start
    x2, y2 = line_1.end
    x3, y3 = line_2.start
    x4, y4 = line_2.end
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0:  # parallel
        return None
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return None
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return None
    x = x1 + ua * (x2-x1)
    y = y1 + ua * (y2-y1)
    return x, y


def is_inside_canvas(_width, _height, point):
    if (-_width / 2) <= point[0] <= (_width / 2):
        if (-_height / 2) <= point[1] <= (_height / 2):
            return True
    return False


def orientation(p, q, r):
    '''
    To find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    '''
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convex_hull(points, _width):
    # https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
    n = len(points)
    if n < 3:
        return points

    left_point = points[0]
    left_index = 0
    for i in range(1, len(points)):
        if points[i][0] < left_point[0]:
            left_point = points[i]
            left_index = i

    hull = []

    p = left_index
    while True:
        hull.append(points[p])
        q = (p + 1) % n

        for i in range(n):

            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == left_index:
            break

    return hull


def draw_canvas(_yertle, _width, _height, _planes):
    print("drawing canvas")
    # First clear the canvas and start over (debug purpose)
    _yertle.clear()
    # We will use the canvas line segments to identify where they intersect with the planes
    canvas_left = Line([-_width / 2, -_height / 2], [-_width / 2, _height / 2])
    canvas_top = Line([-_width / 2, _height / 2], [_width / 2, _height / 2])
    canvas_right = Line([_width / 2, _height / 2], [_width / 2, -_height / 2])
    canvas_bottom = Line([_width / 2, -_height / 2], [-_width / 2, -_height / 2])
    canvas_lines = [
        canvas_left,
        canvas_top,
        canvas_right,
        canvas_bottom
    ]

    _yertle.speed(5)
    _yertle.fillcolor('#FFFFFF')
    draw_plane(_yertle, [
        canvas_left.start,
        canvas_top.start,
        canvas_right.start,
        canvas_bottom.start
    ])
    _yertle.fillcolor('#000000')
    for plane in _planes:
        intersection_points = []
        for square_line in plane.get_all_lines():
            for canvas_line in canvas_lines:
                intersection = line_intersection(square_line, canvas_line)
                if intersection:
                    inter_x = intersection[0]
                    inter_y = intersection[1]
                    intersection_points.append([inter_x, inter_y])
        # We found all the intersection points, now we will find all the points that are within the canvas
        for square_line in plane.get_all_lines():
            if is_inside_canvas(_width, _height, square_line.start):
                intersection_points.append(square_line.start)

        if len(intersection_points) != 0:
            # We have some plane that we should draw!
            sorted_points = convex_hull(intersection_points, _width)
            draw_plane(_yertle, sorted_points)
        print("intersected at: %s" % intersection_points)
