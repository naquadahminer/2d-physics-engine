from vector2 import Vector2
import shapes
from __future__ import annotations

# the engine will use SI units for all physics calculations
class RigidBody:
    def __init__(self, shape: shapes.Circle, mass: float, pos: tuple[float, float], velocity: Vector2):
        self.mass = mass
        self.pos = pos
        self.velocity = velocity