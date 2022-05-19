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
    next_line.get_length()

    angle_choice = _rand.randint(_index, len(angles) + _index)
    angle_choice -= _index
    angle_choice -= 1
    _index += 1

    angle = angles[angle_choice]
    print("angle")


