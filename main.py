import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit
from ui.renderer import Renderer
from ui.input_handler import InputHandler
from core.player import Player
from core.ball import Ball

pygame.init()
glutInit()
screen = pygame.display.set_mode((1280, 720), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("Half-Court Basketball Simulator")

glEnable(GL_DEPTH_TEST)
gluPerspective(45, (1280 / 720), 0.1, 100.0)
glTranslatef(0.0, -5.0, -40)
glRotatef(35, 1, 0, 0)
glRotatef(-45, 0, 1, 0)

renderer = Renderer()
input_handler = InputHandler()
player = Player()
ball = Ball()
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    input_handler.handle_events(player)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    renderer.draw_court()
    player.update()
    ball.update(player)
    player.draw()
    ball.draw()

    pygame.display.flip()

pygame.quit()
