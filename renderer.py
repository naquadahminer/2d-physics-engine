from engine import Vector2
from config import PIXELS_PER_METER as PPM
import pygame

def to_screen(pos: Vector2) -> pygame.Vector2:
    return pygame.Vector2(pos.x * PPM, pos.y * PPM)

def to_screen_scalar(length: float) -> float:
    return length * PPM