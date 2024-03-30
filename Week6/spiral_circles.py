import turtle
NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 360 / NUM_CIRCLES
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)

for i in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()