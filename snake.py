import pygame

class Snake:

    def __init__(self):
        self.head_snake_x = 250
        self.head_snake_y = 250
        self.speed = 3
        self.height = 25
        self.width = 25
        self.x_change = 0
        self.y_change = 0
        self.next_y_change = 0 
        self.next_x_change = 0
        self.body_list = []
        self.growth_pending = 0

    def draw_snake(self, screen):
        GREEN = (0, 255, 0)
        pygame.draw.rect(screen, GREEN, (self.head_snake_x, self.head_snake_y, self.width, self.height))
        for body in self.body_list:
            pygame.draw.rect(screen, GREEN, (body[0], body[1], self.width, self.height))

    def grow_snake(self):
        self.growth_pending += 5
    
    def handle_input(self, key):
        if key == pygame.K_LEFT and self.x_change == 0:
            self.next_x_change = -5
            self.next_y_change = 0 

        elif key == pygame.K_RIGHT and self.x_change == 0:
            self.next_x_change = 5
            self.next_y_change = 0
            
        elif key == pygame.K_UP and self.y_change == 0:
            self.next_x_change = 0
            self.next_y_change = -5
            
        elif key == pygame.K_DOWN and self.y_change == 0:
            self.next_x_change = 0
            self.next_y_change = 5


    def move(self):
        if self.head_snake_x % 25 == 0 and self.head_snake_y % 25 == 0:
            self.x_change = self.next_x_change
            self.y_change = self.next_y_change

        self.body_list.insert(0, [self.head_snake_x, self.head_snake_y])
        self.head_snake_x += self.x_change
        self.head_snake_y += self.y_change

        if self.growth_pending > 0:
            self.growth_pending -= 1
        else:
            if len(self.body_list) > 0: 
                self.body_list.pop(-1)
            



