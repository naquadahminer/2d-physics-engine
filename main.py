from __future__ import annotations
from engine import RigidBody, shapes, World, Vector2
import pygame
import config
import renderer

TEST_ACCELERATION = 10.0

pygame.init()

screen = pygame.display.set_mode((640, 640))
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

clock = pygame.time.Clock()

world = World(SCREEN_WIDTH/config.PIXELS_PER_METER, SCREEN_HEIGHT/config.PIXELS_PER_METER)

running = True
while running:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    
    for body in world.bodies:
        accel = Vector2(0.0, 0.0)
        if pressed_keys[pygame.K_w]:
            accel += Vector2(0.0, -TEST_ACCELERATION)
        if pressed_keys[pygame.K_a]:
            accel += Vector2(-TEST_ACCELERATION, 0.0)
        if pressed_keys[pygame.K_s]:
            accel += Vector2(0.0, TEST_ACCELERATION)
        if pressed_keys[pygame.K_d]:
            accel += Vector2(TEST_ACCELERATION, 0.0)
        body.acceleration = accel


    dt = clock.tick(config.FPS) / 1000
    world.step(dt)

    renderer.draw_all(screen, world.bodies)

pygame.quit()