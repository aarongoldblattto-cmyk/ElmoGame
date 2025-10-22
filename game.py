import pygame
import os
import sys

def resource_path(relative_path):
    """Get absolute path to assets (works with PyInstaller)."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

info = pygame.display.Info()

hand = 0

# Load Elmo image from local assets folder
image = pygame.image.load(resource_path("assets/elmo.png"))

WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tried to close the window 0 times")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.event.set_grab(True)


ELMO_WIDTH, ELMO_HEIGHT = WIDTH, HEIGHT
image = pygame.transform.smoothscale(image, (ELMO_WIDTH, ELMO_HEIGHT))

FLASH_INTERVAL_MS = 200
next_toggle = pygame.time.get_ticks() + FLASH_INTERVAL_MS
show_elmo = True

clock = pygame.time.Clock()
FPS = 60
times = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            times += 1
            pygame.display.set_caption("Tried to close the window " + str(times) + " times")

    now = pygame.time.get_ticks()
    if now >= next_toggle:
        show_elmo = not show_elmo
        next_toggle = now + FLASH_INTERVAL_MS
        if hand == 0:
            hand = 3
            pygame.mouse.set_pos((1300, 120))

        elif hand == 1:
            hand = 4
            pygame.mouse.set_pos((200, 120))

        elif hand == 3:
            hand = 1

        elif hand == 4:
            hand = 0
        
    screen.fill(BLACK if show_elmo else WHITE)

    if show_elmo:
        screen.blit(image, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)
