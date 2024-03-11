import turtle
t = turtle.Turtle()

winw = turtle.Screen()
winw.tracer(1,0.1)
t.speed(1)


t.penup()
t.goto(-375,-100)
t.color("red")
t.setheading(94)
t.pendown()

t.begin_fill()
for i in range(2):
    t.circle(-2500,8,20)
    t.circle(-90,79)
    t.circle(-2500,14,20)
    t.circle(-90,79)

t.end_fill()

t.penup()
t.goto(125,80)
t.setheading(90)
t.pendown()
t.color("white")

t.begin_fill()
t.circle(125,360,3)
t.end_fill()

t.hideturtle()
turtle.done()
