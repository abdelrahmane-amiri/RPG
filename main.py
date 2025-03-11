import pygame
from config import *
from ui.menu import bg
from img import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG")

background = bg()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background.run_game()  
    pygame.display.update()
