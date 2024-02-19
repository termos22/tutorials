import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(100000)
myWin = turtle.Screen()
myWin.bgcolor("#263137")
my_turtle.color("#fe5151")

distance = 10
for i in range(100):
    for _ in range(4):
        my_turtle.forward(distance)
        my_turtle.right(90)
    my_turtle.right(10)
    distance += 2
