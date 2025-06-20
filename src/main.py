# src/main.py

import pygame
from core.vector3 import Vector3
from game.ball import Ball
from game.court import Court
from game.player import Player
import settings

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Game objects
court = Court()
player = Player(Vector3(2, 0, 0.12))
ball = Ball(player.position)
score = 0

font = pygame.font.SysFont("Arial", 28)

def draw_ball(surface, ball_obj):
    px = int(ball_obj.position.x * settings.PIXELS_PER_METER)
    py = settings.SCREEN_HEIGHT - int(ball_obj.position.z * settings.PIXELS_PER_METER)
    pygame.draw.circle(surface, settings.ORANGE, (px, py), int(ball_obj.radius * settings.PIXELS_PER_METER))

def draw_hoop(surface):
    cx = int(court.hoop_center.x * settings.PIXELS_PER_METER)
    cy = settings.SCREEN_HEIGHT - int(court.hoop_center.z * settings.PIXELS_PER_METER)
    pygame.draw.circle(surface, settings.WHITE, (cx, cy), int(court.hoop_radius * settings.PIXELS_PER_METER), 3)

def draw_backboard(surface):
    x = int(court.backboard_x * settings.PIXELS_PER_METER)
    y_top = settings.SCREEN_HEIGHT - int((court.hoop_center.z + court.backboard_height/2) * settings.PIXELS_PER_METER)
    y_bottom = settings.SCREEN_HEIGHT - int((court.hoop_center.z - court.backboard_height/2) * settings.PIXELS_PER_METER)
    pygame.draw.line(surface, settings.DARK_GRAY, (x, y_top), (x, y_bottom), 4)

def draw_player(surface, player_obj):
    px = int(player_obj.position.x * settings.PIXELS_PER_METER)
    py = settings.SCREEN_HEIGHT - int(player_obj.position.z * settings.PIXELS_PER_METER)
    pygame.draw.circle(surface, (0, 255, 0), (px, py), 8)

def draw_score(surface, score_val):
    score_text = font.render(f"Score: {score_val}", True, settings.WHITE)
    surface.blit(score_text, (20, 20))

running = True
while running:
    dt = clock.tick(settings.FPS) / 1000.0  # convert ms to seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not ball.in_motion:
                target_pos = Vector3(court.hoop_center.x, 0, court.hoop_center.z)
                force = 10  # adjust force value for difficulty
                velocity = player.shoot_ball(target_pos, force)
                ball.shoot(velocity)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(-5 * dt, 0)
    if keys[pygame.K_d]:
        player.move(5 * dt, 0)

    # Update ball
    ball.update(dt, court)

    if ball.is_made_shot():
        score += 1
        ball.in_motion = False
        ball.made_shot = False

    # Drawing
    screen.fill((0, 0, 0))
    draw_backboard(screen)
    draw_hoop(screen)
    draw_ball(screen, ball)
    draw_player(screen, player)
    draw_score(screen, score)

    pygame.display.flip()

pygame.quit()
