from objects.line import Line
from util.draw_plane import draw_plane
from util.variables import seed, show_lines


def draw_squares(
    _yertle, _planes, _width, _height, _canvas_lines, draw_everything
):
    plane_index = 1
    _yertle.hideturtle()
    f = None
    if not draw_everything:
        f = open("results/%s/%s" % (seed, "plane_info.txt"), "w")
    for plane in _planes:
        intersection_points = []
        for square_line in plane.get_all_lines():
            for canvas_line in _canvas_lines:
                intersection = line_intersection(square_line, canvas_line)
                if intersection:
                    inter_x = intersection[0]
                    inter_y = intersection[1]
                    intersection_points.append([inter_x, inter_y])
        # We found all the intersection points,
        # now we will find all the points that are within the canvas
        for square_line in plane.get_all_lines():
            if is_inside_canvas(_width, _height, square_line.start):
                intersection_points.append(square_line.start)

        if len(intersection_points) != 0:
            if not draw_everything:
                _yertle.clear()
                _yertle.hideturtle()
            sorted_points = convex_hull(intersection_points)
            _yertle.fillcolor(plane.get_colour())
            if not show_lines:
                _yertle.color(plane.get_colour())
            draw_plane(_yertle, sorted_points)

            if not draw_everything:
                ts = _yertle.getscreen()
                plane_name = "plane_%s" % plane_index
                ts.getcanvas().postscript(
                    file="results/%s/%s" % (seed, plane_name + ".eps")
                )
                # Write information about the plane to a file
                f.write(plane_name + ":\n")
                point_index = 1
                for point in intersection_points:
                    # We convert the points from having the origin in [0, 0]
                    # to have the origin in [width/2, height/2].
                    # This makes the bottom left point [0, 0]
                    # It makes it easier when converting it to the canvas
                    x_point = "%.2f" % (point[0] + _width / 2)
                    y_point = "%.2f" % (point[1] + _height / 2)

                    f.write("point_%s:" % point_index)
                    f.write("x: %s " % x_point)
                    f.write("y: %s\n" % y_point)
                f.write("colour: %s" % plane.get_colour())
                f.write("\n\n")

            plane_index += 1
    if not draw_everything and f:
        f.close()
    else:
        ts = _yertle.getscreen()
        ts.getcanvas().postscript(
            file="results/%s/%s" % (seed, "final_image.eps")
        )


def line_intersection(line_1, line_2):
    # https://gist.github.com/kylemcdonald/6132fc1c29fd3767691442ba4bc84018
    x1, y1 = line_1.start
    x2, y2 = line_1.end
    x3, y3 = line_2.start
    x4, y4 = line_2.end
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # parallel
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:  # out of range
        return None
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:  # out of range
        return None
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    return x, y


def is_inside_canvas(_width, _height, point):
    if (-_width / 2) <= point[0] <= (_width / 2):
        if (-_height / 2) <= point[1] <= (_height / 2):
            return True
    return False


def orientation(p, q, r):
    """
    To find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def convex_hull(points):
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
    _yertle.hideturtle()
    # Use the canvas lines to identify where they intersect with the planes
    canvas_left = Line([-_width / 2, -_height / 2], [-_width / 2, _height / 2])
    canvas_top = Line([-_width / 2, _height / 2], [_width / 2, _height / 2])
    canvas_right = Line([_width / 2, _height / 2], [_width / 2, -_height / 2])
    canvas_bottom = Line(
        [_width / 2, -_height / 2], [-_width / 2, -_height / 2]
    )
    canvas_lines = [canvas_left, canvas_top, canvas_right, canvas_bottom]

    _yertle.fillcolor("#FFFFFF")
    draw_plane(
        _yertle,
        [
            canvas_left.start,
            canvas_top.start,
            canvas_right.start,
            canvas_bottom.start,
        ],
    )

    draw_squares(_yertle, _planes, _width, _height, canvas_lines, False)
    draw_squares(_yertle, _planes, _width, _height, canvas_lines, True)
