import turtle

turtle.showturtle

for i in range(4):
    turtle.circle(50)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    if i == 1:
        turtle.pencolor("red")
    if i == 2:
        turtle.pencolor("bule")
    if i == 3:
        turtle.pencolor("green")


