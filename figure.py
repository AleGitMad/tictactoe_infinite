import pygame
import random
from dimensions import *
from functions import *

class Figure(pygame.sprite.Sprite):
    def __init__(self, shape, x, y, time):
        super().__init__()
        self.shape = shape
        self.x = x
        self.y = y
        if shape == 'X':
            self.color = BLUE
        else:
            self.color = RED
        self.position = get_position(x, y)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.time = time
        
        # Calcola il centro della cella
        center_x = CELL_SIZE // 2
        center_y = CELL_SIZE // 2

        # Offset per disegnare le X e O più piccole della cella
        padding = CELL_SIZE // 4  # Margine intorno alle forme

        if self.shape == 'X':
            pygame.draw.line(self.image, self.color, 
                             (center_x - padding, center_y - padding), 
                             (center_x + padding, center_y + padding), 5)
            pygame.draw.line(self.image, self.color, 
                             (center_x + padding, center_y - padding), 
                             (center_x - padding, center_y + padding), 5)
        else:  # Disegna un O centrato
            pygame.draw.ellipse(self.image, self.color, 
                                (center_x - padding, center_y - padding, 
                                 2 * padding, 2 * padding), 5)
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def draw(self, screen):
        row = (self.position - 1) // COLUMNS
        col = (self.position - 1) % COLUMNS

        # Calcola il centro della cella
        x = col * CELL_SIZE
        y = row * CELL_SIZE

        screen.blit(self.image, (x, y))

    def update(self, counter, map):
        if counter == self.time + 7:
            for group in self.groups():
                group.remove(self)
                map.remove(self.position)