import turtle
def tree(branchLen,t):
    angle = 30
    sf = 0.8
    if branchLen < 3:
        t.color("#ffd640")
        t.stamp()
        t.color("#fe5151")
    if branchLen < 3:
        return
    else:
        t.forward(branchLen)
        t.left(angle)
        tree(branchLen*sf ,t)
        t.right(angle * 2)
        tree(branchLen*sf ,t)
        t.left(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.bgcolor("#263137")
    t.left(90)
    