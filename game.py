import pygame
import random
from figure import Figure
from dimensions import *

# Inizializza Pygame
pygame.init()

# Disegna la griglia
def draw_grid():
    for x in range(0, WIDTH, WIDTH // 3):
        pygame.draw.line(screen, DARK_GREY, (x, 0), (x, HEIGHT), 3)
    for y in range(0, HEIGHT, HEIGHT // 3):
        pygame.draw.line(screen, DARK_GREY, (0, y), (WIDTH, y), 3)

# Crea un oggetto font (Arial, 36 punti)
font = pygame.font.Font(None, 36)  # Usa None per il font di default

# Renderizza il testo (testo, anti-aliasing, colore)
text_surface = font.render("Hai perso!", True, RED)

# Ottieni il rettangolo del testo e posizionalo al centro
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

end = False

# Game loop
running = True
clock = pygame.time.Clock()
turn = 0
all_figures = pygame.sprite.Group()
counter = 0
draw_grid()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if turn == 0:
                figure = Figure('X', x, y, counter)
                all_figures.add(figure)
                turn = 1
            elif turn == 1:
                figure = Figure('O', x, y, counter)
                all_figures.add(figure)
                turn = 0
            counter += 1
    screen.fill(BLACK)
    draw_grid()
    for figure in all_figures.sprites():
        figure.draw(screen)
    all_figures.update(counter)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()