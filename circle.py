import turtle

def draw_turtle():
    window = turtle.Screen()
    window.bgcolor("black")

    amin = turtle.Turtle()
    amin.color("orange")
    amin.shape("turtle")

    for i in range(36):
        amin.forward(100)
        amin.left(30)
        amin.forward(100)
        amin.color("white")
        amin.circle(20)
        amin.color("orange")
        amin.left(150)
        amin.forward(100)
        amin.left(30)
        amin.forward(100)
        amin.left(160)
    
    amin.right(90)
    amin.forward(300)

    window.exitonclick()

draw_turtle()
