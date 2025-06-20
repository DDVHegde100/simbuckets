import pygame
import sys

class InputHandler:
    def handle_events(self, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
