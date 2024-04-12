import turtle

def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def complexshape(lenthen,number,color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(number):
        turtle.forward(lenthen)
        turtle.right(360/number)
    turtle.end_fill()

draw_square(20)
draw_square(40)
complexshape(100,4,"red")
complexshape(200,8,"blue")
turtle.done()