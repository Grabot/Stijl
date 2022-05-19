import math

from objects.line import Line
from util.colours import colours


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

    angle = angles[angle_choice]

    # Sin(a_1) = Opp/Hyp
    # First we don't know the angle, but we know the Opp and Hyp
    angle_1 = math.degrees(math.asin((line.end[1] - line.start[1]) / line.get_length()))

    # Sin(a_1) = Opp/Hyp
    # Now we know the angle and the Hyp
    test_point_a_1 = line.start
    Opp = math.sin(math.radians(angle_1)) * line_length_choice
    Adj = math.sqrt(math.pow(line_length_choice, 2) - math.pow(Opp, 2))

    test_point_a_2 = [test_point_a_1[0] + Adj, test_point_a_1[1] + Opp]

    test_point_b_1 = [test_point_a_1[0] + Adj, test_point_a_1[1] + Opp]
    test_point_b_2 = line.end

    new_line_1 = Line(test_point_a_1, test_point_a_2)
    new_line_2 = Line(test_point_b_1, test_point_b_2)

    # _yertle.penup()
    # _yertle.goto(test_point_b_1[0], test_point_b_1[1])
    # _yertle.pendown()
    print("angle")


