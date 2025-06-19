import pygame
import config
from court import draw_court
from player import Player
from ball import Ball
import math

pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption("SimBuckets: Halfcourt Basketball Sim")
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
                # Fire ball
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - player.x
                dy = mouse_y - player.y
                distance = math.hypot(dx, dy)
                if distance != 0:
                    dx /= distance
                    dy /= distance
                ball.velocity_x = dx * shot_power
                ball.velocity_y = dy * shot_power
                ball.moving = True
                charging_shot = False
                shot_power = 0

    # Player movement
    player.move(keys)
    ball.update(player)

    # Charging power
    if charging_shot:
        shot_power += 0.1
        shot_power = min(shot_power, 10)

    # Draw everything
    draw_court(screen)
    player.draw(screen)
    ball.draw(screen)

    # Draw aiming arrow
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.draw.line(screen, (255, 0, 0), (player.x, player.y), (mouse_x, mouse_y), 2)

    pygame.display.flip()

pygame.quit()
