import turtle
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.clearscreen()
#
# for i in range(8):
#     turtle.forward(100)
#     turtle.right(45)
# turtle.clearscreen()

turtle.goto(-400,0)
for x in range(4):
    for y in range(4):
        turtle.pendown()
        if x % 2 == 0:
            if y % 2 == 0:
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("white")
        else:
            if y % 2 == 0:
                turtle.fillcolor("white")
            else:
                turtle.fillcolor("black")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(100)
        turtle.penup()
    turtle.goto(-400, turtle.ycor() - 100)
    turtle.pendown()


turtle.done()