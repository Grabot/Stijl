import math


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = None

    def set_next(self, line):
        self.next = line

    def get_next(self):
        return self.next

    def get_length(self):
        x_length = abs(self.start[0] - self.end[0])
        y_length = abs(self.start[1] - self.end[1])
        return math.sqrt(math.pow(x_length, 2) + math.pow(y_length, 2))

