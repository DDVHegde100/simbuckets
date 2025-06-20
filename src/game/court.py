# src/game/court.py

from core.vector3 import Vector3

class Court:
    def __init__(self):
        # Realistic hoop and court settings (in meters)
        self.hoop_center = Vector3(7, 0, 3.05)   # 7m from baseline, 3.05m high
        self.hoop_radius = 0.23                  # 0.23m radius (NBA standard)
        self.backboard_x = 6.95                  # Backboard plane at x=6.95m
        self.backboard_width = 1.80
        self.backboard_height = 1.05
        self.floor_z = 0.0

    def is_ball_in_hoop(self, ball_pos):
        # Check if ball center is within hoop cylinder horizontally and at hoop height
        dx = ball_pos.x - self.hoop_center.x
        dy = ball_pos.y - self.hoop_center.y
        dz = ball_pos.z - self.hoop_center.z

        distance_xy = (dx**2 + dy**2)**0.5
        within_radius = distance_xy <= self.hoop_radius * 0.9  # 0.9 fudge factor

        falling_through = ball_pos.z <= self.hoop_center.z + 0.05 and ball_pos.z >= self.hoop_center.z - 0.15

        return within_radius and falling_through

    def check_backboard_collision(self, ball_pos, ball_radius):
        if (abs(ball_pos.x - self.backboard_x) <= ball_radius and
            abs(ball_pos.y) <= self.backboard_width / 2 and
            ball_pos.z <= self.hoop_center.z + self.backboard_height / 2 and
            ball_pos.z >= self.hoop_center.z - self.backboard_height / 2):
            return True
        return False
