import pygame

class Affichage:
    def __init__(self):
        self.W = 800 
        self.H = 600

        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Gestion de Stock")
