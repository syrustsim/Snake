import pygame 
import random

class Apple:

    def __init__(self):
        self.apple_x = random.randrange(0, 575, 25)
        self.apple_y = random.randrange(0, 475, 25)
        self.apple_image = pygame.image.load('apple.png')
        self.resized_image = pygame.transform.scale(self.apple_image, (25,25))
        print(self.apple_x, self.apple_y)
    def draw_apple(self, screen):
        screen.blit(self.resized_image, (self.apple_x, self.apple_y))

    def teleportation_apple(self):
        self.apple_x = random.randrange(0, 575, 25)
        self.apple_y = random.randrange(0, 475, 25)
    