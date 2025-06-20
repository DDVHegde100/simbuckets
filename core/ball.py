from OpenGL.GL import *
from OpenGL.GLUT import glutSolidSphere
from pyrr import Vector3

class Ball:
    def __init__(self):
        self.position = Vector3([1.0, 0.25, -2.0])
        self.size = 0.25

    def update(self, player):
        pass 

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glColor3f(1.0, 0.5, 0.0)
        glutSolidSphere(self.size, 16, 16)
        glPopMatrix()
