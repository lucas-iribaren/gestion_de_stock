import pygame
import mysql.connector

class Element:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="F1m13I12l5*",
            database="store"
        )
        self.cursor = self.db.cursor()
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (122, 122, 122)
        self.W = 800 
        self.H = 600
        self.screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("Gestion de Stock")

        button_add_product = pygame.Rect(50, 50, 200, 50)
        button_view_stock = pygame.Rect(50, 150, 200, 50)

        # Font
        font = pygame.font.Font(None, 36)

        def draw_text(text, color, x, y):
            surface = font.render(text, True, color)
            screen.blit(surface, (x, y))

