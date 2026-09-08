from __future__ import annotations
import pygame, shapes
from rigidbody import RigidBody
from world import World

pygame.init()

screen = pygame.display.set_mode((640, 480))

world = World()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    body: RigidBody
    for body in world.bodies:
        if isinstance(body.shape, shapes.Circle):
            pygame.draw.circle(screen, pygame.Color(127, 127, 127), pygame.Vector2(body.pos[0], body.pos[1]), body.shape.r)
    pygame.display.flip()

pygame.quit()