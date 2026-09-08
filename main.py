from __future__ import annotations
from engine import RigidBody, shapes, World, Vector2
import pygame

FPS = 60
TEST_ACCELERATION = 10.0

pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

world = World()

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                for body in world.bodies:
                    body.acceleration = Vector2(0.0, -TEST_ACCELERATION)

            elif event.key == pygame.K_a:
                for body in world.bodies:
                    body.acceleration = Vector2(-TEST_ACCELERATION, 0.0)
                    
            elif event.key == pygame.K_s:
                for body in world.bodies:
                    body.acceleration = Vector2(0.0, TEST_ACCELERATION)
                    
            elif event.key == pygame.K_d:
                for body in world.bodies:
                    body.acceleration = Vector2(TEST_ACCELERATION, 0.0)
                    
            else:
                for body in world.bodies:
                    body.acceleration = Vector2(0.0, 0.0)

    dt = clock.tick(FPS) / 1000
    world.step(dt)

    body: RigidBody
    for body in world.bodies:
        if isinstance(body.shape, shapes.Circle):
            pygame.draw.circle(screen, (127, 127, 127), pygame.Vector2(body.pos.x, body.pos.y), body.shape.r)
    pygame.display.flip()

pygame.quit()