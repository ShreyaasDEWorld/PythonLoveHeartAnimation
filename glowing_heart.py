import turtle
import math
import time

# -----------------------------
# Screen setup
# -----------------------------

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️ Pulsing Glowing Heart")
screen.setup(width=800, height=700)

# Turn off automatic screen updates
screen.tracer(0)


# -----------------------------
# Create turtles
# -----------------------------

glow1 = turtle.Turtle()
glow2 = turtle.Turtle()
glow3 = turtle.Turtle()
heart = turtle.Turtle()

for t in [glow1, glow2, glow3, heart]:
    t.hideturtle()
    t.speed(0)
    t.penup()


# -----------------------------
# Heart coordinates
# -----------------------------

def heart_points(scale):

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

    return points


# -----------------------------
# Draw a heart
# -----------------------------

def draw_heart(turtle_obj, scale, color):

    points = heart_points(scale)

    turtle_obj.clear()
    turtle_obj.color(color)
    turtle_obj.fillcolor(color)

    turtle_obj.goto(points[0])
    turtle_obj.pendown()

    turtle_obj.begin_fill()

    for x, y in points:
        turtle_obj.goto(x, y)

    turtle_obj.end_fill()

    turtle_obj.penup()


# -----------------------------
# Animation variables
# -----------------------------

scale = 10
growing = True


# -----------------------------
# Animation loop
# -----------------------------

while True:

    # Glow layers
    draw_heart(glow3, scale + 2.5, "#330000")
    draw_heart(glow2, scale + 1.7, "#660000")
    draw_heart(glow1, scale + 0.9, "#990000")

    # Main heart
    draw_heart(heart, scale, "#ff1744")

    # Pulse
    if growing:

        scale += 0.18

        if scale >= 12:

            growing = False

    else:

        scale -= 0.18

        if scale <= 10:

            growing = True

    # Update screen
    screen.update()

    time.sleep(0.03)