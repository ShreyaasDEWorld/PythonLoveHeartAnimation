import pygame
import math
import random


# ============================================================
# INITIALIZATION
# ============================================================

pygame.init()

WIDTH = 1100
HEIGHT = 800

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "❤️ Python Love Heart Animation"
)

clock = pygame.time.Clock()


# ============================================================
# COLORS
# ============================================================

BLACK = (2, 0, 8)

PINK = (255, 50, 140)

LIGHT_PINK = (255, 170, 215)

BRIGHT_PINK = (255, 225, 245)

DARK_PINK = (180, 20, 100)

WHITE = (255, 255, 255)


# ============================================================
# CENTER
# ============================================================

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2


# ============================================================
# HEART SETTINGS
# ============================================================

BASE_SCALE = 19

NUMBER_OF_LAYERS = 6

WORDS_PER_LAYER = 55

TOTAL_WORDS = (
    NUMBER_OF_LAYERS *
    WORDS_PER_LAYER
)


# ============================================================
# ANIMATION SETTINGS
# ============================================================

animation_speed = 0.0015

pulse_speed = 0.04

time_value = 0


# ============================================================
# FONTS
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

font_large = pygame.font.SysFont(
    "Arial",
    16,
    bold=True
)


# ============================================================
# HEART EQUATION
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
# PARTICLE CLASS
# ============================================================

class LoveParticle:

    def __init__(
        self,
        layer,
        index
    ):

        self.layer = layer

        self.index = index


        # -----------------------------------------
        # Starting position
        # -----------------------------------------

        self.angle = (
            2 *
            math.pi *
            index /
            WORDS_PER_LAYER
        )


        # -----------------------------------------
        # Layer distance
        # -----------------------------------------

        self.layer_offset = (
            layer -
            (NUMBER_OF_LAYERS - 1) / 2
        )


        # -----------------------------------------
        # Individual speed
        # -----------------------------------------

        self.speed = random.uniform(
            0.0007,
            0.0018
        )


        # -----------------------------------------
        # Random brightness
        # -----------------------------------------

        self.brightness = random.random()


        # -----------------------------------------
        # Text
        # -----------------------------------------

        self.text = random.choice(
            [
                "I love you",
                "I love you",
                "I love you",
                "❤️"
            ]
        )


        # -----------------------------------------
        # Size
        # -----------------------------------------

        self.size = random.choice(
            [
                "small",
                "small",
                "medium",
                "medium",
                "large"
            ]
        )


    # ========================================================
    # UPDATE
    # ========================================================

    def update(
        self,
        current_scale,
        mouse_x,
        mouse_y
    ):

        # -----------------------------------------
        # Move around heart
        # -----------------------------------------

        self.angle += (
            self.speed *
            animation_speed /
            0.0015
        )


        t = self.angle


        # -----------------------------------------
        # Heart coordinates
        # -----------------------------------------

        x = (
            heart_x(t) *
            current_scale
        )

        y = (
            heart_y(t) *
            current_scale
        )


        # -----------------------------------------
        # Multiple heart layers
        # -----------------------------------------

        offset = (
            self.layer_offset *
            7
        )


        distance = math.sqrt(
            x * x +
            y * y
        )


        if distance != 0:

            x += (
                x /
                distance *
                offset
            )

            y += (
                y /
                distance *
                offset
            )


        # -----------------------------------------
        # Screen position
        # -----------------------------------------

        screen_x = (
            CENTER_X +
            x
        )

        screen_y = (
            CENTER_Y -
            y
        )


        # -----------------------------------------
        # Mouse interaction
        # -----------------------------------------

        dx = (
            screen_x -
            mouse_x
        )

        dy = (
            screen_y -
            mouse_y
        )

        mouse_distance = math.sqrt(
            dx * dx +
            dy * dy
        )


        if mouse_distance < 150:

            force = (
                150 -
                mouse_distance
            ) / 150


            if mouse_distance > 0:

                screen_x += (
                    dx /
                    mouse_distance *
                    force *
                    35
                )

                screen_y += (
                    dy /
                    mouse_distance *
                    force *
                    35
                )


        return (
            screen_x,
            screen_y,
            t
        )


# ============================================================
# CREATE PARTICLES
# ============================================================

particles = []


for layer in range(
    NUMBER_OF_LAYERS
):

    for index in range(
        WORDS_PER_LAYER
    ):

        particles.append(
            LoveParticle(
                layer,
                index
            )
        )


# ============================================================
# BACKGROUND STARS
# ============================================================

stars = []


for i in range(180):

    stars.append(
        {
            "x": random.randint(
                0,
                WIDTH
            ),

            "y": random.randint(
                0,
                HEIGHT
            ),

            "size": random.randint(
                1,
                3
            ),

            "speed": random.uniform(
                0.2,
                1.0
            ),

            "brightness": random.randint(
                80,
                220
            )
        }
    )


