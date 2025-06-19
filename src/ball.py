# ball.py

import pygame
import config
import math
import random

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.vel_x = 0
        self.vel_y = 0
        self.in_motion = False

    def draw(self, screen):
        pygame.draw.circle(
            screen, config.BALL_COLOR,
            (int(self.x), int(self.y)),
            self.radius
        )

    def shoot(self, target_x, target_y):
        if not self.in_motion:
            # Simple projectile motion approximation
            dx = target_x - self.x
            dy = target_y - self.y
            distance = math.hypot(dx, dy)

            # Set velocity components proportional to distance
            speed_factor = 10
            self.vel_x = (dx / distance) * speed_factor
            self.vel_y = (dy / distance) * speed_factor
            self.in_motion = True

    def update(self):
        if self.in_motion:
            self.x += self.vel_x
            self.y += self.vel_y

            # Gravity-like effect on y-axis
            self.vel_y += 0.3  # gravity

            # Check for "score" condition or miss
            if self.y <= config.COURT_MARGIN + config.BASKET_RADIUS:
                self.check_shot_result()

            # Out of bounds check
            if self.y > config.WINDOW_HEIGHT or self.x < 0 or self.x > config.WINDOW_WIDTH:
                self.reset()

    def check_shot_result(self):
        # Probability based on vertical distance
        success_chance = max(20, 90 - int(abs(self.x - config.WINDOW_WIDTH // 2) * 0.5))  # closer to center = higher chance

        if random.randint(0, 100) < success_chance:
            print("🟢 Score!")
        else:
            print("🔴 Miss!")

        self.reset()

    def reset(self):
        self.x = config.WINDOW_WIDTH // 2
        self.y = config.COURT_MARGIN + config.BASKET_RADIUS + 50
        self.vel_x = 0
        self.vel_y = 0
        self.in_motion = False
