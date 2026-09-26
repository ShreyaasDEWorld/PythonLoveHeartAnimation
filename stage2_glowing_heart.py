import pygame
import math

# ==========================================
# 1. INITIALIZE
# ==========================================

pygame.init()

WIDTH = 900
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Python ❤️ Glowing Heart")

clock = pygame.time.Clock()


# ==========================================
# 2. COLORS
# ==========================================

BLACK = (0, 0, 0)

HEART_COLOR = (255, 40, 120)


# ==========================================
# 3. HEART EQUATION
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

def create_heart(scale):

    points = []

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    for i in range(1000):

        t = (2 * math.pi * i) / 1000

        x = center_x + heart_x(t, scale)

        y = center_y - heart_y(t, scale)

        points.append((x, y))

    return points


# ==========================================
# 5. CREATE TRANSPARENT GLOW SURFACE
# ==========================================

glow_surface = pygame.Surface(
    (WIDTH, HEIGHT),
    pygame.SRCALPHA
)


# ==========================================
# 6. MAIN LOOP
# ==========================================

running = True

time_value = 0


while running:

    # --------------------------------------
    # EVENTS
    # --------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # --------------------------------------
    # TIME
    # --------------------------------------

    time_value += 0.05


    # --------------------------------------
    # HEART PULSE
    # --------------------------------------

    pulse = math.sin(time_value) * 1.5

    scale = 20 + pulse


    # --------------------------------------
    # CREATE HEART
    # --------------------------------------

    heart_points = create_heart(scale)


    # --------------------------------------
    # CLEAR SCREEN
    # --------------------------------------

    screen.fill(BLACK)


    # ======================================
    # CLEAR GLOW SURFACE
    # ======================================

    glow_surface.fill((0, 0, 0, 0))


    # ======================================
    # OUTER GLOW
    # ======================================

    for point in heart_points:

        pygame.draw.circle(
            glow_surface,
            (255, 0, 80, 20),
            (int(point[0]), int(point[1])),
            12
        )


    # ======================================
    # SECOND GLOW
    # ======================================

    for point in heart_points:

        pygame.draw.circle(
            glow_surface,
            (255, 0, 100, 35),
            (int(point[0]), int(point[1])),
            8
        )


    # ======================================
    # INNER GLOW
    # ======================================

    for point in heart_points:

        pygame.draw.circle(
            glow_surface,
            (255, 40, 130, 60),
            (int(point[0]), int(point[1])),
            5
        )


    # ======================================
    # DRAW GLOW
    # ======================================

    screen.blit(
        glow_surface,
        (0, 0)
    )


    # ======================================
    # MAIN HEART
    # ======================================

    for point in heart_points:

        pygame.draw.circle(
            screen,
            HEART_COLOR,
            (int(point[0]), int(point[1])),
            2
        )


    # ======================================
    # UPDATE SCREEN
    # ======================================

    pygame.display.flip()

    clock.tick(60)


pygame.quit()