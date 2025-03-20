import pygame
import figure
from dimensions import *

def get_position(x, y):
    position = 0
    if x < WIDTH // 3:
        if y < HEIGHT // 3:
            position = 1
        if y < HEIGHT // 3 * 2 and y >= HEIGHT // 3:
            position = 4
        if y >= HEIGHT // 3 * 2:
            position = 7
    if x < WIDTH // 3 * 2 and x >= WIDTH // 3:
        if y < HEIGHT // 3:
            position = 2
        if y < HEIGHT // 3 * 2 and y >= HEIGHT // 3:
            position = 5
        if y >= HEIGHT // 3 * 2:
            position = 8
    if x >= WIDTH // 3 * 2:
        if y < HEIGHT // 3:
            position = 3
        if y < HEIGHT // 3 * 2 and y >= HEIGHT // 3:
            position = 6
        if y >= HEIGHT // 3 * 2:
            position = 9
    return position