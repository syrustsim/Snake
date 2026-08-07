import pygame
import random

class Snake:

    def __init__(self):
        self.head_snake_x = random.randint(100,700)
        self.head_snake_y = 500
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.speed = 3
        self.height = 25
        self.width = 25
        self.body_list = []

    def draw_snake(self, screen):
        GREEN = (0, 255, 0)
        pygame.draw.rect(screen, GREEN, (self.head_snake_x, self.head_snake_y, self.width, self.height))

    def move(self, event, screen):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left = True
            if event.key == pygame.K_RIGHT:
                self.move_right = True
            if event.key == pygame.K_UP:
                self.move_up = True
            if event.key == pygame.K_DOWN:
                self.move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_RIGHT:
                self.move_right = False
            if event.key == pygame.K_UP:
                self.move_up = False
            if event.key == pygame.K_DOWN:
                self.move_down = False
        direction = pygame.math.Vector2(0,0)
        if self.move_left:
            direction.x -= 1
        if self.move_right:
            direction.x += 1
        if self.move_up:
            direction.y -= 1
        if self.move_down:
            direction.y += 1
        if direction.length() > 0:
            direction = direction.normalize()*self.speed
        self.head_snake_x += direction.x
        self.head_snake_y += direction.y

