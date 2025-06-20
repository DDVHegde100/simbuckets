# src/game/ball.py

from core.vector3 import Vector3

class Ball:
    def __init__(self, start_pos):
        self.position = start_pos.copy()
        self.velocity = Vector3()
        self.radius = 0.12   # basketball radius in meters
        self.in_motion = False
        self.made_shot = False
        self.trail = []

        # physics
        self.gravity = -9.81   # m/s²
        self.air_drag = 0.02   # arbitrary

    def shoot(self, velocity):
        self.velocity = velocity.copy()
        self.in_motion = True
        self.made_shot = False
        self.trail.clear()

    def update(self, dt, court):
        if not self.in_motion:
            return

        # Apply gravity
        self.velocity.z += self.gravity * dt

        # Apply air resistance
        self.velocity.x *= (1 - self.air_drag)
        self.velocity.y *= (1 - self.air_drag)
        self.velocity.z *= (1 - self.air_drag)

        # Update position
        self.position += self.velocity * dt
        self.trail.append(self.position.copy())

        # Floor collision
        if self.position.z <= court.floor_z + self.radius:
            self.position.z = court.floor_z + self.radius
            self.velocity.z *= -0.7  # dampened bounce

        # Backboard collision
        if court.check_backboard_collision(self.position, self.radius):
            self.velocity.x *= -0.8

        # Hoop scoring check
        if court.is_ball_in_hoop(self.position) and self.velocity.z < 0:
            self.made_shot = True
            self.in_motion = False

        # Stop dead if motion too low
        if self.velocity.length() < 0.5 and self.position.z <= court.floor_z + self.radius + 0.01:
            self.in_motion = False

    def is_made_shot(self):
        return self.made_shot
