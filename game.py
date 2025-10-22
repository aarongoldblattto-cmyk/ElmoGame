import pygame
import sys
import io
import requests

times = 0

pygame.init()

url = "https://static.wikia.nocookie.net/muppet/images/5/5a/Elmo-elmo-elmo.jpg/revision/latest?cb=20110917000614"
response = requests.get(url)
image_bytes = io.BytesIO(response.content)
image = pygame.image.load(image_bytes)


WIDTH,HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tried to close the window " + str(times) + " times")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ELMO_WIDTH, ELMO_HEIGHT = WIDTH, HEIGHT

image = pygame.transform.smoothscale(image, (ELMO_WIDTH, ELMO_HEIGHT))

FLASH_INTERVAL_MS = 5000  
next_toggle = pygame.time.get_ticks() + FLASH_INTERVAL_MS
show_elmo = True

clock = pygame.time.Clock()
FPS = 60
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            times += 1
            pygame.display.set_caption("Tried to close the window " + str(times) + " times")
            FLASH_INTERVAL_MS -= 100


    now = pygame.time.get_ticks()
    if now >= next_toggle:
        show_elmo = not show_elmo
        next_toggle = now + FLASH_INTERVAL_MS
    screen.fill(BLACK)

    if show_elmo:
        screen.blit(image, (0, 0))
    else:
        screen.fill(WHITE)

    pygame.display.flip()