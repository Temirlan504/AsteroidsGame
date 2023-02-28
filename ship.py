import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, screen_width, screen_height): # Initializing child class
        super().__init__(groups) # Initializing parent class and passing sprite groups
        self.image = pygame.image.load("graphics/ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32,32))
        # Place center of that image on the center of the screen
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height/2))

    def mouse_follow(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = mouse_pos[0]
        self.rect.centery = mouse_pos[1]

    def run(self):
        self.mouse_follow()