import math

from objects.line import Line
from objects.plane import Plane
from util.colours import colours
from util.draw_plane import draw_plane
from util.variables import min_line_length


def get_angle_lines(line_1, line_2):
    # https://stackoverflow.com/questions/28260962/calculating-angles-between-line-segments-python-with-math-atan2
    slope1 = slope_line(line_1.start, line_1.end)
    slope2 = slope_line(line_2.start, line_2.end)
    return angle_slopes(slope1, slope2)


def slope_line(point_1, point_2):
    dividend = point_2[1] - point_1[1]
    divisor = point_2[0] - point_1[0]
    return dividend / divisor


def angle_slopes(slope_1, slope_2):
    divisor = (1 + (slope_2 * slope_1))
    if divisor == 0:
        divisor = 0.00001
    ang_rad = math.atan((slope_2 - slope_1) / divisor)
    ang = math.degrees(ang_rad)
    # We know we have a convex quadrilateral so all angles are positive and between 0 and 180
    if ang > 180:
        return ang - 180
    elif ang < -180:
        return ang + 360
    elif ang < 0:
        return ang + 180
    else:
        return ang


def point_on_line(_line, _point):
    segment_1 = Line(_line.start, _point)
    segment_2 = Line(_point, _line.end)

    segments_length =(segment_1.get_length() + segment_2.get_length())
    # Damn floating points!
    if abs(_line.get_length() - segments_length) <= 0.001:
        return True
    else:
        return False


def point_on_plane(_plane, _point):
    line_1 = _plane.get_line(0)
    line_2 = _plane.get_line(1)
    line_3 = _plane.get_line(2)
    line_4 = _plane.get_line(3)
    # If the point is on any of the 4 lines of the plane it is fine.
    if point_on_line(line_1, _point) or \
            point_on_line(line_2, _point) or \
            point_on_line(line_3, _point) or \
            point_on_line(line_4, _point):
        return True
    else:
        return False


def get_length(start_point, end_point):
    x_length = abs(start_point[0] - end_point[0])
    y_length = abs(start_point[1] - end_point[1])
    return math.sqrt(math.pow(x_length, 2) + math.pow(y_length, 2))


