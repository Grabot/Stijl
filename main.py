import turtle
from turtle import Screen
import random
import numpy
import math

from objects.line import Line

colours = [
    ['maroon', '#800000', (128, 0, 0)],
    ['dark red', '#8B0000', (139, 0, 0)],
    ['brown', '#A52A2A', (165, 42, 42)],
    ['firebrick', '#B22222', (178, 34, 34)],
    ['crimson', '#DC143C', (220, 20, 60)],
    ['red', '#FF0000', (255, 0, 0)],
    ['tomato', '#FF6347', (255, 99, 71)],
    ['coral', '#FF7F50', (255, 127, 80)],
    ['indian red', '#CD5C5C', (205, 92, 92)],
    ['light coral', '#F08080', (240, 128, 128)],
    ['dark salmon', '#E9967A', (233, 150, 122)],
    ['salmon', '#FA8072', (250, 128, 114)],
    ['light salmon', '#FFA07A', (255, 160, 122)],
    ['orange red', '#FF4500', (255, 69, 0)],
    ['dark orange', '#FF8C00', (255, 140, 0)],
    ['orange', '#FFA500', (255, 165, 0)],
    ['gold', '#FFD700', (255, 215, 0)],
    ['dark golden rod', '#B8860B', (184, 134, 11)],
    ['golden rod', '#DAA520', (218, 165, 32)],
    ['pale golden rod', '#EEE8AA', (238, 232, 170)],
    ['dark khaki', '#BDB76B', (189, 183, 107)],
    ['khaki', '#F0E68C', (240, 230, 140)],
    ['olive', '#808000', (128, 128, 0)],
    ['yellow', '#FFFF00', (255, 255, 0)],
    ['yellow green', '#9ACD32', (154, 205, 50)],
    ['dark olive green', '#556B2F', (85, 107, 47)],
    ['olive drab', '#6B8E23', (107, 142, 35)],
    ['lawn green', '#7CFC00', (124, 252, 0)],
    ['chart reuse', '#7FFF00', (127, 255, 0)],
    ['green yellow', '#ADFF2F', (173, 255, 47)],
    ['dark green', '#006400', (0, 100, 0)],
    ['green', '#008000', (0, 128, 0)],
    ['forest green', '#228B22', (34, 139, 34)],
    ['lime', '#00FF00', (0, 255, 0)],
    ['lime green', '#32CD32', (50, 205, 50)],
    ['light green', '#90EE90', (144, 238, 144)],
    ['pale green', '#98FB98', (152, 251, 152)],
    ['dark sea green', '#8FBC8F', (143, 188, 143)],
    ['medium spring green', '#00FA9A', (0, 250, 154)],
    ['spring green', '#00FF7F', (0, 255, 127)],
    ['sea green', '#2E8B57', (46, 139, 87)],
    ['medium aqua marine', '#66CDAA', (102, 205, 170)],
    ['medium sea green', '#3CB371', (60, 179, 113)],
    ['light sea green', '#20B2AA', (32, 178, 170)],
    ['dark slate gray', '#2F4F4F', (47, 79, 79)],
    ['teal', '#008080', (0, 128, 128)],
    ['dark cyan', '#008B8B', (0, 139, 139)],
    ['aqua', '#00FFFF', (0, 255, 255)],
    ['cyan', '#00FFFF', (0, 255, 255)],
    ['light cyan', '#E0FFFF', (224, 255, 255)],
    ['dark turquoise', '#00CED1', (0, 206, 209)],
    ['turquoise', '#40E0D0', (64, 224, 208)],
    ['medium turquoise', '#48D1CC', (72, 209, 204)],
    ['pale turquoise', '#AFEEEE', (175, 238, 238)],
    ['aqua marine', '#7FFFD4', (127, 255, 212)],
    ['powder blue', '#B0E0E6', (176, 224, 230)],
    ['cadet blue', '#5F9EA0', (95, 158, 160)],
    ['steel blue', '#4682B4', (70, 130, 180)],
    ['corn flower blue', '#6495ED', (100, 149, 237)],
    ['deep sky blue', '#00BFFF', (0, 191, 255)],
    ['dodger blue', '#1E90FF', (30, 144, 255)],
    ['light blue', '#ADD8E6', (173, 216, 230)],
    ['sky blue', '#87CEEB', (135, 206, 235)],
    ['light sky blue', '#87CEFA', (135, 206, 250)],
    ['midnight blue', '#191970', (25, 25, 112)],
    ['navy', '#000080', (0, 0, 128)],
    ['dark blue', '#00008B', (0, 0, 139)],
    ['medium blue', '#0000CD', (0, 0, 205)],
    ['blue', '#0000FF', (0, 0, 255)],
    ['royal blue', '#4169E1', (65, 105, 225)],
    ['blue violet', '#8A2BE2', (138, 43, 226)],
    ['indigo', '#4B0082', (75, 0, 130)],
    ['dark slate blue', '#483D8B', (72, 61, 139)],
    ['slate blue', '#6A5ACD', (106, 90, 205)],
    ['medium slate blue', '#7B68EE', (123, 104, 238)],
    ['medium purple', '#9370DB', (147, 112, 219)],
    ['dark magenta', '#8B008B', (139, 0, 139)],
    ['dark violet', '#9400D3', (148, 0, 211)],
    ['dark orchid', '#9932CC', (153, 50, 204)],
    ['medium orchid', '#BA55D3', (186, 85, 211)],
    ['purple', '#800080', (128, 0, 128)],
    ['thistle', '#D8BFD8', (216, 191, 216)],
    ['plum', '#DDA0DD', (221, 160, 221)],
    ['violet', '#EE82EE', (238, 130, 238)],
    ['magenta / fuchsia', '#FF00FF', (255, 0, 255)],
    ['orchid', '#DA70D6', (218, 112, 214)],
    ['medium violet red', '#C71585', (199, 21, 133)],
    ['pale violet red', '#DB7093', (219, 112, 147)],
    ['deep pink', '#FF1493', (255, 20, 147)],
    ['hot pink', '#FF69B4', (255, 105, 180)],
    ['light pink', '#FFB6C1', (255, 182, 193)],
    ['pink', '#FFC0CB', (255, 192, 203)],
    ['antique white', '#FAEBD7', (250, 235, 215)],
    ['beige', '#F5F5DC', (245, 245, 220)],
    ['bisque', '#FFE4C4', (255, 228, 196)],
    ['blanched almond', '#FFEBCD', (255, 235, 205)],
    ['wheat', '#F5DEB3', (245, 222, 179)],
    ['corn silk', '#FFF8DC', (255, 248, 220)],
    ['lemon chiffon', '#FFFACD', (255, 250, 205)],
    ['light golden rod yellow', '#FAFAD2', (250, 250, 210)],
    ['light yellow', '#FFFFE0', (255, 255, 224)],
    ['saddle brown', '#8B4513', (139, 69, 19)],
    ['sienna', '#A0522D', (160, 82, 45)],
    ['chocolate', '#D2691E', (210, 105, 30)],
    ['peru', '#CD853F', (205, 133, 63)],
    ['sandy brown', '#F4A460', (244, 164, 96)],
    ['burly wood', '#DEB887', (222, 184, 135)],
    ['tan', '#D2B48C', (210, 180, 140)],
    ['rosy brown', '#BC8F8F', (188, 143, 143)],
    ['moccasin', '#FFE4B5', (255, 228, 181)],
    ['navajo white', '#FFDEAD', (255, 222, 173)],
    ['peach puff', '#FFDAB9', (255, 218, 185)],
    ['misty rose', '#FFE4E1', (255, 228, 225)],
    ['lavender blush', '#FFF0F5', (255, 240, 245)],
    ['linen', '#FAF0E6', (250, 240, 230)],
    ['old lace', '#FDF5E6', (253, 245, 230)],
    ['papaya whip', '#FFEFD5', (255, 239, 213)],
    ['sea shell', '#FFF5EE', (255, 245, 238)],
    ['mint cream', '#F5FFFA', (245, 255, 250)],
    ['slate gray', '#708090', (112, 128, 144)],
    ['light slate gray', '#778899', (119, 136, 153)],
    ['light steel blue', '#B0C4DE', (176, 196, 222)],
    ['lavender', '#E6E6FA', (230, 230, 250)],
    ['floral white', '#FFFAF0', (255, 250, 240)],
    ['alice blue', '#F0F8FF', (240, 248, 255)],
    ['ghost white', '#F8F8FF', (248, 248, 255)],
    ['honeydew', '#F0FFF0', (240, 255, 240)],
    ['ivory', '#FFFFF0', (255, 255, 240)],
    ['azure', '#F0FFFF', (240, 255, 255)],
    ['snow', '#FFFAFA', (255, 250, 250)],
    ['black', '#000000', (0, 0, 0)],
    ['dim gray / dim grey', '#696969', (105, 105, 105)],
    ['gray / grey', '#808080', (128, 128, 128)],
    ['dark gray / dark grey', '#A9A9A9', (169, 169, 169)],
    ['silver', '#C0C0C0', (192, 192, 192)],
    ['light gray / light grey', '#D3D3D3', (211, 211, 211)],
    ['gainsboro', '#DCDCDC', (220, 220, 220)],
    ['white smoke', '#F5F5F5', (245, 245, 245)],
    ['white', '#FFFFFF', (255, 255, 255)]
]


