import pygame
from affichage import Affichage
class Element(Affichage):
    def __init__(self):
        Affichage.__init__(self)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (122, 122, 122)


        button_add_product = pygame.Rect(50, 50, 200, 50)
        button_view_stock = pygame.Rect(50, 150, 200, 50)

        # Font
        self.font = pygame.font.Font("Arial", 36)

    def draw_text(self, text, color, x, y):
        self.surface = self.font.render(text, True, color)
        self.screen.blit(self.surface, (x, y))

    def solid_rect(self, color, x, y, largeur, longueur):
        pygame.draw.rect(self.screen,color, (x, y, largeur, longueur))
            
    def light_rect(self, fill_color, border_color, x, y, largeur, longueur, border_width=2):
        # Draw filled inner rectangle
        pygame.draw.rect(self.screen, fill_color, (x, y, largeur, longueur))

        # Draw border
        pygame.draw.rect(self.screen, border_color, (x, y, largeur, longueur), border_width)