# ============================================================
# MAIN LOOP
# ============================================================

running = True


while running:


    # ========================================================
    # EVENTS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        # -----------------------------------------
        # Keyboard
        # -----------------------------------------

        if event.type == pygame.KEYDOWN:


            # Increase speed

            if event.key == pygame.K_UP:

                animation_speed += 0.0003


            # Decrease speed

            if event.key == pygame.K_DOWN:

                animation_speed = max(
                    0.0002,
                    animation_speed - 0.0003
                )


            # Reset

            if event.key == pygame.K_SPACE:

                animation_speed = 0.0015


            # Escape

            if event.key == pygame.K_ESCAPE:

                running = False


    # ========================================================
    # TIME
    # ========================================================

    time_value += pulse_speed


    # ========================================================
    # HEARTBEAT
    # ========================================================

    heartbeat = (
        math.sin(time_value)
        * 1.2
    )


    current_scale = (
        BASE_SCALE +
        heartbeat
    )


    # ========================================================
    # BACKGROUND
    # ========================================================

    screen.fill(
        BLACK
    )


    # ========================================================
    # STARS
    # ========================================================

    for star in stars:

        star["y"] += (
            star["speed"]
        )


        if star["y"] > HEIGHT:

            star["y"] = 0


        brightness = int(
            star["brightness"]
            *
            (
                0.7 +
                0.3 *
                math.sin(
                    time_value *
                    star["speed"]
                )
            )
        )


        pygame.draw.circle(

            screen,

            (
                brightness,
                brightness,
                brightness
            ),

            (
                int(star["x"]),
                int(star["y"])
            ),

            star["size"]
        )


    # ========================================================
    # GLOW SURFACE
    # ========================================================

    glow_surface = pygame.Surface(
        (
            WIDTH,
            HEIGHT
        ),
        pygame.SRCALPHA
    )


    # ========================================================
    # MOUSE
    # ========================================================

    mouse_x, mouse_y = pygame.mouse.get_pos()


    # ========================================================
    # DRAW PARTICLES
    # ========================================================

    for particle in particles:


        # -----------------------------------------
        # Position
        # -----------------------------------------

        x, y, t = particle.update(
            current_scale,
            mouse_x,
            mouse_y
        )


        # -----------------------------------------
        # Glow
        # -----------------------------------------

        pygame.draw.circle(

            glow_surface,

            (
                255,
                20,
                130,
                25
            ),

            (
                int(x),
                int(y)
            ),

            14
        )


        pygame.draw.circle(

            glow_surface,

            (
                255,
                60,
                170,
                40
            ),

            (
                int(x),
                int(y)
            ),

            7
        )


        # -----------------------------------------
        # Select font
        # -----------------------------------------

        if particle.size == "large":

            font = font_large

        elif particle.size == "medium":

            font = font_medium

        else:

            font = font_small


        # -----------------------------------------
        # Select color
        # -----------------------------------------

        if particle.brightness > 0.85:

            color = BRIGHT_PINK

        elif particle.brightness > 0.45:

            color = LIGHT_PINK

        else:

            color = PINK


        # -----------------------------------------
        # Render text
        # -----------------------------------------

        text_surface = font.render(

            particle.text,

            True,

            color
        )


        # -----------------------------------------
        # Direction
        # -----------------------------------------

        next_t = (
            t +
            0.01
        )


        next_x = (
            heart_x(next_t) *
            current_scale
        )


        next_y = (
            heart_y(next_t) *
            current_scale
        )


        dx = (
            next_x -
            heart_x(t) *
            current_scale
        )


        dy = -(
            next_y -
            heart_y(t) *
            current_scale
        )


        angle = math.degrees(
            math.atan2(
                dy,
                dx
            )
        )


        # -----------------------------------------
        # Rotate text
        # -----------------------------------------

        rotated_text = (
            pygame.transform.rotate(
                text_surface,
                -angle
            )
        )


        text_rect = (
            rotated_text.get_rect(
                center=(
                    int(x),
                    int(y)
                )
            )
        )


        # -----------------------------------------
        # Draw
        # -----------------------------------------

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
    # CENTER MESSAGE
    # ========================================================

    center_font = pygame.font.SysFont(
        "Arial",
        24,
        bold=True
    )


    center_text = center_font.render(
        "I Love Python",
        True,
        WHITE
    )


    center_rect = (
        center_text.get_rect(
            center=(
                CENTER_X,
                CENTER_Y
            )
        )
    )


    screen.blit(
        center_text,
        center_rect
    )


    # ========================================================
    # UPDATE
    # ========================================================

    pygame.display.flip()

    clock.tick(60)


# ============================================================
# EXIT
# ============================================================

pygame.quit()