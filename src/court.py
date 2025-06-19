import pygame
import config
import math

def draw_court(screen):
    screen.fill(config.COURT_COLOR)

    margin = config.COURT_MARGIN
    width = config.WINDOW_WIDTH
    height = config.WINDOW_HEIGHT
    center_x = width // 2

    # Court boundaries
    pygame.draw.rect(screen, config.LINE_COLOR, (margin, margin, width - 2 * margin, height - 2 * margin), 3)
    backboard_y = config.BACKBOARD_TOP_Y

    # Backboard
    backboard_y = margin + 40
    pygame.draw.line(screen, config.LINE_COLOR, (center_x - 30, backboard_y), (center_x + 30, backboard_y), 4)

    # Rim (Hoop)
    hoop_y = backboard_y + 10
    pygame.draw.circle(screen, config.LINE_COLOR, (center_x, hoop_y), config.BASKET_RADIUS, 3)

    # Key (Free throw lane / Paint)
    key_width = 120
    key_height = 190
    pygame.draw.rect(screen, config.LINE_COLOR, (center_x - key_width // 2, margin, key_width, key_height), 3)

    # Free-throw circle (full)
    ft_circle_rect = pygame.Rect(center_x - 60, backboard_y + 90, 120, 120)
    pygame.draw.ellipse(screen, config.LINE_COLOR, ft_circle_rect, 2)

    # 3-point arc
    arc_radius = 220
    pygame.draw.arc(
        screen, config.LINE_COLOR,
        (center_x - arc_radius, hoop_y - arc_radius, 2 * arc_radius, 2 * arc_radius),
        math.pi, 0, 3
    )

    # Vertical corner three side lines from top baseline down to arc ends
    left_corner_x = center_x - arc_radius
    right_corner_x = center_x + arc_radius
    arc_top_y = hoop_y + arc_radius
    top_baseline_y = margin

    pygame.draw.line(screen, config.LINE_COLOR, (left_corner_x, top_baseline_y), (left_corner_x, arc_top_y), 3)
    pygame.draw.line(screen, config.LINE_COLOR, (right_corner_x, top_baseline_y), (right_corner_x, arc_top_y), 3)

    # Baseline (bottom)
    pygame.draw.line(screen, config.LINE_COLOR, (margin, height - margin), (width - margin, height - margin), 3)
