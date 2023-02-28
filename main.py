import pygame, sys
from ship import Ship

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# ==================
# Ship code
spaceship_group = pygame.sprite.GroupSingle() # Create sprite group
spaceship = Ship(spaceship_group, WIDTH, HEIGHT) # Create ship object with a group as a parameter
# ==================

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick() / 1000 # Get a delta time in seconds

    spaceship_group.draw(screen)

    pygame.display.update()