def add_square(_yertle, _rand, _width, _height, _planes, _index):
    # angles = [86, 87, 88, 89, 91, 92, 93, 94]
    angles = [88, 89, 91, 92]
    while True:
        colour_index = _rand.randint(_index, len(colours) - 1 + _index)
        colour_index -= _index
        _yertle.fillcolor(colours[colour_index][1])
        _index += 1

        plane_choice = _rand.randint(_index, len(_planes) - 1 + _index)
        plane_choice -= _index
        _index += 1
        # This is the square that we will want to divide in 2 squares!
        plane = _planes[plane_choice]

        line_choice = _rand.randint(_index, 3 + _index)
        line_choice -= _index
        _index += 1
        line = plane.get_line(line_choice)
        # It's possible that a line is shorter than the minimum length because of the angles, don't pick these
        if line.get_length() <= min_line_length:
            continue
        next_line = line.get_next()
        # We are going to split the chosen line somewhere
        # and attempt to calculate the new resulting plane split using the chosen angle
        line_length_choice = _rand.uniform(_index + min_line_length, line.get_length() + _index)
        line_length_choice -= _index
        _index += 1

        angle_choice = _rand.randint(_index, len(angles) + _index)
        angle_choice -= _index
        angle_choice -= 1
        _index += 1

        ang_1 = angles[angle_choice]

        # Sin(a_1) = Opp/Hyp
        # First we don't know the angle, but we know the Opp and Hyp
        angle_1 = math.degrees(math.asin((line.end[1] - line.start[1]) / line.get_length()))

        # Sin(a_1) = Opp/Hyp
        # Now we know the angle and the Hyp
        test_point_a_1 = line.start
        opp = math.sin(math.radians(angle_1)) * line_length_choice
        adj = math.sqrt(math.pow(line_length_choice, 2) - math.pow(opp, 2))

        # TODO: - or + adj do tests!
        test_point_a_2 = [test_point_a_1[0] + adj, test_point_a_1[1] + opp]
        if not point_on_line(line, test_point_a_2):
            test_point_a_2 = [test_point_a_1[0] - adj, test_point_a_1[1] + opp]
        if not point_on_line(line, test_point_a_2):
            test_point_a_2 = [test_point_a_1[0] + adj, test_point_a_1[1] - opp]
        if not point_on_line(line, test_point_a_2):
            test_point_a_2 = [test_point_a_1[0] - adj, test_point_a_1[1] - opp]
        if not point_on_line(line, test_point_a_2):
            continue

        # It's possible that the point is not in the plane
        _yertle.penup()
        _yertle.goto(test_point_a_2[0], test_point_a_2[1])
        _yertle.pendown()

        test_point_b_1 = test_point_a_2

        # ang_1 is the chosen angle for the new plane
        ang_2 = get_angle_lines(line, next_line)
        ang_3 = get_angle_lines(next_line, next_line.get_next())
        ang_4 = 360 - ang_1 - ang_2 - ang_3

        triangle_1_line_1 = Line(test_point_b_1, next_line.start)
        triangle_1_line_2 = Line(next_line.start, next_line.end)
        triangle_1_line_3 = Line(next_line.end, test_point_b_1)

        _yertle.penup()
        _yertle.goto(test_point_b_1[0], test_point_b_1[1])
        _yertle.pendown()

        _yertle.penup()
        _yertle.goto(next_line.start[0], next_line.start[1])
        _yertle.pendown()

        _yertle.penup()
        _yertle.goto(next_line.end[0], next_line.end[1])
        _yertle.pendown()

        triangle_1_ang_1 = get_angle_lines(triangle_1_line_3, triangle_1_line_1)
        triangle_1_ang_2 = get_angle_lines(triangle_1_line_1, triangle_1_line_2)
        triangle_1_ang_3 = get_angle_lines(triangle_1_line_2, triangle_1_line_3)

        t2_ang_1 = ang_3 - triangle_1_ang_3
        t2_ang_2 = ang_4
        t2_ang_3 = 180 - t2_ang_1 - t2_ang_2

        t2_mid = Line(next_line.end, test_point_b_1).get_length()
        t2_center = (t2_mid * math.sin(math.radians(t2_ang_1))) / math.sin(math.radians(t2_ang_2))
        t2_side = (t2_mid * math.sin(math.radians(t2_ang_3))) / math.sin(math.radians(t2_ang_2))

        # Sin(a_1) = Opp/Hyp
        # Again we only know the Opp and the Hyp
        change_line = next_line.get_next()
        angle_c_1 = math.degrees(math.asin((change_line.end[1] - change_line.start[1]) / change_line.get_length()))

        # Sin(a_1) = Opp/Hyp
        # Now we know the angle and the Hyp
        test_point_c_1 = change_line.start
        opp = math.sin(math.radians(angle_c_1)) * t2_side
        adj = math.sqrt(math.pow(t2_side, 2) - math.pow(opp, 2))

        # TODO: Check if the minus plus thing gives problems later!
        test_point_c_2 = [test_point_c_1[0] + adj, test_point_c_1[1] + opp]
        if not point_on_line(change_line, test_point_c_2):
            test_point_c_2 = [test_point_c_1[0] - adj, test_point_c_1[1] + opp]
        if not point_on_line(change_line, test_point_c_2):
            test_point_c_2 = [test_point_c_1[0] + adj, test_point_c_1[1] - opp]
        if not point_on_line(change_line, test_point_c_2):
            test_point_c_2 = [test_point_c_1[0] - adj, test_point_c_1[1] - opp]
        if not point_on_line(change_line, test_point_c_2):
            # For now we will just assume that the point is out of bounds by angle choice
            continue

        # Check if the other point is actually inside the plane where you want to put it.
        # If this is not the case we do not draw this and try again
        if not point_on_plane(plane, test_point_c_2):
            # The point is not in the plane so try again!
            continue

        triangle_1_points = [
            test_point_b_1,
            next_line.start,
            next_line.end
        ]
        triangle_2_points = [
            change_line.start,
            test_point_c_2,
            test_point_b_1
        ]

        new_plane_1_points = [
            test_point_b_1,
            next_line.start,
            next_line.end,
            test_point_c_2
        ]
        new_plane_2_points = [
            line.start,
            test_point_b_1,
            test_point_c_2,
            change_line.end
        ]

        # Not sure why the min line length wasn't captured before but this seems to work too.
        length_1 = get_length(new_plane_1_points[0], new_plane_1_points[1])
        length_2 = get_length(new_plane_1_points[1], new_plane_1_points[2])
        length_3 = get_length(new_plane_1_points[2], new_plane_1_points[3])
        length_4 = get_length(new_plane_1_points[3], new_plane_1_points[0])
        length_5 = get_length(new_plane_2_points[0], new_plane_2_points[1])
        length_6 = get_length(new_plane_2_points[1], new_plane_2_points[2])
        length_7 = get_length(new_plane_2_points[2], new_plane_2_points[3])
        length_8 = get_length(new_plane_2_points[3], new_plane_2_points[0])
        if length_1 <= min_line_length or \
                length_2 <= min_line_length or \
                length_3 <= min_line_length or \
                length_4 <= min_line_length or \
                length_5 <= min_line_length or \
                length_6 <= min_line_length or \
                length_7 <= min_line_length or \
                length_8 <= min_line_length:
            continue
        plane_1 = Plane(new_plane_1_points, colours[colour_index][1])
        plane_2 = Plane(new_plane_2_points, plane.get_colour())

        # Check if all the new angles are NOT nice, so not 90
        # Damn floating points :(
        if abs(angle_c_1 - 90) < 0.001:
            continue

        # If everything about this new plane is validated, we will finally draw it!
        # First the 2 triangles, mainly for tests and debugging
        draw_plane(_yertle, triangle_1_points)
        draw_plane(_yertle, triangle_2_points)

        # Now draw the new plane!
        draw_plane(_yertle, new_plane_1_points)

        # We don't draw the second plane because the plane below it will be the colour of this new plane.
        # draw_plane(_yertle, new_plane_2_points)

        return plane_1, plane_2, plane_choice

