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

font = pygame.font.SysFont("arial", 24)

player = Player(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT // 2)
ball = Ball(player)

shot_power = 0
charging_shot = False
shots_taken = 0
shots_made = 0

running = True
while running:
    clock.tick(config.FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ball.in_possession:
                charging_shot = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and charging_shot:
                rad = math.radians(player.angle)
                if ball.in_possession:
                    ball.velocity_x = math.cos(rad) * shot_power
                    ball.velocity_y = math.sin(rad) * shot_power
                    ball.velocity_z = shot_power / 2

                    distance_from_hoop = math.hypot(player.x - config.WINDOW_WIDTH // 2, player.y - (config.COURT_MARGIN + 60))
                    if distance_from_hoop < 70:
                        shot_type = "1PT"
                    elif distance_from_hoop < 160:
                        shot_type = "2PT"
                    else:
                        shot_type = "3PT"

                    print(f"Shot attempted: {shot_type} from {int(distance_from_hoop)} pixels")

                    ball.moving = True
                    ball.in_possession = False
                    charging_shot = False
                    shots_taken += 1
                    shot_power = 0

    player.move(keys)
    player.adjust_angle(keys)
    ball.update(player)

    # Check for made shot
    if ball.is_made_shot():
        shots_made += 1
        print("Shot made!")
        ball.in_possession = True
        ball.moving = False
        ball.z = 0
        ball.velocity_x = ball.velocity_y = ball.velocity_z = 0
        ball.x = config.WINDOW_WIDTH // 2
        ball.y = config.WINDOW_HEIGHT // 2 + 100

    if charging_shot:
        shot_power += 0.25
        shot_power = min(shot_power, 15)

    draw_court(screen)
    player.draw(screen)
    ball.draw(screen)

    rad = math.radians(player.angle)
    arrow_len = 40
    end_x = player.x + math.cos(rad) * arrow_len
    end_y = player.y + math.sin(rad) * arrow_len
    pygame.draw.line(screen, (255, 0, 0), (player.x, player.y), (end_x, end_y), 3)

    if charging_shot:
        for i in range(1, int(shot_power) * 2):
            dot_x = player.x + math.cos(rad) * i * 10
            dot_y = player.y + math.sin(rad) * i * 10
            pygame.draw.circle(screen, (200, 0, 0), (int(dot_x), int(dot_y)), 3)

    # Draw scoreboard
    score_text = font.render(f"{shots_made} / {shots_taken}", True, config.BLACK)
    screen.blit(score_text, (config.SCOREBOARD_X, config.SCOREBOARD_Y))

    pygame.display.flip()

pygame.quit()
