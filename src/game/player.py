# src/game/player.py

from core.vector3 import Vector3

class Player:
    def __init__(self, start_pos):
        self.position = start_pos.copy()

    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy

    def shoot_ball(self, target_pos, force):
        # Simplified: calculate 3D velocity vector needed
        displacement = target_pos - self.position
        time = displacement.length() / force

        velocity = Vector3(
            displacement.x / time,
            displacement.y / time,
            (displacement.z + 0.5 * 9.81 * time**2) / time
        )

        return velocity
