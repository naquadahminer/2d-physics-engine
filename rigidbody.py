from __future__ import annotations
from vector2 import Vector2
import shapes

# the engine will use SI units for all physics calculations
class RigidBody:
    def __init__(self, shape: shapes.Shape, mass: float, pos: tuple[float, float], velocity: Vector2):
        self.shape = shape
        self.mass = mass
        self.pos = pos
        self.velocity = velocity