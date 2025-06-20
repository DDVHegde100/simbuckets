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
        self.prev_z = 0
        self.gravity = -0.3
        self.moving = False
        self.in_possession = True
        self.made_shot = False

    def update(self, player):
        if self.in_possession:
            self.x = player.x
            self.y = player.y
            self.prev_z = self.z
            self.z = 0
        else:
            self.x += self.velocity_x
            self.y += self.velocity_y
            self.z += self.velocity_z

            self.velocity_x *= 0.99
            self.velocity_y *= 0.99
            self.velocity_z += self.gravity


            # Check for made shot crossing hoop plane
            rim_x = config.WINDOW_WIDTH // 2
            rim_y = config.COURT_MARGIN + 60
            rim_radius = config.BASKET_RADIUS

            if (self.prev_z > 0 and self.z <= 0 and
                math.hypot(self.x - rim_x, self.y - rim_y) <= rim_radius and
                not self.in_possession):
                self.made_shot = True
            else:
                self.made_shot = False

            if (config.BACKBOARD_LEFT_X <= self.x <= config.BACKBOARD_RIGHT_X) and self.y - self.radius <= config.BACKBOARD_TOP_Y:
                self.velocity_y *= -0.8
                self.y = config.BACKBOARD_TOP_Y + self.radius

            # Ball hits ground
            if self.z < 0:
                self.z = 0
                self.velocity_z = 0

            # Rim collision
            rim_x = config.WINDOW_WIDTH // 2
            rim_y = config.COURT_MARGIN + 60
            rim_radius = config.BASKET_RADIUS

            if math.hypot(self.x - rim_x, self.y - rim_y) <= self.radius + rim_radius:
                dx = self.x - rim_x
                dy = self.y - rim_y
                dist = math.hypot(dx, dy)
                if dist == 0:
                    dist = 0.1
                nx = dx / dist
                ny = dy / dist

                dot = self.velocity_x * nx + self.velocity_y * ny
                self.velocity_x -= 2 * dot * nx
                self.velocity_y -= 2 * dot * ny

                self.velocity_x *= 0.8
                self.velocity_y *= 0.8

                overlap = self.radius + rim_radius - dist
                self.x += nx * overlap
                self.y += ny * overlap

            # Out of bounds
            if not (config.COURT_MARGIN <= self.x <= config.WINDOW_WIDTH - config.COURT_MARGIN and
                    config.COURT_MARGIN <= self.y <= config.WINDOW_HEIGHT - config.COURT_MARGIN):
                self.x = config.WINDOW_WIDTH // 2
                self.y = config.WINDOW_HEIGHT // 2 + 100
                self.velocity_x = 0
                self.velocity_y = 0
                self.velocity_z = 0
                self.z = 0
                self.moving = False
                self.in_possession = True

            # Player recovers ball
            if math.hypot(player.x - self.x, player.y - self.y) <= self.radius + player.radius:
                self.in_possession = True
                self.moving = False

    def is_made_shot(self):
        return self.made_shot

    def draw(self, screen):
        brightness = max(50, min(255, int(255 - self.z * 5)))
        color = (brightness, brightness // 2, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)