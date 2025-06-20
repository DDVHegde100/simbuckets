import pygame
from OpenGL.GL import *
from OpenGL.GLUT import glutSolidCube
from pyrr import Vector3

class Player:
    def __init__(self):
        self.position = Vector3([0.0, 0.0, 0.0])
        self.speed = 0.15
        self.size = 0.5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.position.x -= self.speed
        if keys[pygame.K_RIGHT]: self.position.x += self.speed
        if keys[pygame.K_UP]: self.position.z -= self.speed
        if keys[pygame.K_DOWN]: self.position.z += self.speed

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y + self.size / 2, self.position.z)
        glColor3f(1.0, 0.0, 0.0)
        self.draw_cube(self.size)
        glPopMatrix()

    def draw_cube(self, size):
        hs = size / 2  # half size
        vertices = [
            [-hs, -hs, -hs],
            [ hs, -hs, -hs],
            [ hs,  hs, -hs],
            [-hs,  hs, -hs],
            [-hs, -hs,  hs],
            [ hs, -hs,  hs],
            [ hs,  hs,  hs],
            [-hs,  hs,  hs],
        ]

        faces = [
            [0, 1, 2, 3],
            [1, 5, 6, 2],
            [5, 4, 7, 6],
            [4, 0, 3, 7],
            [3, 2, 6, 7],
            [0, 1, 5, 4]
        ]

        glBegin(GL_QUADS)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()
