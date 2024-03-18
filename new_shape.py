import turtle

def draw_attractive_design2():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(0)
    turtle.bgcolor("black")
    pen.pensize(1)
    
    initial_size = 35
    
    for i in range(250):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(59) 
    
    pen.hideturtle()
    
draw_attractive_design2()
turtle.done() 