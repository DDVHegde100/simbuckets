# main.py

import pygame
import config
from court import draw_court
from player import Player
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption("SimBuckets")
clock = pygame.time.Clock()

player = Player(config.WINDOW_WIDTH // 2 - 15, config.WINDOW_HEIGHT - 100)
ball = Ball(player)


running = True
while running:
    clock.tick(config.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shooting event — press SPACE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball.shoot(config.WINDOW_WIDTH // 2, config.COURT_MARGIN + config.BASKET_RADIUS)

    keys = pygame.key.get_pressed()
    player.move(keys)

    # Update ball physics
    ball.update(player)


    # Draw everything
    draw_court(screen)
    player.draw(screen)
    ball.draw(screen)

    pygame.display.flip()

pygame.quit()
