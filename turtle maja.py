import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def ruut(suurus):
    for _ in range(4):
        t.forward(suurus)
        t.left(90)

def katus(suurus):
    t.left(45)
    t.forward(suurus / 1.4)
    t.left(270)
    t.forward(suurus / 1.4)
    t.left(135)

def uks(suurus):
    t.color("blue")
    t.forward(suurus / 3)
    t.left(90)
    t.forward(suurus / 2)
    t.left(90)
    t.forward(suurus / 3)
    t.left(90)
    t.forward(suurus / 2)
    t.left(90)
    t.color("black")

def maja(x, y, suurus):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

    ruut(suurus)

    t.left(90)
    t.forward(suurus)
    t.right(90)
    t.color("green")
    katus(suurus)
    t.color("black")

    t.penup()
    t.goto(x + suurus / 3, y)
    t.setheading(0)
    t.pendown()
    uks(suurus)

x = -300
maja(x, -150, 60)
maja(x + 80, -150, 90)
maja(x + 180, -150, 130)
maja(x + 320, -150, 90)
maja(x + 420, -150, 60)
maja(x + 500, -150, 90)

turtle.done()