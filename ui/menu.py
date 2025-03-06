import pygame
from config import *

class bg:
    def __init__(self, WIDTH=800, HEIGHT=600):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.running = True
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.button_rect = None
        self.on_page2 = False  
    
    def background(bg):
        super().__init__(self)
        self.background = pygame.transform.scale(pygame.image.load('background.png'), (800, 600))
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
