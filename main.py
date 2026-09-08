from __future__ import annotations
from engine import RigidBody, shapes, World, Vector2
import pygame

FPS = 60

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

world = World()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_w:
            for body in world.bodies:
                body.acceleration = Vector2(0.0, 1.0)
                
        elif event.type == pygame.K_a:
            for body in world.bodies:
                body.acceleration = Vector2(-1.0, 0.0)
                
        elif event.type == pygame.K_s:
            for body in world.bodies:
                body.acceleration = Vector2(0.0, -1.0)
                
        elif event.type == pygame.K_d:
            for body in world.bodies:
                body.acceleration = Vector2(1.0, 0.0)
                
        else:
            for body in world.bodies:
                body.acceleration = Vector2(0.0, 0.0)

    dt = clock.tick(FPS) / 1000
    world.step(dt)

    body: RigidBody
    for body in world.bodies:
        if isinstance(body.shape, shapes.Circle):
            pygame.draw.circle(screen, pygame.Color(127, 127, 127), pygame.Vector2(body.pos.x, body.pos.y), body.shape.r)
    pygame.display.flip()

pygame.quit()