import pygame
from config import *

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen = pygame.display.set_caption("RPG")

def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.update()

main()