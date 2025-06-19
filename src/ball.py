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
        self.velocity_z = 0
        self.z = 0
        self.gravity = -0.3
        self.moving = False

    def update(self, player):
        if not self.moving:
            self.x = player.x
            self.y = player.y
            self.z = 0
        else:
            self.x += self.velocity_x
            self.y += self.velocity_y
            self.z += self.velocity_z
            self.velocity_x *= 0.99
            self.velocity_y *= 0.99
            self.velocity_z += self.gravity  # gravity pull down

            if self.z < 0:
                self.z = 0
                self.moving = False

    def draw(self, screen):
        brightness = max(50, min(255, int(255 - self.z * 5)))
        color = (brightness, brightness // 2, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
