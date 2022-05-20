import math

from objects.line import Line
from objects.plane import Plane
from util.colours import colours
from util.draw_plane import draw_plane


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
    ang_rad = math.atan((slope_2 - slope_1) / (1 + (slope_2 * slope_1)))
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


def add_square(_yertle, _rand, _width, _height, planes, _index):
    angles = [86, 87, 88, 89, 91, 92, 93, 94]
    print("adding square")
    colour_index = _rand.randint(_index, len(colours) + _index)
    colour_index -= _index
    _yertle.fillcolor(colours[colour_index][1])
    print("colour_index: %s" % colour_index)
    _index += 1

    plane_choice = _rand.randint(_index, len(planes) + _index)
    plane_choice -= _index
    plane_choice -= 1
    _index += 1
    # This is the square that we will want to divide in 2 squares!
    plane = planes[plane_choice]

    line_choice = _rand.randint(_index, 4 + _index)
    line_choice -= _index
    _index += 1
    line = plane.get_line(line_choice)
    next_line = line.get_next()
    # We are going to split the chosen line somewhere
    # and attempt to calculate the new resulting plane split using the chosen angle
    line_length_choice = _rand.uniform(_index, line.get_length() + _index)
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

    test_point_a_2 = [test_point_a_1[0] + adj, test_point_a_1[1] + opp]

    _yertle.penup()
    _yertle.goto(test_point_a_2[0], test_point_a_2[1])
    _yertle.pendown()

    test_point_b_1 = [test_point_a_1[0] + adj, test_point_a_1[1] + opp]
    test_point_b_2 = line.end

    new_line_1 = Line(test_point_a_1, test_point_a_2)
    new_line_2 = Line(test_point_b_1, test_point_b_2)

    # ang_1 is the chosen angle for the new plane
    ang_2 = get_angle_lines(line, next_line)
    ang_3 = get_angle_lines(next_line, next_line.get_next())
    ang_4 = 360 - ang_1 - ang_2 - ang_3

    print("ang 1: %s" % ang_1)
    print("ang 2: %s" % ang_2)
    print("ang 3: %s" % ang_3)
    print("ang 4: %s" % ang_4)
    print("total: %s" % (ang_1 + ang_2 + ang_3 + ang_4))

    triangle_1_line_1 = Line(test_point_b_1, next_line.start)
    triangle_1_line_2 = Line(next_line.start, next_line.end)
    triangle_1_line_3 = Line(next_line.end, test_point_b_1)

    triangle_1_ang_1 = get_angle_lines(triangle_1_line_3, triangle_1_line_1)
    triangle_1_ang_2 = get_angle_lines(triangle_1_line_1, triangle_1_line_2)
    triangle_1_ang_3 = get_angle_lines(triangle_1_line_2, triangle_1_line_3)

    print("t1 ang 1: %s" % triangle_1_ang_1)
    print("t1 ang 2: %s" % triangle_1_ang_2)
    print("t1 ang 3: %s" % triangle_1_ang_3)
    print("total: %s" % (triangle_1_ang_1 + triangle_1_ang_2 + triangle_1_ang_3))

    print("length 1: %s" % triangle_1_line_1.get_length())
    print("length 2: %s" % triangle_1_line_2.get_length())
    print("length 3: %s" % triangle_1_line_3.get_length())

    t2_ang_1 = ang_3 - triangle_1_ang_3
    t2_ang_2 = ang_4
    t2_ang_3 = 180 - t2_ang_1 - t2_ang_2

    print("final triangle ang 1: %s" % t2_ang_1)
    print("final triangle ang 2: %s" % t2_ang_2)
    print("final triangle ang 3: %s" % t2_ang_3)

    t2_mid = Line(next_line.end, test_point_b_1).get_length()
    t2_center = (t2_mid * math.sin(math.radians(t2_ang_1))) / math.sin(math.radians(t2_ang_2))
    t2_side = (t2_mid * math.sin(math.radians(t2_ang_3))) / math.sin(math.radians(t2_ang_2))

    print("t2_mid: %s" % t2_mid)
    print("t2_center: %s" % t2_center)
    print("t2_side: %s" % t2_side)

    # Sin(a_1) = Opp/Hyp
    # Again we only know the Opp and the Hyp
    change_line = next_line.get_next()
    test_point_c_1 = change_line.start

    angle_c_1 = math.degrees(math.asin((change_line.end[1] - change_line.start[1]) / change_line.get_length()))

    # Sin(a_1) = Opp/Hyp
    # Now we know the angle and the Hyp
    test_point_c_1 = change_line.start
    opp = math.sin(math.radians(angle_c_1)) * t2_side
    adj = math.sqrt(math.pow(t2_side, 2) - math.pow(opp, 2))

    # TODO: Check if the minus plus thing gives problems later!
    test_point_c_2 = [test_point_c_1[0] - adj, test_point_c_1[1] + opp]

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
    draw_plane(_yertle, triangle_1_points)
    draw_plane(_yertle, triangle_2_points)

    new_plane_1_points = [
        test_point_b_1,
        next_line.start,
        next_line.end,
        test_point_c_2
    ]
    draw_plane(_yertle, new_plane_1_points)
    new_plane_2_points = [
        line.start,
        test_point_b_1,
        test_point_c_2,
        change_line.end
    ]
    # We don't draw the second plane because the plane below it will be the colour of this new plane.
    # draw_plane(_yertle, new_plane_2_points)
    plane_1 = Plane(new_plane_1_points)
    plane_2 = Plane(new_plane_2_points)
    return plane_1, plane_2

