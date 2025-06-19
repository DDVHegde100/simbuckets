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
ball = Ball(config.WINDOW_WIDTH // 2, config.COURT_MARGIN + config.BASKET_RADIUS + 50)

running = True
while running:
    clock.tick(config.FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    draw_court(screen)
    player.draw(screen)
    ball.draw(screen)

    pygame.display.flip()
pygame.quit()
