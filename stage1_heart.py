import pygame
import math

# ==========================================
# 1. INITIALIZE
# ==========================================

pygame.init()

WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Python ❤️ Mathematical Heart")

clock = pygame.time.Clock()


# ==========================================
# 2. COLORS
# ==========================================

BLACK = (0, 0, 0)
PINK = (255, 80, 150)


# ==========================================
# 3. HEART FUNCTION
# ==========================================

def heart_x(t, scale):

    return scale * 16 * math.sin(t) ** 3


def heart_y(t, scale):

    return scale * (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )


# ==========================================
# 4. CREATE HEART POINTS
# ==========================================

def create_heart():

    points = []

    scale = 20

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    for i in range(1000):

        t = (2 * math.pi * i) / 1000

        x = center_x + heart_x(t, scale)

        y = center_y - heart_y(t, scale)

        points.append((x, y))

    return points


heart_points = create_heart()


# ==========================================
# 5. MAIN LOOP
# ==========================================

running = True

while running:

    # --------------------------------------
    # Events
    # --------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # --------------------------------------
    # Background
    # --------------------------------------

    screen.fill(BLACK)


    # --------------------------------------
    # Draw heart
    # --------------------------------------

    for point in heart_points:

        pygame.draw.circle(
            screen,
            PINK,
            (int(point[0]), int(point[1])),
            2
        )


    # --------------------------------------
    # Update
    # --------------------------------------

    pygame.display.flip()

    clock.tick(60)


pygame.quit()