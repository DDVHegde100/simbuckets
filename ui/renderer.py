from OpenGL.GL import *
import math

class Renderer:
    def draw_court(self):
        glColor3f(0.2, 0.7, 0.2)  # Green court surface
        glBegin(GL_QUADS)
        glVertex3f(-7.5, 0, -14)
        glVertex3f(7.5, 0, -14)
        glVertex3f(7.5, 0, 0)
        glVertex3f(-7.5, 0, 0)
        glEnd()
        self.draw_lines()

    def draw_lines(self):
        glColor3f(1.0, 1.0, 1.0)
        glLineWidth(2)
        glBegin(GL_LINES)

        # Half court line
        glVertex3f(-7.5, 0.01, -7)
        glVertex3f(7.5, 0.01, -7)

        # Free throw lane
        for x in [-2.4, 2.4]:
            glVertex3f(x, 0.01, -5.8)
            glVertex3f(x, 0.01, -0.6)
        glVertex3f(-2.4, 0.01, -0.6)
        glVertex3f(2.4, 0.01, -0.6)

        # 3-point arc
        cx, cz, r = 0.0, -1.0, 6.75
        for i in range(0, 181, 5):
            theta1 = math.radians(i)
            theta2 = math.radians(i + 5)
            x1, z1 = r * math.cos(theta1), cz + r * math.sin(theta1)
            x2, z2 = r * math.cos(theta2), cz + r * math.sin(theta2)
            glVertex3f(x1, 0.01, z1)
            glVertex3f(x2, 0.01, z2)

        glEnd()
