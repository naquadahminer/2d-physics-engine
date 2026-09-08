from __future__ import annotations
from .vector2 import Vector2
from . import shapes

# the engine will use SI units for all physics calculations
class RigidBody:
    def __init__(self, shape: shapes.Shape, mass: float, pos: Vector2, velocity: Vector2, acceleration: Vector2):
        self.shape = shape
        self.mass = mass
        self.pos = pos
        self.velocity = velocity
        self.acceleration = acceleration

    def integrate(self, dt: float):
        self.velocity += self.acceleration * dt
        self.pos += self.velocity * dt