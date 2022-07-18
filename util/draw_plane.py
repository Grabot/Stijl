def draw_plane(_yertle, _points):

    _yertle.penup()
    _yertle.goto(_points[-1][0], _points[-1][1])
    _yertle.pendown()

    _yertle.begin_fill()
    for point in _points:
        _yertle.goto(point[0], point[1])
    _yertle.end_fill()
