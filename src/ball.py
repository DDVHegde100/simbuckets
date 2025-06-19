# ball.py

import pygame
import config
import math
import random

class Ball:
    def __init__(self, player):
        self.radius = 10
        self.attach_to_player(player)
        self.vel_x = 0
        self.vel_y = 0
        self.in_motion = False

    def attach_to_player(self, player):
        self.x = player.x + player.width // 2
        self.y = player.y - self.radius * 2

    def draw(self, screen):
        pygame.draw.circle(
            screen, config.BALL_COLOR,
            (int(self.x), int(self.y)),
            self.radius
        )

    def shoot(self, target_x, target_y):
        if not self.in_motion:
            dx = target_x - self.x
            dy = target_y - self.y
            distance = math.hypot(dx, dy)

            speed_factor = 14
            self.vel_x = (dx / distance) * speed_factor
            self.vel_y = (dy / distance) * speed_factor
            self.in_motion = True

    def update(self, player):
        if self.in_motion:
            self.x += self.vel_x
            self.y += self.vel_y

            self.vel_y += 0.4  # gravity

            if self.y < config.COURT_MARGIN + config.BASKET_RADIUS:
                self.check_shot_result()

            if self.y > config.WINDOW_HEIGHT or self.x < 0 or self.x > config.WINDOW_WIDTH:
                self.reset(player)
        else:
            self.attach_to_player(player)

    def check_shot_result(self):
        hoop_center_x = config.WINDOW_WIDTH // 2
        distance_from_center = abs(self.x - hoop_center_x)

        success_chance = max(20, 90 - int(distance_from_center * 0.5))

        if random.randint(0, 100) < success_chance:
            print("🟢 Score!")
        else:
            print("🔴 Miss!")

        self.in_motion = False

    def reset(self, player):
        self.vel_x = 0
        self.vel_y = 0
        self.in_motion = False
        self.attach_to_player(player)
