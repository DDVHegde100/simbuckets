# court.py

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
    # 3-point line corner side lines (short horizontal segments)
    left_corner_x = center_x - arc_radius
    right_corner_x = center_x + arc_radius
    arc_bottom_y = hoop_y + arc_radius

    # Length of the short side lines (say 30 pixels)
    side_line_length = 30

    # Draw left horizontal line to sideline
    pygame.draw.line(screen, config.LINE_COLOR, (left_corner_x, arc_bottom_y), (left_corner_x - side_line_length, arc_bottom_y), 3)

    # Draw right horizontal line to sideline
    pygame.draw.line(screen, config.LINE_COLOR, (right_corner_x, arc_bottom_y), (right_corner_x + side_line_length, arc_bottom_y), 3)

    # Baseline (bottom)
    pygame.draw.line(screen, config.LINE_COLOR, (margin, height - margin), (width - margin, height - margin), 3)
