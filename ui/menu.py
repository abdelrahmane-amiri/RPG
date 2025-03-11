import pygame
import math
from config import *
from img import *

class bg:
    def __init__(self, WIDTH=800, HEIGHT=600):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.running = True
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.current_page = "menu"  # Page actuelle
        self.background = pygame.transform.scale(pygame.image.load('img/background.png'), (self.WIDTH, self.HEIGHT))
        self.button = [{"rect": pygame.Rect(300, 350, 200, 60), "text": "Jouer !", "action": self.start_game}]  
        self.temps_initial = pygame.time.get_ticks()  
        self.font_path = "fighting-spirit-tbs.regular.ttf"
        self.custom_font = pygame.font.Font(self.font_path, 36) 
        self.title_font = pygame.font.Font(self.font_path, 80)  # Police pour le titre
        self.page_font = pygame.font.Font(self.font_path, 50)   # Police pour le premier texte
        self.page_font2 = pygame.font.Font(self.font_path, 24)  # Police pour le texte justifié

        # Charger l'image du curseur et la redimensionner
        self.cursor_img = pygame.image.load('img/cursorepee.png')
        self.cursor_img = pygame.transform.scale(self.cursor_img, (30, 30))    
        self.cursor_rect = self.cursor_img.get_rect()  

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))  
    
    def cursor(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if (0 <= mouse_pos[0] < self.WIDTH) and (0 <= mouse_pos[1] < self.HEIGHT):
            self.cursor_rect.center = mouse_pos 
            self.screen.blit(self.cursor_img, self.cursor_rect)

    def title(self):
        text_color = (165, 37, 37) 
        outline_color = (0, 0, 0)   
        outline_thickness = 1          

        title_text = self.title_font.render("The Legend", True, text_color)
        outline_text = self.title_font.render("The Legend", True, outline_color)

        title_rect = title_text.get_rect(center=(self.WIDTH // 2, 80))

        for dx in range(-outline_thickness, outline_thickness + 1):
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:
                    self.screen.blit(outline_text, title_rect.move(dx, dy))

        self.screen.blit(title_text, title_rect)
    
    def draw_rounded_rect(self, surface, color, rect, radius):
        """ Dessiner un rectangle avec des coins arrondis """
        pygame.draw.rect(surface, color, rect, border_radius=radius)
    
    def buttons(self):
        for button in self.button:  
            temps_passé = pygame.time.get_ticks() - self.temps_initial
            facteur_pulsation = 1 + 0.05 * math.sin(temps_passé / 200) 

            self.draw_rounded_rect(self.screen, (50, 50, 50), button["rect"].move(3, 3), 15) 
            self.draw_rounded_rect(self.screen, (0, 0, 0), button["rect"], 15) 

            if button["rect"].collidepoint(pygame.mouse.get_pos()):
                self.draw_rounded_rect(self.screen, (0, 0, 0), button["rect"].inflate(-5, -5), 15)
            else:
                self.draw_rounded_rect(self.screen, (165, 37, 37), button["rect"].inflate(-5, -5), 15) 

            text = self.custom_font.render(button["text"], True, (255, 255, 255))
            text_rect = text.get_rect(center=button["rect"].center)  
            self.screen.blit(text, text_rect)
    
    def start_game(self):
        self.current_page = "game"

    def game_page(self):
        self.screen.fill((0, 0, 0))  
        game_text = self.page_font.render("Il etait une fois", True, (255, 0, 0))
        game_rect = game_text.get_rect(center=(self.WIDTH // 2, 50))  
        self.screen.blit(game_text, game_rect)

        presentation_text = [
            "Link, un jeune epeiste vagabond, erre dans un royaume",
            "oublie par le temps. Arme de son epee legendaire et de",
            "son courage, il doit affronter des ennemis redoutables",
            "pour prendre possession de ce territoire en ruines.",
            "Sur son chemin, il rencontrera des creatures mysterieuses,",
            "des enigmes anciennes et des defis qui mettront a l'epreuve",
            "sa force et son esprit. Son destin est entre ses mains :",
            "parviendra-t-il à restaurer la gloire de ce royaume,",
            "ou sombrera-t-il dans l'oubli ?"
        ]

        y_offset = 170  
        for line in presentation_text:
            text_surface = self.page_font2.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, y_offset))
            self.screen.blit(text_surface, text_rect)
            y_offset += 30  

        space_text = self.page_font2.render("Appuyer sur ESPACE pour continuer", True, (255, 255, 255))
        space_rect = space_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT - 50))
        self.screen.blit(space_text, space_rect)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.button:
                    if button["rect"].collidepoint(event.pos):
                        button["action"]()  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.current_page == "game":
                    self.current_page = "next_page"  # Changez la page ici

    def next_page(self):
        self.screen.fill((0, 0, 0))  
        next_text = self.page_font.render("Nouvelle Page", True, (255, 0, 0))
        next_rect = next_text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(next_text, next_rect)

    def run_game(self):
        pygame.mouse.set_visible(False)

        while self.running:
            self.draw_background()

            if self.current_page == "menu":
                self.title()
                self.buttons()
            elif self.current_page == "game":
                self.game_page()  
            elif self.current_page == "next_page":
                self.next_page()

            self.cursor()  
            self.events()
            pygame.display.update()

pygame.quit()
