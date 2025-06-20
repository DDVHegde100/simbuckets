import pygame
import math

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = (0, 0, 255)
        self.max_speed = 5
        self.acceleration = 0.3
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = -90  # degrees, facing upward initially

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration
        elif keys[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration
        else:
            self.velocity_x = 0

        if keys[pygame.K_UP]:
            self.velocity_y -= self.acceleration
        elif keys[pygame.K_DOWN]:
            self.velocity_y += self.acceleration
        else:
            self.velocity_y = 0

        self.velocity_x = max(-self.max_speed, min(self.velocity_x, self.max_speed))
        self.velocity_y = max(-self.max_speed, min(self.velocity_y, self.max_speed))

        self.x += self.velocity_x
        self.y += self.velocity_y

    def adjust_angle(self, keys):
        if keys[pygame.K_a]:
            self.angle -= 3  # Faster turn
        if keys[pygame.K_d]:
            self.angle += 3

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)