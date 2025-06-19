import pygame
import math
import config

class Ball:
    def __init__(self, player):
        self.x = player.x
        self.y = player.y
        self.radius = 10
        self.color = config.BALL_COLOR
        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity_z = 0
        self.z = 0
        self.gravity = -0.3
        self.moving = False
        self.in_possession = True

    def update(self, player):
        if self.in_possession:
            self.x = player.x
            self.y = player.y
            self.z = 0
        else:
            self.x += self.velocity_x
            self.y += self.velocity_y
            self.z += self.velocity_z

            self.velocity_x *= 0.99
            self.velocity_y *= 0.99
            self.velocity_z += self.gravity

            # Rebound off backboard
            if (config.BACKBOARD_LEFT_X <= self.x <= config.BACKBOARD_RIGHT_X) and self.y - self.radius <= config.BACKBOARD_TOP_Y:
                self.velocity_y *= -0.8  # reverse & dampen
                self.y = config.BACKBOARD_TOP_Y + self.radius

            # Ball hits ground
            if self.z < 0:
                self.z = 0
                self.velocity_z = 0

            # Out of bounds check
            if not (config.COURT_MARGIN <= self.x <= config.WINDOW_WIDTH - config.COURT_MARGIN and
                    config.COURT_MARGIN <= self.y <= config.WINDOW_HEIGHT - config.COURT_MARGIN):
                self.moving = False

            # Check if player recovers ball
            if math.hypot(player.x - self.x, player.y - self.y) <= self.radius + player.radius:
                self.in_possession = True
                self.moving = False

    def draw(self, screen):
        brightness = max(50, min(255, int(255 - self.z * 5)))
        color = (brightness, brightness // 2, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
