import turtle

alex = turtle.Turtle()
wn = turtle.Screen()
alex.pensize(3)


def forwards():
    alex.forward(10)


def backwards():
    alex.backward(10)


def counter_clockwise():
    alex.left(10)


def clockwise():
    alex.right(10)


def reset():
    wn.resetscreen()


def etch_a_sketch():
    wn.listen()
    wn.onkey(key="w", fun=forwards)
    wn.onkey(key="s", fun=backwards)
    wn.onkey(key="a", fun=counter_clockwise)
    wn.onkey(key="d", fun=clockwise)
    wn.onkey(key="c", fun=reset)


etch_a_sketch()

wn.exitonclick()
