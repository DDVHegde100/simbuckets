import pygame
import math

class Ball:
    def __init__(self, player):
        self.x = player.x
        self.y = player.y
        self.radius = 10
        self.color = (255, 165, 0)
        self.velocity_x = 0
        self.velocity_y = 0
        self.moving = False

    def update(self, player):
        if not self.moving:
            self.x = player.x
            self.y = player.y
        else:
            self.x += self.velocity_x
            self.y += self.velocity_y
            # Basic air drag
            self.velocity_x *= 0.99
            self.velocity_y *= 0.99

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
