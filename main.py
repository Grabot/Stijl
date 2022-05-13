import turtle


if __name__ == '__main__':
    print("Hello world")
    turtle.hideturtle()
    s = turtle.getscreen()
    t = turtle.Turtle(visible=False)

    t.fillcolor('blue')
    t.begin_fill()
    t.goto(0, 100)
    t.goto(100, 100)
    t.goto(100, 0)
    t.goto(0, 0)
    t.end_fill()

    turtle.Screen().exitonclick()

