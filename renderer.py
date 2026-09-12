from engine import Vector2, RigidBody, shapes
from config import PIXELS_PER_METER as PPM
import pygame


def draw_all(screen: pygame.Surface, bodies: list[RigidBody]) -> None:
    for body in bodies:
        if isinstance(body.shape, shapes.Circle):
            pygame.draw.circle(screen, (127, 127, 127), to_screen(body.pos), to_screen_scalar(body.shape.r))

        if isinstance(body.shape, shapes.Rectangle):
            pygame.draw.rect(screen, (127, 127, 127), to_screen_rect(body))
    pygame.display.flip()

def to_screen(pos: Vector2) -> pygame.Vector2:
    return pygame.Vector2(pos.x * PPM, pos.y * PPM)

def to_screen_scalar(length: float) -> float:
    return length * PPM

def to_screen_rect(body: RigidBody) -> pygame.Rect:
    assert isinstance(body.shape, shapes.Rectangle)
    left = body.pos.x - body.shape.width / 2
    top = body.pos.y - body.shape.height / 2
    return pygame.Rect(to_screen_scalar(left), to_screen_scalar(top), to_screen_scalar(body.shape.width), to_screen_scalar(body.shape.height))