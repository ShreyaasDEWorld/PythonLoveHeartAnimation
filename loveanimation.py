import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️ Heart Animation")

# Turtle setup
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.color("red")
heart.fillcolor("red")

# Draw heart using mathematical coordinates
def draw_heart(scale):
    heart.clear()

    heart.penup()

    points = []

    for i in range(361):
        t = math.radians(i)

        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        points.append((x * scale, y * scale))

    heart.goto(points[0])

    heart.pendown()
    heart.begin_fill()

    for x, y in points:
        heart.goto(x, y)

    heart.end_fill()


# Animation
scale = 10
growing = True

while True:

    draw_heart(scale)

    if growing:
        scale += 0.3

        if scale >= 12:
            growing = False

    else:
        scale -= 0.3

        if scale <= 10:
            growing = True

    time.sleep(0.03)

screen.mainloop()