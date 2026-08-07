import pygame 
import random

class Apple:

    def __init__(self):
        self.apple_x = random.randint(0,775)
        self.apple_y = random.randint(0, 575)
        self.apple_image = pygame.image.load('apple.png')
        self.resized_image = pygame.transform.scale(self.apple_image, (25,25))
    def draw_apple(self, screen):
        screen.blit(self.resized_image, (self.apple_x, self.apple_y))
    