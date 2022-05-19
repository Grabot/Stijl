from objects.line import Line


class Plane:

    def __init__(self, points):
        self.points = points
        # The plane will always be a rectangle with 4 lines
        line1 = Line(points[0], points[1])
        line2 = Line(points[1], points[2])
        line3 = Line(points[2], points[3])
        line4 = Line(points[3], points[0])
        line1.set_next(line2)
        line2.set_next(line3)
        line3.set_next(line4)
        line4.set_next(line1)
        self.lines = [
            line1,
            line2,
            line3,
            line4
        ]

    def get_line(self, line_choice):
        return self.lines[line_choice]

