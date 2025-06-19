import pygame
import config
from court import draw_court
from player import Player
from ball import Ball
import math

pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption("SimBuckets: Halfcourt Sim")
clock = pygame.time.Clock()

player = Player(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2)
ball = Ball(player)

shot_power = 0
charging_shot = False

running = True
while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                charging_shot = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and charging_shot:
                rad = math.radians(player.angle)
                ball.velocity_x = math.cos(rad) * shot_power
                ball.velocity_y = math.sin(rad) * shot_power
                ball.velocity_z = shot_power / 2
                ball.moving = True
                charging_shot = False
                shot_power = 0

    player.move(keys)
    player.adjust_angle(keys)
    ball.update(player)

    if charging_shot:
        shot_power += 0.25
        shot_power = min(shot_power, 15)

    draw_court(screen)
    player.draw(screen)
    ball.draw(screen)

    # Draw dotted aim line
    if charging_shot:
        rad = math.radians(player.angle)
        start_x, start_y = player.x, player.y
        for i in range(1, 20):
            dot_x = start_x + math.cos(rad) * i * 10
            dot_y = start_y + math.sin(rad) * i * 10
            pygame.draw.circle(screen, (200, 0, 0), (int(dot_x), int(dot_y)), 3)

    pygame.display.flip()

pygame.quit()
