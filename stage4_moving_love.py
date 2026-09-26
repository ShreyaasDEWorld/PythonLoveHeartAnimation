import pygame
import math
import random


# ============================================================
# 1. INITIALIZE
# ============================================================

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Stage 4 - Moving I Love You ❤️"
)

clock = pygame.time.Clock()


# ============================================================
# 2. COLORS
# ============================================================

BLACK = (0, 0, 0)

PINK = (255, 80, 150)

LIGHT_PINK = (255, 180, 220)

BRIGHT_PINK = (255, 220, 240)


# ============================================================
# 3. HEART SETTINGS
# ============================================================

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

SCALE = 20

NUMBER_OF_WORDS = 120

SPEED = 0.0018


# ============================================================
# 4. HEART EQUATION
# ============================================================

def heart_x(t):

    return (
        16 *
        math.sin(t) ** 3
    )


def heart_y(t):

    return (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )


# ============================================================
# 5. CREATE FONT
# ============================================================

font_small = pygame.font.SysFont(
    "Arial",
    11,
    bold=True
)

font_medium = pygame.font.SysFont(
    "Arial",
    13,
    bold=True
)


# ============================================================
# 6. CREATE WORD PARTICLES
# ============================================================

particles = []


for i in range(NUMBER_OF_WORDS):

    # Spread words around complete heart

    starting_angle = (
        2 *
        math.pi *
        i /
        NUMBER_OF_WORDS
    )


    particle = {

        "angle": starting_angle,

        # Slight random distance from heart

        "offset": random.uniform(
            -1.5,
            1.5
        ),

        # Different speeds

        "speed": random.uniform(
            0.0008,
            0.0018
        ),

        # Random size

        "size": random.choice([
            "small",
            "small",
            "medium"
        ]),

        # Some brighter particles

        "bright": random.random() < 0.12

    }


    particles.append(
        particle
    )


# ============================================================
# 7. ANIMATION
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
        * 0.8
    )


    current_scale = (
        SCALE +
        pulse
    )


    # ========================================================
    # BACKGROUND
    # ========================================================

    screen.fill(BLACK)


    # ========================================================
    # GLOW SURFACE
    # ========================================================

    glow_surface = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )


    # ========================================================
    # UPDATE PARTICLES
    # ========================================================

    for particle in particles:


        # ----------------------------------------------------
        # Move around heart
        # ----------------------------------------------------

        particle["angle"] += (
            particle["speed"]
        )


        t = particle["angle"]


        # ----------------------------------------------------
        # Heart coordinates
        # ----------------------------------------------------

        x = (
            heart_x(t)
            *
            current_scale
        )


        y = (
            heart_y(t)
            *
            current_scale
        )


        # ----------------------------------------------------
        # Add small variation
        # ----------------------------------------------------

        x += (
            particle["offset"]
            *
            math.cos(t)
        )

        y += (
            particle["offset"]
            *
            math.sin(t)
        )


        # ----------------------------------------------------
        # Convert to screen coordinates
        # ----------------------------------------------------

        screen_x = (
            CENTER_X +
            x
        )

        screen_y = (
            CENTER_Y -
            y
        )


        # ====================================================
        # GLOW
        # ====================================================

        pygame.draw.circle(

            glow_surface,

            (255, 20, 130, 30),

            (
                int(screen_x),
                int(screen_y)
            ),

            14
        )


        pygame.draw.circle(

            glow_surface,

            (255, 70, 160, 45),

            (
                int(screen_x),
                int(screen_y)
            ),

            7
        )


        # ====================================================
        # TEXT
        # ====================================================

        if particle["bright"]:

            text_surface = font_medium.render(

                "I love you",

                True,

                BRIGHT_PINK

            )

        else:

            text_surface = font_small.render(

                "I love you",

                True,

                LIGHT_PINK

            )


        # ----------------------------------------------------
        # Calculate movement direction
        # ----------------------------------------------------

        next_t = t + 0.01


        next_x = (
            heart_x(next_t)
            *
            current_scale
        )


        next_y = (
            heart_y(next_t)
            *
            current_scale
        )


        dx = (
            next_x -
            x
        )


        dy = (
            -(next_y - y)
        )


        angle = math.degrees(
            math.atan2(
                dy,
                dx
            )
        )


        # ----------------------------------------------------
        # Rotate text
        # ----------------------------------------------------

        rotated_text = pygame.transform.rotate(
            text_surface,
            -angle
        )


        text_rect = (
            rotated_text.get_rect(
                center=(
                    int(screen_x),
                    int(screen_y)
                )
            )
        )


        screen.blit(
            rotated_text,
            text_rect
        )


    # ========================================================
    # DRAW GLOW
    # ========================================================

    screen.blit(
        glow_surface,
        (0, 0)
    )


    # ========================================================
    # DISPLAY
    # ========================================================

    pygame.display.flip()


    clock.tick(60)


pygame.quit()