import pygame
import config

def draw_court(screen):
    screen.fill(config.COURT_COLOR)

    pygame.draw.rect(
        screen, config.LINE_COLOR,
        (config.COURT_MARGIN, config.COURT_MARGIN,
         config.WINDOW_WIDTH - 2 * config.COURT_MARGIN,
         config.WINDOW_HEIGHT - 2 * config.COURT_MARGIN), 4
    )

    pygame.draw.arc(
        screen, config.LINE_COLOR,
        (config.WINDOW_WIDTH / 2 - 60, config.COURT_MARGIN + 50, 120, 120),
        0, 3.14159, 4
    )

    pygame.draw.circle(
        screen, config.LINE_COLOR,
        (config.WINDOW_WIDTH // 2, config.COURT_MARGIN),
        config.BASKET_RADIUS, 4
    )
