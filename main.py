import pygame
from snake import Snake 
from apple import Apple
pygame.init()

pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((600, 500))
snake = Snake()
apple = Apple()
clock = pygame.time.Clock()

def check_collision_player_contacted_wall():
    if snake.head_snake_x < 0 or snake.head_snake_x > 600 or snake.head_snake_y < 0 or snake.head_snake_y > 500:
        return True
    else:
        return False
    
def check_collision_player_contacted_apple():
    if snake.head_snake_x == apple.apple_x and snake.head_snake_y == apple.apple_y:
        return True
    else:
        return False

def check_collision_snake_touch_snake():
    for body in snake.body_list:
        if snake.head_snake_x == body[0] and snake.head_snake_y == body[1]:
            return True
    return False

def gameover():
    screen.fill((56,56,59))
    gameover_text = font.render("Score:" + str(score) + " Game Over", True, (255, 255, 255))
    screen.blit(gameover_text, (200, 225))

font = pygame.font.Font("freesansbold.ttf", 20)

def show_score(): 
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

score = 0

pausing = False
running = True 
while running:
    screen.fill((56,56,59))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if check_collision_player_contacted_wall() == True:
        gameover()
        pausing = True
    if check_collision_snake_touch_snake() == True:
        gameover()
        pausing = True
    if check_collision_player_contacted_apple() == True:
        score = score + 1
        apple.teleportation_apple()
        snake.move(event, screen, True)
    else:
         snake.move(event, screen, False)
    if pausing == False:
        show_score()
        snake.draw_snake(screen)
        apple.draw_apple(screen)
    
        
    pygame.display.update()
    clock.tick(5)
