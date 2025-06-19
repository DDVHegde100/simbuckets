import pygame
import config

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10

    def draw(self, screen):
        pygame.draw.circle(
            screen, config.BALL_COLOR,
            (int(self.x), int(self.y)),
            self.radius
        )
