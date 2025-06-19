import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = (0, 0, 255)
        self.max_speed = 5
        self.acceleration = 0.3
        self.velocity_x = 0
        self.velocity_y = 0

    def move(self, keys):
        # Horizontal
        if keys[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration
        elif keys[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration
        else:
            self.velocity_x = 0

        # Vertical
        if keys[pygame.K_UP]:
            self.velocity_y -= self.acceleration
        elif keys[pygame.K_DOWN]:
            self.velocity_y += self.acceleration
        else:
            self.velocity_y = 0

        # Limit speed
        self.velocity_x = max(-self.max_speed, min(self.velocity_x, self.max_speed))
        self.velocity_y = max(-self.max_speed, min(self.velocity_y, self.max_speed))

        # Apply movement
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
