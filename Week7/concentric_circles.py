import turtle

NUM_CIRCLES = int(turtle.numinput("NUM_CIRCLES","Enter the number of circles: "))
STARTING_RADIUS = int(turtle.numinput("STARTING_RADIUS","Enter the starting radius: "))
OFFSET = int(turtle.numinput("OFFSET","Enter the offset: "))
ANIMATION_SPEED = 0

#set environment
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()
radius = STARTING_RADIUS

for count in range(NUM_CIRCLES):
    radius += OFFSET
    turtle.circle(radius)
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.done()