import pygame
import math
import random


# ============================================================
# 1. INITIALIZE
# ============================================================

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(
    "Stage 3 - I Love You ❤️"
)

clock = pygame.time.Clock()


# ============================================================
# 2. COLORS
# ============================================================

BLACK = (0, 0, 0)

PINK = (255, 80, 150)

LIGHT_PINK = (255, 170, 210)

WHITE = (255, 255, 255)


# ============================================================
# 3. FONT
# ============================================================

font = pygame.font.SysFont(
    "Arial",
    12,
    bold=True
)


# ============================================================
# 4. HEART EQUATION
# ============================================================

def heart_x(t, scale):

    return (
        scale *
        16 *
        math.sin(t) ** 3
    )


def heart_y(t, scale):

    return (
        scale *
        (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )
    )


# ============================================================
# 5. CREATE HEART POSITIONS
# ============================================================

def create_heart_positions():

    positions = []

    scale = 20

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Number of text particles

    total_particles = 300

    for i in range(total_particles):

        t = (
            2 *
            math.pi *
            i /
            total_particles
        )

        x = (
            center_x +
            heart_x(t, scale)
        )

        y = (
            center_y -
            heart_y(t, scale)
        )

        positions.append(
            (x, y)
        )

    return positions


# ============================================================
# 6. CREATE PARTICLES
# ============================================================

heart_positions = create_heart_positions()


particles = []


for x, y in heart_positions:

    particle = {

        "x": x,

        "y": y,

        "text": random.choice([
            "I love you",
            "I love you",
            "I love you",
            "❤️"
        ]),

        "size": random.randint(
            10,
            14
        ),

        "alpha": random.randint(
            150,
            255
        )

    }

    particles.append(
        particle
    )


# ============================================================
# 7. MAIN LOOP
# ============================================================

running = True

time_value = 0


while running:

    # ========================================================
    # EVENTS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # ========================================================
    # TIME
    # ========================================================

    time_value += 0.04


    # ========================================================
    # HEARTBEAT
    # ========================================================

    pulse = (
        math.sin(time_value)
        * 1.5
    )


    # ========================================================
    # BACKGROUND
    # ========================================================

    screen.fill(BLACK)


    # ========================================================
    # DRAW GLOW
    # ========================================================

    glow_surface = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )


    for particle in particles:

        x = particle["x"]

        y = particle["y"]


        # Outer glow

        pygame.draw.circle(

            glow_surface,

            (255, 0, 120, 20),

            (
                int(x),
                int(y)
            ),

            14
        )


        # Inner glow

        pygame.draw.circle(

            glow_surface,

            (255, 50, 150, 35),

            (
                int(x),
                int(y)
            ),

            8
        )


    screen.blit(
        glow_surface,
        (0, 0)
    )


    # ========================================================
    # DRAW TEXT PARTICLES
    # ========================================================

    for particle in particles:

        x = particle["x"]

        y = particle["y"]

        text = particle["text"]


        # ------------------------------------
        # Create text
        # ------------------------------------

        text_surface = font.render(
            text,
            True,
            LIGHT_PINK
        )


        # ------------------------------------
        # Position text
        # ------------------------------------

        text_rect = (
            text_surface.get_rect()
        )


        text_rect.center = (
            int(x),
            int(y)
        )


        # ------------------------------------
        # Draw text
        # ------------------------------------

        screen.blit(
            text_surface,
            text_rect
        )


    # ========================================================
    # DISPLAY
    # ========================================================

    pygame.display.flip()

    clock.tick(60)


pygame.quit()