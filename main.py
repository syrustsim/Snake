import pygame
from snake import Snake 
from apple import Apple
pygame.init()

pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((800, 600))
snake = Snake()
apple = Apple()
clock = pygame.time.Clock()

running = True 
while running:
    screen.fill((56,56,59))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    snake.draw_snake(screen)
    apple.draw_apple(screen)
    snake.move(event, screen)
    pygame.display.update()
    clock.tick(40)