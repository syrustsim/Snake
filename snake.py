import pygame

class Snake:

    def __init__(self):
        self.head_snake_x = 250
        self.head_snake_y = 250
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.speed = 3
        self.height = 25
        self.width = 25
        self.x_change = 0
        self.y_change = 0
        self.body_list = []

    def draw_snake(self, screen):
        GREEN = (0, 255, 0)
        pygame.draw.rect(screen, GREEN, (self.head_snake_x, self.head_snake_y, self.width, self.height))
        for body in self.body_list:
            pygame.draw.rect(screen, GREEN, (body[0], body[1], self.width, self.height))


    def move(self, event, screen, collision):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.move_right == False:
                self.x_change = -25
                self.y_change = 0 
                self.move_left = True
                self.move_right = False
                self.move_up = False
                self.move_down = False
                
            if event.key == pygame.K_RIGHT and self.move_left == False:
                self.x_change = 25
                self.y_change = 0
                self.move_right = True
                self.move_up = False
                self.move_down = False
                self.move_left = False
                
            if event.key == pygame.K_UP and self.move_down == False:
                self.y_change = -25
                self.x_change = 0
                self.move_up = True
                self.move_right = False
                self.move_left = False
                self.move_down = False
                
            if event.key == pygame.K_DOWN and self.move_up == False:
                self.y_change = 25
                self.x_change = 0
                self.move_down = True
                self.move_right = False
                self.move_left = False
                self.move_up = False
        self.body_list.insert(0, [self.head_snake_x, self.head_snake_y])
        self.head_snake_x += self.x_change
        self.head_snake_y += self.y_change

        if collision == False: 
            self.body_list.pop(-1)
            