def background_square(_t, _rand, _width, _height, _index):
    colour_index = _rand.randint(_index, len(colours) + _index)
    colour_index -= _index
    _t.fillcolor(colours[colour_index][1])

    plane_points = [[0, 0], [0, _height], [_width, _height], [_width, 0]]
    line1 = Line([0, 0], [0, _height])
    line2 = Line([0, _height], [_width, _height])
    line3 = Line([_width, _height], [_width, 0])
    line4 = Line([_width, 0], [0, 0])

    _t.penup()
    _t.goto(line1.start[0], line1.start[1])
    _t.pendown()

    _t.begin_fill()
    _t.goto(line1.end[0], line1.end[1])
    _t.goto(line2.end[0], line2.end[1])
    _t.goto(line3.end[0], line3.end[1])
    _t.goto(line4.end[0], line4.end[1])
    _t.end_fill()


def add_random_triangle(_t, _rand, _width, _height, _index):
    print("add triangle")
    colour_index = _rand.randint(_index, len(colours) + _index)
    colour_index -= _index
    _t.fillcolor(colours[colour_index][1])
    print("colour_index: %s" % colour_index)
    _index += 1


if __name__ == '__main__':
    random.seed("test")
    
    width = 800
    height = 600
    screen = Screen()
    screen.setup(width+5, height+5)
    screen.setworldcoordinates(0, 0, width+5, height+5)
    # screen.tracer(False)

    turtle.hideturtle()
    t = turtle.Turtle(visible=False)
    t.speed(1)

    # Add an index so that we can pick new colours from the same list using the same seed and get a new one every time.
    index = 0
    background_square(t, random, width, height, index)
    index += 1

    triangle_numbers = random.randint(0, 20)

    add_random_triangle(t, random, width, height, index)
    # for t in range(0, triangle_numbers):
    #     add_random_triangle(random, width, height)
    index += triangle_numbers
    print(triangle_numbers)

    turtle.Screen().exitonclick()

