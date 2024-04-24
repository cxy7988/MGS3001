import turtle
def main():
    turtle.hideturtle()
    square(100,0,50,'blue')
    turtle.done()
def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(2):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

if __name__ == '__main__':
    main()
