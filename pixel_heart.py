import pygame
import math
import random

# -----------------------------
# Initialize Pygame
# -----------------------------

pygame.init()

WIDTH = 800
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("❤️ Python Pixel Heart")

clock = pygame.time.Clock()


# -----------------------------
# Colors
# -----------------------------

BLACK = (0, 0, 0)
RED = (255, 30, 80)
PINK = (255, 100, 150)
WHITE = (255, 255, 255)


# -----------------------------
# Heart equation
# -----------------------------

def inside_heart(x, y):

    value = (
        (x * x + y * y - 1) ** 3
        - x * x * y ** 3
    )

    return value <= 0


# -----------------------------
# Create heart pixels
# -----------------------------

pixels = []

pixel_size = 4

for x in range(-300, 301, pixel_size):

    for y in range(-280, 281, pixel_size):

        # Convert coordinates
        hx = x / 200
        hy = -y / 200

        if inside_heart(hx, hy):

            # Random brightness
            brightness = random.randint(180, 255)

            color = (
                brightness,
                random.randint(20, 80),
                random.randint(60, 120)
            )

            pixels.append(
                (x, y, color)
            )


# -----------------------------
# Animation
# -----------------------------

running = True

scale = 1.0
growing = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLACK)


    # -----------------------------
    # Pulse effect
    # -----------------------------

    if growing:

        scale += 0.003

        if scale >= 1.08:
            growing = False

    else:

        scale -= 0.003

        if scale <= 1.0:
            growing = True


    # -----------------------------
    # Draw every pixel
    # -----------------------------

    for x, y, color in pixels:

        new_x = int(
            WIDTH / 2 + x * scale
        )

        new_y = int(
            HEIGHT / 2 + y * scale
        )

        pygame.draw.rect(
            screen,
            color,
            (
                new_x,
                new_y,
                pixel_size,
                pixel_size
            )
        )


    # -----------------------------
    # Display text
    # -----------------------------

    font = pygame.font.SysFont(
        "Arial",
        32,
        bold=True
    )

    text = font.render(
        "I ❤️ Python",
        True,
        WHITE
    )

    text_rect = text.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    screen.blit(text, text_rect)


    pygame.display.flip()

    clock.tick(60)


pygame.quit()