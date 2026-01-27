import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def ristkylik(laius, korgus):
    for _ in range(2):
        t.forward(laius)
        t.left(90)
        t.forward(korgus)
        t.left(90)


t.penup()
t.goto(-180, -40)
t.setheading(0)
t.pendown()
ristkylik(260, 60)

t.penup()
t.goto(-40, 20)
t.setheading(0)
t.pendown()
ristkylik(260, 60)


t.penup()
t.goto(140, -240)
t.setheading(90)
t.pendown()
ristkylik(260, 60)


t.penup()
t.goto(-40, 20)
t.setheading(90)
t.pendown()
ristkylik(180, 60)

turtle.done()