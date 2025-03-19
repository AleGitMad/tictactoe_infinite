import pygame
import random

# Dimensioni finestra
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 9
COLUMNS = 3
ROWS = 3
CELL_SIZE = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite TicTacToe")

# Colori
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREY = (40, 40, 40)