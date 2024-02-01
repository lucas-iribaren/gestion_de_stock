import pygame
import sys
from element import Element 

pygame.init()

class Main(Element):
    def __init__(self):
        Element.__init__(self) 
    def main(self):
        while True:
            self.screen.fill(self.white)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type:
                    self.eventType(event)

            self.solid_rect(self.black,100,100,100,100)
    def eventType(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.KEYDOWN:
            pass

main = Main()

main.main()