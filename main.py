import turtle
t = turtle.Pen()
colors = ["yellow", "red", "green", "purple"]
turtle.bgcolor("black")
for x in range(450):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(150)